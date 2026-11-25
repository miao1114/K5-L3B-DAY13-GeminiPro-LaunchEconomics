# Gắn nhãn độc lập 20 ca lỗi — Máy 4 (Người gắn nhãn 2)

- **Người thực hiện:** Nguyễn Đức Minh (`2A202603765`) · Vai trò: Người gắn nhãn 2 kiêm Giữ hồ sơ (Máy 4).
- **Mục đích:** Gắn nhãn độc lập 20 ca lỗi từ `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` theo 5 loại Google PAIR (phân loại theo **nguyên nhân gốc**, không theo chỗ cần sửa) để ghép vào `report/team/bang_loi.md` đối chiếu đồng thuận CP3 với Máy 3 (mục tiêu ≥ 80%, kết quả thực tế đạt **18/20 = 90%**, đã thống nhất đủ 20/20 ca).

## Tóm tắt phân bố nhãn Máy 4

| Loại lỗi (Google PAIR) | Các ca | Số ca |
| --- | --- | --: |
| `Do người dùng` | 1, 6, 9, 14 | 4 |
| `Hệ thống` | 2, 7, 8, 15, 20 | 5 |
| `Ngữ cảnh` | 3, 10, 16, 18 | 4 |
| `Giới hạn hệ thống` | 4, 11, 13, 19 | 4 |
| `Ngầm` | 5, 12, 17 | 3 |
| **Tổng cộng** | **1–20** | **20** |

## Bảng gắn nhãn chi tiết 20 ca lỗi

| Ca số | Tóm tắt tình huống | Nhãn Máy 4 | Lý do phân loại (≤ 2 dòng) |
| --: | --- | --- | --- |
| 1 | Khách nhập số tài khoản nhận hoàn tiền thiếu 2 chữ số; trợ lý tạo lệnh hoàn và ngân hàng trả về lỗi. | `Do người dùng` | Nguyên nhân gốc do người dùng nhập thiếu thông tin đầu vào (số tài khoản sai định dạng). |
| 2 | Kiện nội địa 28 kg; trợ lý gọi tool tra bảng giá với tham số hàng thường thay vì hàng nặng, hoàn thiếu 45.000 đ; khách mở lại sau 2 ngày. | `Hệ thống` | Trợ lý truyền sai tham số gọi tool so với chính sách/thiết kế và sai sót đã lộ ra cho khách. |
| 3 | Theo thiết kế, trợ lý hoàn tiền về ví LogiX trong 5 phút; khách chờ tiền về tài khoản ngân hàng và báo "chưa được hoàn". | `Ngữ cảnh` | Trợ lý làm đúng thiết kế, nhưng giả định về kênh nhận tiền không khớp kỳ vọng hoàn cảnh của khách. |
| 4 | Khách yêu cầu hoàn phí chặng hãng nước ngoài giao; LogiX không có dữ liệu chặng này; trợ lý báo không xác định được và chuyển nhân viên. | `Giới hạn hệ thống` | Hệ thống không có dữ liệu chặng vận chuyển ngoài nên không thể tự xử lý. |
| 5 | Kiểm tra mẫu cuối tuần thấy 14 đơn có mã giảm giá bị hoàn theo giá trước giảm (thừa TB 12.000 đ/đơn); không khách báo, không cảnh báo kích. | `Ngầm` | Hoàn sai tiền nhưng cả khách lẫn hệ thống đều không nhận ra, chỉ phát hiện qua kiểm tra mẫu. |
| 6 | Khách chọn mục "Hoàn phí giao trễ" nhưng mô tả hàng bị vỡ; trợ lý xử lý theo luồng giao trễ và từ chối vì đơn giao đúng hạn. | `Do người dùng` | Gốc lỗi là khách chọn sai danh mục đầu vào; việc trợ lý chưa phát hiện mâu thuẫn thuộc hướng khắc phục. |
| 7 | API sổ cái trả lỗi 503 ở bước ghi hoàn tiền; trợ lý thử lại 3 lần rồi vẫn báo khách "đã hoàn tiền thành công". | `Hệ thống` | Trợ lý vi phạm thiết kế nghiêm trọng khi báo hoàn thành công dù sổ cái chưa trả `ok`. |
| 8 | Trợ lý dẫn "Điều 7.2 chính sách hoàn phí" (không tồn tại trong bản hiện hành) làm căn cứ; số tiền hoàn vẫn đúng. | `Hệ thống` | Trợ lý bịa trích dẫn sai chính sách và lỗi hiển thị trực tiếp trong câu trả lời (không phải lỗi ngầm). |
| 9 | Khách nhập mã đơn sàn TMĐT thay vì mã vận đơn; trợ lý báo "mã không hợp lệ" rồi dừng, không gợi ý. | `Do người dùng` | Nguyên nhân gốc do khách nhập sai loại mã đầu vào; việc bổ sung gợi ý nằm ở bước khắc phục. |
| 10 | Đơn giao trễ do bão; trợ lý từ chối hoàn theo điều khoản bất khả kháng (đúng chính sách), nhưng khách thấy vô lý vì app vẫn hiện "cam kết giao 24 giờ". | `Ngữ cảnh` | Trợ lý làm đúng chính sách nhưng kết quả xung đột với ngữ cảnh thông tin ứng dụng hiển thị cho khách. |
| 11 | Khách gửi tin nhắn thoại 40 giây; trợ lý không xử lý được âm thanh, trả lời "vui lòng nhập bằng chữ". | `Giới hạn hệ thống` | Dạng đầu vào âm thanh vượt quá năng lực xử lý của hệ thống. |
| 12 | Tool tra đơn depot D05 trả thiếu 1 trường; trợ lý vẫn ra đáp án đúng sau nhiều lần gọi, khiến tiền token D05 gấp 3 lần suốt 3 tuần không ai thấy. | `Ngầm` | Sai sót về chi phí diễn ra âm thầm 3 tuần mà không có cảnh báo hay khiếu nại từ khách và hệ thống. |
| 13 | Khách hỏi hoàn phí bảo hiểm hàng hoá của đối tác (ngoài phạm vi); trợ lý trả lời chung chung về phí vận chuyển, không nói rõ không xử lý được. | `Giới hạn hệ thống` | Gốc lỗi là yêu cầu nằm ngoài phạm vi trợ lý, dù cách phản hồi giới hạn vẫn cần cải thiện. |
| 14 | Khách bấm nhầm "Xác nhận đã nhận tiền" khi chưa nhận nên yêu cầu bị đóng. | `Do người dùng` | Nguyên nhân gốc xuất phát trực tiếp từ thao tác bấm nhầm của người dùng. |
| 15 | Đơn trễ 26 giờ (chính sách 24–48 giờ hoàn 50%), trợ lý tính hoàn 100%; nhân viên xem lại bắt được trước khi gửi. | `Hệ thống` | Trợ lý tính sai chính sách và lỗi đã bị nhân viên phát hiện khi xem lại (không phải lỗi ngầm). |
| 16 | Theo thiết kế "gửi ngay khi xong", trợ lý gửi thông báo hoàn tiền qua Zalo lúc 2:14 sáng; khách phản ánh bị làm phiền. | `Ngữ cảnh` | Trợ lý chạy đúng thiết kế nhưng giả định gửi tức thời không phù hợp ngữ cảnh sinh hoạt của khách. |
| 17 | Bảng giá đổi từ 01/11 nhưng trợ lý vẫn dùng bản cũ trong bộ nhớ đệm cho đơn < 2 kg; lệch 1.000–2.000 đ/đơn trên 212 đơn suốt 9 ngày, không ai mở lại. | `Ngầm` | Hoàn sai 212 đơn suốt 9 ngày mà cả khách và hệ thống không ai phát hiện hay mở lại yêu cầu. |
| 18 | Trợ lý tính đúng (phí 30.000 đ, hoàn 50%) nhưng tin nhắn chỉ ghi "Đã hoàn 15.000 đ" không kèm cách tính; khách tưởng hoàn thiếu và mở lại. | `Ngữ cảnh` | Số tiền đúng chính sách nhưng giả định "khách tự hiểu công thức tính" không khớp hoàn cảnh thực tế. |
| 19 | Khách yêu cầu hoàn phí cho đơn từ 14 tháng trước; trợ lý chỉ truy cập được dữ liệu 12 tháng, nên báo rõ và chuyển nhân viên kèm tóm tắt. | `Giới hạn hệ thống` | Hệ thống không có quyền/khả năng truy cập dữ liệu cũ quá 12 tháng. |
| 20 | Khách gửi lại yêu cầu sau 10 phút vì chưa thấy phản hồi; trợ lý hoàn hai lần cho cùng một đơn do lệnh thứ hai không có khoá chống trùng. | `Hệ thống` | Lỗi thiết kế/hệ thống thiếu khoá chống trùng (`idempotency_key`) dẫn tới hoàn tiền trùng lặp. |

## Quy tắc phân biệt nhanh khi đối chiếu CP3 với Máy 3

- **Ca 6, 9 → `Do người dùng`:** bám nguyên nhân gốc (khách chọn sai mục/nhập sai mã), không gán `Hệ thống` vì thiếu gợi ý.
- **Ca 13 → `Giới hạn hệ thống`:** ngoài phạm vi là giới hạn, bất kể trợ lý xử lý giới hạn đó tốt hay kém.
- **Ca 8, 15 → `Hệ thống`:** lỗi đã lộ ra (trích dẫn hiển thị, nhân viên phát hiện), không gán `Ngầm`.
- **Ca 18 → `Ngữ cảnh`:** kết quả số tiền đúng chính sách, chỉ thiếu diễn giải gây lệch kỳ vọng khách.
- **Ca 12 → `Ngầm`:** lỗi có thể là sai về chi phí (token gấp 3 lần trong 3 tuần không ai biết), không chỉ sai đáp án.

---

## Nhật ký tiến độ & Kết quả tự kiểm tra (Verification Log — Máy 4)

### 1. Tóm tắt các file đã tạo / cập nhật (Zero-Conflict Scope)

| STT | Đường dẫn file | Trạng thái | Nội dung chính |
| --: | --- | --- | --- |
| 1 | `TEAM.md` | Đã cập nhật | Giữ nguyên thông tin 4 thành viên nhóm GeminiPro (L3B), bổ sung URL repo, phân công phạm vi file 4 máy và mục đóng góp cá nhân. |
| 2 | `docs/notes/nhan_loi_may4.md` | Tạo mới | Gắn nhãn độc lập 20/20 ca lỗi theo 5 nhóm Google PAIR (nguyên nhân gốc) kèm lý do ≤ 2 dòng và quy tắc đối chiếu CP3. |
| 3 | `report/team/ho_so_launch_v0.md` | Đã cập nhật | Hoàn thiện hồ sơ launch v0 dài 1 trang: đủ 7 mục bắt buộc, trạng thái chuẩn, 1 vai trò phụ trách/mục và đề xuất `Go có điều kiện` (4 điều kiện). |
| 4 | `report/team/group_report.md` | Đã cập nhật | Tổng hợp quy trình A–E, phân công 4 máy, kết quả chính (`simulated` đúng chỗ), đề xuất Gate 2a và hạn chế/hướng cải thiện. |
| 5 | `report/team/2A202603765_NguyenDucMinh.md` | Đã cập nhật | Hoàn thiện báo cáo cá nhân Máy 4 (`Nguyễn Đức Minh — 2A202603765`); giữ nguyên file mẫu `report/team/MSSV_HoTen.md`. |

- **Kiểm tra zero-conflict (`git status --short`):** Không chỉnh sửa `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/pilot_plan.yaml`, `report/team/chi_so.md`, `report/team/bang_loi.md`, `report/team/MSSV_HoTen.md`.

### 2. Kết quả 4 bước kiểm tra tự động

1. **Quy tắc 5 (cấm từ vi phạm phạm vi Gate 2a, không phân biệt hoa thường) trên cả 5 file:** **ĐẠT (0 dòng khớp)**.
2. **Độ dài & số liệu trong `report/team/ho_so_launch_v0.md`:** **ĐẠT** — đủ 7/7 mục bảng chính (206–284 ký tự/ô, ≤ 3 dòng hiển thị) và 4 điều kiện đề xuất, mọi ô đều có số liệu cụ thể; 0 lần dùng cụm `"đã nâng"`.
3. **Nhãn `simulated`:** **ĐẠT** — toàn bộ con số tính từ hai cột `_simulated` (Mục 1, 2, 3, 7 và điều kiện 4 trong `ho_so_launch_v0.md`, cùng mục Kết quả trong `group_report.md`) đều có nhãn `simulated` và cột Trạng thái ghi `Giả lập`.
4. **Vai trò phụ trách:** **ĐẠT** — mỗi mục chỉ gán 1 vai trò cụ thể có quyền quyết định (`PM trợ lý hoàn phí`, `Trưởng nhóm CSKH`, `Kỹ sư trưởng agent`, `Giám đốc vận hành LogiX-VN`), không ghi `"cả đội"` hay gán chung chung cho `"nhóm"`.
