# Tài chính và kế toán quản trị

## Khi nào dùng

Dùng khi cần chọn phương án đầu tư hoặc định giá, kiểm mô hình, rà dòng tiền, đối soát sổ với chứng từ, hoặc giải thích chênh lệch ngân sách. Dùng thêm `business-strategy-presentation` khi trình lãnh đạo và `data-analytics` khi cần truy nguyên dữ liệu đầu vào.

## Chuẩn bị

Chốt câu cần quyết, đối tượng hưởng lợi và chịu chi phí, kỳ, tiền tệ, đơn vị, cơ sở trước/sau thuế và phạm vi pháp nhân. Mở bản mới nhất của mô hình, quyết định dự án và chứng từ liên quan. Ghi nguồn từng đầu vào, ngày, bảng hoặc ô, loại số thực tế/dự báo/mục tiêu/giả định, và người xác nhận. Khi nguồn vênh, giữ cả hai con số, tính tác động và nêu điều kiện phân xử.

## Quy trình thẩm định

1. Vẽ mô hình kinh doanh bằng các biến có thể kiểm. Nối số lượng, giá và doanh thu với chi phí biến đổi, chi phí cố định, chi phí thời gian của Haji và vốn ban đầu. Tách chi phí cơ hội khỏi dòng tiền chi thực tế. Kiểm nhu cầu, năng lực phục vụ và tính khả thi của giá theo nguồn thị trường phù hợp trước khi coi dự báo là cơ sở quyết định.
2. Dựng lợi nhuận và dòng tiền theo kỳ. Đặt cọc, thời hạn thu/chi, công nợ, vốn lưu động, đầu tư và tài trợ vào đúng kỳ tiền chuyển. Nếu có nhiều bên, lập riêng phần chủ tài sản và đơn vị vận hành, nhất quán về tiền thuê và giao dịch nội bộ. Tiền cuối kỳ = tiền đầu kỳ + tiền thu - tiền chi. Nêu kỳ thiếu tiền lớn nhất và vốn cần bổ sung.
3. Tính lãi đóng góp mỗi đơn vị = doanh thu thuần mỗi đơn vị - chi phí biến đổi mỗi đơn vị. Điểm hòa vốn theo số lượng = chi phí cố định / lãi đóng góp mỗi đơn vị, khi phần đóng góp dương và giả định giá/cơ cấu bán phù hợp. Nếu dùng hoàn vốn, tìm kỳ đầu tiên dòng tiền cộng dồn bù vốn đã bỏ và ghi rõ có chiết khấu hay không. Nếu quyết định cần NPV, chiết khấu dòng tiền theo suất và nhịp cùng kỳ, ghi cơ sở suất chiết khấu và phạm vi dòng tiền.
4. Chạy kịch bản cơ sở, bất lợi và thuận lợi. Đổi biến theo quan hệ thực tế, rồi kiểm riêng những biến có thể đảo quyết định. Nêu điều kiện đạt hòa vốn, điều kiện dừng và dữ kiện cần kiểm tiếp. Với Ruby Bãi Kem, lấy chính sách thuê, giá phòng, công suất và chi phí vận hành từ phiên bản đang được dùng, rồi tách góc nhìn chủ nhà khỏi công ty vận hành.
5. Bàn giao kết luận, bảng giả định, các kịch bản, mâu thuẫn còn mở và đối chiếu từng số trọng yếu trên mô hình, deck và đề xuất.

## Quy trình kế toán quản trị

1. Gom chứng từ, sao kê, sổ chi tiết, sổ cái hoặc bảng tổng hợp đúng kỳ. Đối chiếu số dư đầu/cuối kỳ, khóa giao dịch, ngày, tiền tệ và số tiền theo từng nguồn.
2. Phân loại chênh lệch do thời điểm, do cần điều chỉnh hoặc do chưa đủ hồ sơ. Giữ ID gốc, chênh lệch, giải thích, tuổi khoản đang treo, người xử lý và hạn. Cộng lại cầu nối từ số nguồn A tới số nguồn B.
3. Với bút toán nháp, ghi chứng từ, kỳ, tài khoản Nợ/Có theo hệ thống áp dụng, lý do và số tiền. Kiểm tổng Nợ = tổng Có và bàn giao người có thẩm quyền duyệt hạch toán. Xác minh quy định Việt Nam theo loại hình, kỳ và văn bản chính thức khi công việc liên quan đến thuế hoặc báo cáo pháp định.
4. So thực tế với ngân sách, dự báo hoặc kỳ gốc cùng phạm vi. Chênh lệch tuyệt đối = thực tế - mốc so. Chỉ tính phần trăm khi mẫu số có ý nghĩa. Khi tách theo giá, lượng hoặc cơ cấu, công bố phương pháp, xử lý phần giao nhau và kiểm tổng các nguyên nhân khớp chênh lệch. Phân biệt nguyên nhân đã kiểm với lời giải thích dự kiến.
5. Nếu có đủ số liệu để lập báo cáo, đối chiếu kết quả kinh doanh, bảng cân đối và lưu chuyển tiền tệ. Kiểm tài sản = nợ phải trả + vốn chủ và đối chiếu tiền cuối kỳ giữa hai báo cáo. Ghi cơ sở báo cáo và phần chưa đối soát.

## Kiểm chứng

Tính bằng công thức hoặc mã, ghi đơn vị và kiểm độc lập những chỉ số làm thay đổi đề xuất. Dùng bộ dữ liệu minh họa để thử số âm, mẫu số 0, kỳ thiếu dữ liệu và thay đổi dấu. Trước khi trình, truy ngược mỗi con số trọng yếu về nguồn.

Tham khảo phương pháp [bộ tài chính-kế toán của Anthropic](https://github.com/anthropics/knowledge-work-plugins/blob/main/finance/README.md) và cách trình bày dòng tiền theo [IAS 7 của IFRS Foundation](https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows.html/).
