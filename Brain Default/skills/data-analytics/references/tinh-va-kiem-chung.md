# Tính và kiểm chứng bằng Python, Excel và Google Sheets

Chọn công cụ theo dữ liệu và người sẽ sử dụng kết quả. Nếu kết luận có thể làm đổi quyết định, dùng một cách tính độc lập, một mẫu có thể tính tay hoặc đối chiếu với tổng kiểm có sẵn. Hai bảng cùng tham chiếu một ô kết quả chỉ kiểm được việc truyền số.

## Python

- Dùng `csv` hoặc thư viện bảng phù hợp để đọc, ép kiểu và giữ ID hoặc dòng nguồn. Trước khi ghép, xác định quan hệ một-một, một-nhiều hay nhiều-nhiều. So số hàng và tổng có thể đối soát trước và sau khi ghép.
- Chạy theo thứ tự đọc dữ liệu, kiểm kiểu và khóa, lọc, tổng hợp, tính chỉ số, kiểm tra rồi xuất. Giữ mã, lệnh chạy, phiên bản đầu vào, kết quả và danh sách lỗi. Mở lại vài bản ghi đủ điều kiện và vài bản ghi bị loại để kiểm phương pháp.
- Dùng [script đối soát tỷ lệ](skills/data-analytics/scripts/doi_soat_ty_le.py) làm mẫu thực thi khi mỗi dòng là tổng đếm của một phân khúc và một kỳ, các phân khúc trong kỳ không chồng nhau và tử số là tập con của mẫu số. Dữ liệu cấp sự kiện hoặc phân khúc giao nhau cần dựng mẫu số riêng trước khi dùng script này.

Ví dụ CSV có header `period,segment,numerator,denominator`.

```csv
period,segment,numerator,denominator
2026-10,A,18,60
2026-10,B,2,40
2026-11,A,0,20
2026-12,A,0,0
```

Chạy từ gốc brain với đầu vào và đầu ra thực tế. Tạo thư mục đích trước.

```sh
python3 skills/data-analytics/scripts/doi_soat_ty_le.py ./du-lieu.csv
python3 skills/data-analytics/scripts/doi_soat_ty_le.py ./du-lieu.csv --xlsx ./doi-soat.xlsx
```

Lệnh thứ nhất dùng thư viện chuẩn. Lệnh thứ hai cần `XlsxWriter` trong môi trường Python dùng cho công việc. Script báo dòng lỗi và dừng với khóa trùng, trường sai kiểu, tử vượt mẫu hoặc lỗi cấu trúc. Tỷ lệ của kỳ có mẫu số 0 trả `null`. Python xuất cả tử, mẫu và số dòng theo kỳ để so với bảng tính.

## Excel và Google Sheets

Giữ dữ liệu gốc hoặc bản trích có ID trong tab `Data`, để tham số ở ô riêng và kết quả trong `Summary`. Dùng `SUMIFS` và `COUNTIFS` để tổng hợp theo điều kiện. Khi nối bảng bằng hàm tra cứu, kiểm khóa duy nhất và đếm khóa không khớp trước. Với workbook nhiều bước, tách các phép tính trung gian, giữ đơn vị và ghi phạm vi dữ liệu để người khác lần được.

[Mở workbook ví dụ](skills/data-analytics/references/mau-doi-soat-ty-le.xlsx). Workbook dùng vùng cố định đúng bốn dòng mẫu, để dễ đọc công thức. Khi thay dữ liệu bằng vùng lớn hơn, tái tạo workbook bằng script hoặc mở rộng đồng bộ phạm vi. Các ô cột A ở hai tab dùng văn bản dạng `YYYY-MM`. Nếu công cụ nhập tháng thành ngày, chuẩn hóa hai tab về cùng kiểu trước khi đối chiếu.

| Ô trong Summary | Công thức ví dụ | Ý nghĩa |
|---|---|---|
| B2 | `=SUMIFS(Data!$C$2:$C$5,Data!$A$2:$A$5,A2)` | Cộng tử số của các dòng đúng kỳ. |
| C2 | `=SUMIFS(Data!$D$2:$D$5,Data!$A$2:$A$5,A2)` | Cộng mẫu số của các dòng đúng kỳ. |
| D2 | `=COUNTIF(Data!$A$2:$A$5,A2)` | Đếm dòng nguồn của kỳ. |
| E2 | `=IF(OR(D2=0,C2=0),"",B2/C2)` | Tính tỷ lệ từ tổng tử/tổng mẫu nếu xác định được. |
| F2 | `=IF(D2=0,"Thiếu dữ liệu",IF(C2=0,"Mẫu số bằng 0","Đã tính"))` | Giải thích khi tỷ lệ trống, giữ phân biệt với tỷ lệ bằng 0. |

Với Excel, mở workbook ở chế độ tính lại và kiểm cả công thức lẫn giá trị. Theo vết các ô tham chiếu và kiểm một dòng tính tay. Với Google Sheets, dùng công thức trên trong tài liệu có quyền phù hợp hoặc nhập workbook. Đọc lại công thức và giá trị sau khi Sheets tính, kiểm locale, dấu phân cách, kiểu ngày và phạm vi. Khi thiếu kết nối Sheets, bàn giao .xlsx cùng công thức và ghi công cụ đã thực sự chạy. File CSV chỉ mang dữ liệu dạng bảng.

Đối chiếu ví dụ tháng 10: `(18 + 2) / (60 + 40) = 20 / 100 = 20%`. Hai phân khúc lần lượt là 30% và 5%. Lấy trung bình đều 17,5% sẽ trả lời một câu hỏi khác vì hai mẫu số khác nhau. Tháng 11 là 0%, tháng 12 có mẫu số 0. Nếu thêm kỳ 2027-01 vào Summary, công thức báo thiếu dữ liệu.

## Khi kết quả lệch

1. So lại kỳ, bộ lọc, cấp bản ghi, múi giờ, kiểu dữ liệu và quy tắc làm tròn.
2. So tử, mẫu, số bản ghi và tổng sau từng bước. Tìm bước đầu tiên hai cách tính lệch để quay lại dòng hoặc ô gốc. Kiểm điều kiện lọc, khóa trùng, nhóm chồng nhau, dòng bị mất và phạm vi công thức.
3. Sửa từ bước gây sai và chạy lại các chỉ số phụ thuộc. Ghi nguyên nhân, kết quả trước/sau và ảnh hưởng tới đề xuất. Khi còn bất đồng, ghi số nào chưa đối soát và giới hạn sử dụng.

Tham khảo [SUMIFS trong Excel](https://support.microsoft.com/en-us/excel/functions/sumifs-function), [kiểm công thức Excel](https://support.microsoft.com/en-us/excel/how-to-avoid-broken-formulas-in-excel) và [SUMIFS trong Google Sheets](https://support.google.com/docs/answer/3238496?hl=en).
