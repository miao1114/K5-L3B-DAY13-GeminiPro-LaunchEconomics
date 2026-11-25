# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Phạm Thế Hùng · Người gắn nhãn 2: Nguyễn Đức Minh 

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Hệ thống | Ngữ cảnh | Không | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Ngầm | Hệ thống | Không | Hệ thống |

**Tỉ lệ đồng thuận:** 18 / 20 = **90%** (vượt ngưỡng 80%, không cần viết lại định nghĩa; đã thống nhất đủ 20/20 ca theo nguyên nhân gốc).

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- **Ca 10 → `Ngữ cảnh`:** Trợ lý từ chối hoàn theo điều khoản bất khả kháng là đúng chính sách và thiết kế, chỉ xung đột với thông tin "cam kết giao 24 giờ" hiển thị trên ứng dụng khiến khách thấy vô lý nên không phải lỗi `Hệ thống`.
- **Ca 20 → `Hệ thống`:** Trợ lý hoàn tiền hai lần do thiếu khoá chống trùng (`idempotency_key`) là vi phạm thiết kế hệ thống và thể hiện trực tiếp trên lệnh hoàn tiền, không phải lỗi `Ngầm`.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `agent_run_completed` kết hợp kiểm tra định dạng mã đầu vào (`input_validation_failed`); cảnh báo khi vượt ngưỡng > 2% số yêu cầu/ngày | Tự động nhận diện mã đơn sàn TMĐT và tra sang mã vận đơn; nếu không tra được thì hiển thị hướng dẫn kèm ảnh minh họa | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ giữa tin nhắn báo "đã hoàn" (`agent_run_completed`) và event `refund_ledger_write` có `ket_qua == 'ok'` theo `trace_id`; ngưỡng cảnh báo = 0 ca lệch | Chỉ cho phép gửi thông báo "đã hoàn tiền thành công" khi `refund_ledger_write` trả về `ok`; nếu API trả 503 sau 3 lần thử thì báo "đang xử lý" và phát `handoff_to_staff` | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Theo dõi hằng tuần tỉ lệ `ticket_reopened` có lý do thắc mắc số tiền dù `audit_sample_checked` xác nhận tính đúng; ngưỡng cảnh báo > 1% số đơn/tuần | Cập nhật mẫu tin nhắn phản hồi luôn hiển thị rõ công thức tính tiền hoàn (ví dụ: `30.000 đ × 50% = 15.000 đ`) | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason == 'thieu_du_lieu'`, thống kê hằng ngày theo cột `loai`; cảnh báo khi tỉ lệ chuyển tăng > 10% | Giữ cơ chế chuyển nhân viên kèm tóm tắt ngữ cảnh; loại nhóm yêu cầu ngoài dữ liệu (`quoc_te`) khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Event `audit_sample_checked` kiểm tra mẫu ngẫu nhiên 100 đơn/tuần so với bảng giá hiện hành; ngưỡng cảnh báo ≥ 1% đơn lệch | Xóa bộ nhớ đệm ngay khi cập nhật bảng giá mới và ghi kèm `price_table_version` vào thuộc tính trace của `agent_run_completed` | Kế toán trưởng |
