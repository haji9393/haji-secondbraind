---
name: "regex-vs-llm-structured-text"
description: "Parse forms, invoices and tables regex-first, flag low-confidence items, and send only those edge cases to an LLM."
group: "ECC · Research"
---

# Trích và đối soát dữ liệu CS

1. Kiểm tra định dạng thực tế. Với XLSX/CSV, đọc theo sheet, cột và kiểu dữ liệu. Với JSON, đọc theo khóa và cấu trúc lồng nhau. Với văn bản lặp mẫu, có thể dùng regex cho từng trường. Với bản scan, trích bằng OCR rồi đối chiếu với ảnh khi ký tự hoặc giá trị còn mơ hồ.
2. Chốt đơn vị đầu vào (dòng giao dịch, hóa đơn hay một biểu mẫu). Lập danh sách bản ghi từ nguồn trước khi trích, ghi vị trí như tên file + sheet + dòng hoặc trang + số thứ tự. Với chứng từ nhiều dòng, giữ liên kết giữa các dòng và chứng từ. Ghi riêng tiêu đề, dòng tổng và dòng trống đã loại khỏi phạm vi.
3. Với mỗi bản ghi, kiểm tra trường bắt buộc, kiểu dữ liệu, tiền tệ và quy ước dấu thập phân phù hợp với nguồn. Ghi một trong hai trạng thái: đã trích hợp lệ hoặc chờ kiểm tra kèm lý do và vị trí. Dòng không khớp mẫu và dòng nghi trùng đều cần được ghi nhận.
4. Trước khi gộp hoặc pivot, đối chiếu tập vị trí nguồn: mỗi vị trí thuộc đúng một trạng thái. Kiểm tra **số đầu vào = số hợp lệ + số chờ kiểm tra**. Với trường tiền, so tổng theo cùng loại tiền và cùng phạm vi nếu nguồn có tổng kiểm soát. Ghi phần số liệu còn chờ xử lý vào báo cáo.
5. Ví dụ: file CSV có ba dòng giao dịch, dòng thứ hai thiếu đơn vị tiền tệ. Kết quả gồm hai dòng hợp lệ và một dòng chờ kiểm tra, giữ số dòng gốc. Nếu cần AI hỗ trợ đọc ngoại lệ, chỉ đưa phần liên quan và kiểm lại với chứng từ trước khi chấp nhận.

## Ví dụ tham khảo từ nguồn ECC

Đoạn mã dưới đây minh họa việc đọc câu hỏi trắc nghiệm từ văn bản. Hàm dùng `finditer` chỉ trả phần khớp, nên khi áp dụng phải đối chiếu với danh sách đầu vào ở bước 2. Hàm gọi mô hình để ngỏ phần đọc phản hồi. Các ngưỡng điểm và kết quả ở cuối ví dụ thuộc bộ câu hỏi của tác giả. Chọn tiêu chí kiểm tra cho từng bộ dữ liệu CS dựa trên mẫu đã đối chiếu thực tế.

### 1. Regex Parser (Handles the Majority)

```python
import re
from dataclasses import dataclass

@dataclass(frozen=True)
class ParsedItem:
    id: str
    text: str
    choices: tuple[str, ...]
    answer: str
    confidence: float = 1.0

def parse_structured_text(content: str) -> list[ParsedItem]:
    """Parse structured text using regex patterns."""
    pattern = re.compile(
        r"(?P<id>\d+)\.\s*(?P<text>.+?)\n"
        r"(?P<choices>(?:[A-D]\..+?\n)+)"
        r"Answer:\s*(?P<answer>[A-D])",
        re.MULTILINE | re.DOTALL,
    )
    items = []
    for match in pattern.finditer(content):
        choices = tuple(
            c.strip() for c in re.findall(r"[A-D]\.\s*(.+)", match.group("choices"))
        )
        items.append(ParsedItem(
            id=match.group("id"),
            text=match.group("text").strip(),
            choices=choices,
            answer=match.group("answer"),
        ))
    return items
```

### 2. Confidence Scoring

Flag items that may need LLM review:

```python
@dataclass(frozen=True)
class ConfidenceFlag:
    item_id: str
    score: float
    reasons: tuple[str, ...]

def score_confidence(item: ParsedItem) -> ConfidenceFlag:
    """Score extraction confidence and flag issues."""
    reasons = []
    score = 1.0

    if len(item.choices) < 3:
        reasons.append("few_choices")
        score -= 0.3

    if not item.answer:
        reasons.append("missing_answer")
        score -= 0.5

    if len(item.text) < 10:
        reasons.append("short_text")
        score -= 0.2

    return ConfidenceFlag(
        item_id=item.id,
        score=max(0.0, score),
        reasons=tuple(reasons),
    )

def identify_low_confidence(
    items: list[ParsedItem],
    threshold: float = 0.95,
) -> list[ConfidenceFlag]:
    """Return items below confidence threshold."""
    flags = [score_confidence(item) for item in items]
    return [f for f in flags if f.score < threshold]
```

### 3. LLM Validator (Edge Cases Only)

```python
def validate_with_llm(
    item: ParsedItem,
    original_text: str,
    client,
) -> ParsedItem:
    """Use LLM to fix low-confidence extractions."""
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",  # Cheapest model for validation
        max_tokens=500,
        messages=[{
            "role": "user",
            "content": (
                f"Extract the question, choices, and answer from this text.\n\n"
                f"Text: {original_text}\n\n"
                f"Current extraction: {item}\n\n"
                f"Return corrected JSON if needed, or 'CORRECT' if accurate."
            ),
        }],
    )
    # Parse LLM response and return corrected item...
    return corrected_item
```

### 4. Hybrid Pipeline

```python
def process_document(
    content: str,
    *,
    llm_client=None,
    confidence_threshold: float = 0.95,
) -> list[ParsedItem]:
    """Full pipeline: regex -> confidence check -> LLM for edge cases."""
    # Step 1: Regex extraction (handles 95-98%)
    items = parse_structured_text(content)

    # Step 2: Confidence scoring
    low_confidence = identify_low_confidence(items, confidence_threshold)

    if not low_confidence or llm_client is None:
        return items

    # Step 3: LLM validation (only for flagged items)
    low_conf_ids = {f.item_id for f in low_confidence}
    result = []
    for item in items:
        if item.id in low_conf_ids:
            result.append(validate_with_llm(item, content, llm_client))
        else:
            result.append(item)

    return result
```

## Real-World Metrics

From a production quiz parsing pipeline (410 items):

| Metric | Value |
|--------|-------|
| Regex success rate | 98.0% |
| Low confidence items | 8 (2.0%) |
| LLM calls needed | ~5 |
| Cost savings vs all-LLM | ~95% |
| Test coverage | 93% |

### Ghi chú của tác giả cho ví dụ trắc nghiệm

- **Start with regex** — even imperfect regex gives you a baseline to improve
- **Use confidence scoring** to programmatically identify what needs LLM help
- **Use the cheapest LLM** for validation (Haiku-class models are sufficient)
- **Never mutate** parsed items — return new instances from cleaning/validation steps
- **TDD works well** for parsers — write tests for known patterns first, then edge cases
- **Log metrics** (regex success rate, LLM call count) to track pipeline health

## Anti-Patterns to Avoid

- Sending all text to an LLM when regex handles 95%+ of cases (expensive and slow)
- Using regex for free-form, highly variable text (LLM is better here)
- Skipping confidence scoring and hoping regex "just works"
- Mutating parsed objects during cleaning/validation steps
- Not testing edge cases (malformed input, missing fields, encoding issues)

## Phạm vi ví dụ nguồn

- Quiz/exam question parsing
- Form data extraction
- Invoice/receipt processing
- Document structure parsing (headers, sections, tables)
- Any structured text with repeating patterns where cost matters

---

*Nguồn: [ECC](https://github.com/affaan-m/ECC) của Affaan Mustafa - `ECC/skills/regex-vs-llm-structured-text` - giấy phép MIT.*
*Đã sửa để chạy trên Javis OS: `description` được viết lại còn ≤150 ký tự cho router của Javis; `group` được thêm cho trang Kỹ năng của Javis. Đã bổ sung quy trình đối soát dữ liệu CS.*

*Mô tả gốc:*

> Decision framework for parsing structured text (quizzes, forms, invoices, receipts, tables) with a hybrid regex-first pipeline — regex extraction handles 95%+ cheaply, a confidence scorer flags low-confidence items, and an LLM validator fixes only the edge cases. Use when choosing between regex and LLM for text extraction, building a cheap document parser, or optimizing extraction cost and accuracy.
