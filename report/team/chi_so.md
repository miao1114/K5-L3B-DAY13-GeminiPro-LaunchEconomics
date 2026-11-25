# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là **82,83%** (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | Chỉ số trong đợt chạy thử là **27,12%** (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là **4,25%** (51/1.200) |
| Dùng | Nhóm tự đề xuất: Tỉ lệ sử dụng trợ lý ở nhóm can thiệp | Số yêu cầu nhóm can thiệp có phát sinh `agent_suggestion_shown` chia tổng số yêu cầu của nhóm can thiệp | Không cần tính |
| An toàn | Nhóm tự đề xuất: Tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần | Số đơn lệch số tiền hoàn trong `audit_sample_checked` chia tổng số đơn được kiểm tra mẫu (bắt lỗi ngầm) | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | `request_id`, `loai`, `so_tien_vnd`, `arm` (`treatment`/`control`), `trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `agent_run_completed` | Agent | `request_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện CSKH | `request_id`, `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý của trợ lý hiện ra |
| `staff_review_decision` | Nhân viên CSKH | `request_id`, `staff_id`, `quyet_dinh_xem_lai` (`giu`/`sua`/`bo`), `phut_xem_lai`, `trace_id` | Khi nhân viên bấm giữ, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên CSKH | `request_id`, `staff_id`, `phut_lam_lai`, `ly_do`, `trace_id` | Khi nhân viên làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | `request_id`, `idempotency_key`, `so_tien`, `ket_qua`, `trace_id` | Khi ghi nhận lệnh hoàn tiền |
| `handoff_to_staff` | Agent | `request_id`, `reason`, `tom_tat`, `trace_id` | Khi chuyển yêu cầu sang nhân viên |
| `ticket_closed` | Hệ thống ticket | `request_id`, `closed_at`, `trace_id` | Khi đóng yêu cầu |
| `ticket_reopened` | Khách hàng / CSKH | `request_id`, `reopened_at`, `reason`, `trace_id` | Khi yêu cầu được mở lại |
| `audit_sample_checked` | Kế toán | `request_id`, `so_tien_da_hoan`, `so_tien_dung`, `le_ch_tien`, `trace_id` | Hằng tuần khi kiểm tra mẫu |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chính (% đóng trong 24h và không mở lại trong 7 ngày):** tính từ `refund_request_created` (mẫu số, mốc tạo), `ticket_closed` (kiểm tra `closed_at - created_at <= 24h`), và `ticket_reopened` (kiểm tra không có event mở lại trong 7 ngày).
- **Dùng (Tỉ lệ bỏ qua gợi ý):** tính từ `staff_review_decision` (tử số: `quyet_dinh_xem_lai` là `sua` hoặc `bo`; mẫu số: tổng số event `staff_review_decision`).
- **An toàn (Tỉ lệ lỗi lọt đến khách):** tính từ `ticket_reopened` trong 7 ngày (tử số) và `refund_request_created` (mẫu số).
- **Dùng — tự đề xuất (Tỉ lệ sử dụng trợ lý ở nhóm can thiệp):** tính từ `agent_suggestion_shown` (tử số, lọc `request_id` thuộc nhóm can thiệp) và `refund_request_created` (mẫu số, lọc `arm == treatment`).
- **An toàn — tự đề xuất (Tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu):** tính từ `audit_sample_checked` (tử số: `le_ch_tien != 0`; mẫu số: tổng số bản ghi `audit_sample_checked`).

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Tăng **+51,8%**, lên **6.787 đ/việc** (`simulated`, so với mức gốc 4.472 đ) | Tỉ lệ làm lại theo tuần > 7% (đợt chạy thử: 4,9% trong phạm vi) hoặc số ca `staff_rework_completed` tăng > 1,5× tuần gốc | Thu hẹp phạm vi về `noi_dia`, rà soát 20 trace có `staff_rework_completed` gần nhất | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | **11.743 đ = 0,98×** mức 12.000 đ (với 9 phút làm lại) hoặc **12.414 đ = 1,03×** nếu làm lại 15,3 phút như dữ liệu (`simulated`) | Tỉ lệ yêu cầu có `staff_review_decision` vẫn > 50% ở cuối bước rollout 0,25 | Áp dụng giảm tỉ lệ xem lại theo bậc khi tỉ lệ sửa + bỏ < 15% trong 1 tuần | Trưởng nhóm CSKH |
| Khối lượng yêu cầu thấp hơn dự kiến | Chi phí cố định 40 triệu đ/tháng: **+1.185 đ/việc** (lên 4.599 đ = 0,38×) ở 45.000 yc/tháng; tăng thành **+2.370 đ/việc** (lên 5.784 đ = 0,48×) nếu khối lượng giảm một nửa (`simulated`) | Số việc thành công theo tuần < 50% kế hoạch quy mô đầy đủ | Tạm dừng mở rộng pilot và đàm phán lại hợp đồng chi phí cố định hàng tháng | PM trợ lý hoàn phí |
