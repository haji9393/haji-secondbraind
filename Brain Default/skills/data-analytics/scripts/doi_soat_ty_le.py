"""Tính tỷ lệ tháng từ CSV tổng hợp, có thể xuất Excel với công thức truy được."""
import argparse
import csv
import json
import re
from collections import defaultdict
from pathlib import Path

FIELDS = ("period", "segment", "numerator", "denominator")


def read_rows(source):
    rows = []
    seen = set()
    with source.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, strict=True)
        if tuple(reader.fieldnames or ()) != FIELDS:
            raise ValueError(f"Header phải là {','.join(FIELDS)}")
        for row in reader:
            line = reader.line_num
            if None in row or any(value is None for value in row.values()):
                raise ValueError(f"Dòng {line}: sai số cột")
            period, segment, numerator, denominator = (row[key].strip() for key in FIELDS)
            if not re.fullmatch(r"[0-9]{4}-(0[1-9]|1[0-2])", period) or not segment:
                raise ValueError(f"Dòng {line}: period cần YYYY-MM và segment cần có giá trị")
            key = (period, segment.casefold())
            if key in seen:
                raise ValueError(f"Dòng {line}: trùng kỳ và phân khúc ({period}, {segment})")
            if not all(re.fullmatch(r"[0-9]+", value) for value in (numerator, denominator)):
                raise ValueError(f"Dòng {line}: tử và mẫu phải là số nguyên không âm")
            n, d = int(numerator), int(denominator)
            if n > d:
                raise ValueError(f"Dòng {line}: tử vượt mẫu")
            seen.add(key)
            rows.append((period, segment, n, d, line))
    if not rows:
        raise ValueError("CSV chưa có dữ liệu")
    return rows


def summarize(rows):
    totals = defaultdict(lambda: [0, 0, 0])
    for period, _, numerator, denominator, _ in rows:
        totals[period][0] += numerator
        totals[period][1] += denominator
        totals[period][2] += 1
    return [
        {
            "period": period,
            "numerator": n,
            "denominator": d,
            "input_rows": count,
            "rate": n / d if d else None,
        }
        for period, (n, d, count) in sorted(totals.items())
    ]


def write_excel(output, rows, summary):
    try:
        from xlsxwriter import Workbook
    except ImportError as exc:
        raise ValueError("Cần XlsxWriter để xuất .xlsx. Có thể chạy Python riêng khi bỏ --xlsx.") from exc

    # Ghi kiểu chuỗi rõ ràng để kỳ, phân khúc và nhãn đầu vào giữ nguyên.
    with output.open("xb") as handle, Workbook(handle) as book:
        raw = book.add_worksheet("Data")
        result = book.add_worksheet("Summary")
        percent = book.add_format({"num_format": "0.00%"})
        raw.write_row(0, 0, [*FIELDS, "csv_line"])
        result.write_row(0, 0, ["period", "numerator", "denominator", "input_rows", "rate", "status"])
        for i, (period, segment, n, d, line) in enumerate(rows, start=1):
            raw.write_string(i, 0, period)
            raw.write_string(i, 1, segment)
            raw.write_row(i, 2, [n, d, line])

        last_row = len(rows) + 1
        period_range = f"Data!$A$2:$A${last_row}"
        n_range = f"Data!$C$2:$C${last_row}"
        d_range = f"Data!$D$2:$D${last_row}"
        for i, data in enumerate(summary, start=1):
            row = i + 1
            rate = data["rate"]
            status = "Mẫu số bằng 0" if rate is None else "Đã tính"
            result.write_string(i, 0, data["period"])
            result.write_formula(i, 1, f"=SUMIFS({n_range},{period_range},A{row})", None, data["numerator"])
            result.write_formula(i, 2, f"=SUMIFS({d_range},{period_range},A{row})", None, data["denominator"])
            result.write_formula(i, 3, f"=COUNTIF({period_range},A{row})", None, data["input_rows"])
            result.write_formula(i, 4, f'=IF(OR(D{row}=0,C{row}=0),"",B{row}/C{row})', percent, "" if rate is None else rate)
            result.write_formula(i, 5, f'=IF(D{row}=0,"Thiếu dữ liệu",IF(C{row}=0,"Mẫu số bằng 0","Đã tính"))', None, status)

        for sheet in (raw, result):
            sheet.freeze_panes(1, 0)
            sheet.set_column("A:F", 17)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", type=Path)
    parser.add_argument("--xlsx", type=Path, help="Tạo workbook mới tại đường dẫn .xlsx")
    args = parser.parse_args()
    try:
        rows = read_rows(args.csv_file)
        summary = summarize(rows)
        if args.xlsx:
            if args.xlsx.suffix.lower() != ".xlsx":
                raise ValueError("Đường dẫn đầu ra cần đuôi .xlsx")
            write_excel(args.xlsx, rows, summary)
    except (ValueError, OSError, csv.Error) as exc:
        parser.exit(1, f"{exc}\n")
    print(json.dumps({"source": str(args.csv_file), "input_rows": len(rows), "periods": summary}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
