## Bài học (tự học)
- Khi đọc bằng chứng bàn giao, kiểm riêng thời lượng chat, việc khách phải kể lại, lần liên hệ lại cùng vấn đề và kết quả xử lý thực tế vì các chỉ số này có thể đi khác hướng.
- Khi đánh giá nộp lại sau thư từ chối qua ATS, liệt kê mọi tin cùng chức danh trên trang tuyển dụng, kể cả mã đã gỡ, và đối chiếu ngày sửa các file CV với ngày thư để biết đơn cũ vào mã nào, dùng bản CV nào.
- Khi thư từ chối không nêu vị trí, mã tin hay lý do, chỉ dùng nó ở dạng điều kiện để chọn kênh, không dùng làm căn cứ chấm điểm hay suy ra người lọc đã thấy khoảng trống nào.
- Khi nghiệm thu cần chứng minh workflow chạy nhiều agent, đọc bảng `server/workflow_runs.sqlite3` (steps_json có agent_key, đầu ra từng bước; started_at/finished_at cho cả run) thay vì dựa vào nhãn tự ghi trong file.
- Ở bước nghiên cứu của workflow Career, chỉ ghi vào file research và bàn giao, không tự sửa hồ sơ cơ hội hay dòng tiến độ, vì làm vậy xóa ranh giới giữa hai vai khi nghiệm thu.
- Khi kể lại các run workflow, đọc trường error và output từng bước trong `steps_json`, không suy trạng thái run từ việc bước 1 đã ghi file, vì run có thể lỗi ở bước sau.
