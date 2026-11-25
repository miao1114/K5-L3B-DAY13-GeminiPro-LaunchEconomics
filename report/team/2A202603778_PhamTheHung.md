# Báo cáo cá nhân — PhamTheHung-2A202603778

## 1. Thông tin thành viên

- Họ tên: Phạm Thế Hùng
- MSSV: `2A202603778`
- Email: `26ai.hungpt5@vinuni.edu.vn`
- Vai trong nhóm: Người gắn nhãn 1 — Lỗi & Telemetry (Máy 3)

## 2. Phần việc phụ trách

- **Nhiệm vụ C (CP3 — `report/team/bang_loi.md`):** Tự gắn bộ nhãn độc lập 1 cho 20 ca lỗi từ đề bài theo 5 loại Google PAIR, gửi đối chiếu đồng thuận với Máy 4 (Người gắn nhãn 2), và xây dựng bảng khắc phục cho 5 ca đại diện đủ 5 loại lỗi.
- **Nhiệm vụ E1 & E2 (CP5 — `report/team/chi_so.md`):** Tính thử 3 chỉ số chính/dùng/an toàn từ `src/logix_requests.csv`, đề xuất thêm 2 chỉ số mới, thiết kế danh sách event có `trace_id` kèm kiểm tra chéo công thức, và hoàn thiện bảng rủi ro kinh tế E2 gắn số liệu `simulated`.

## 3. Đóng góp cụ thể

- **Nhiệm vụ C (`report/team/bang_loi.md`):**
  - Đọc và tự phân loại độc lập 20 ca lỗi (Bộ nhãn 1: `Do người dùng`: 1, 6, 9, 14; `Hệ thống`: 2, 7, 8, 10, 15; `Ngữ cảnh`: 3, 16, 18; `Giới hạn hệ thống`: 4, 11, 13, 19; `Ngầm`: 5, 12, 17, 20), giữ nguyên bộ nhãn độc lập khi đối chiếu với Máy 4 đạt đồng thuận **18/20 = 90%** (vượt ngưỡng 80%) và thống nhất 2 ca lệch (Ca 10 → `Ngữ cảnh`, Ca 20 → `Hệ thống`).
  - Soạn bảng khắc phục cho 5 ca đại diện đủ 5 loại (`Ca 9, 7, 18, 4, 17`), bảo đảm mỗi dòng có cách phát hiện đo được (tên event khớp `chi_so.md`, ngưỡng, tần suất) và 1 vai trò phụ trách cụ thể.
- **Nhiệm vụ E1 & E2 (`report/team/chi_so.md`):**
  - Tính thử 3 chỉ số trên 1.200 yêu cầu của đợt chạy thử (`keep_default_na=False`): Chính **82,83%** (994/1.200), Dùng **27,12%** (48/177), An toàn **4,25%** (51/1.200); đề xuất thêm 2 chỉ số mới (*Tỉ lệ sử dụng trợ lý ở nhóm can thiệp* và *Tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần*).
  - Thiết kế **10 event** bao phủ toàn bộ luồng hoàn phí, mỗi event đều có `trace_id`, kèm mục kiểm tra chéo chứng minh cả 5 chỉ số E1 đều đo được.
  - Hoàn thiện 3 dòng rủi ro kinh tế E2 với số liệu `simulated` đối chiếu từ mô hình chi phí nhóm (`+51,8%` lên 6.787 đ khi làm lại gấp đôi; `11.743 đ = 0,98×` / `12.414 đ = 1,03×` khi xem lại 100%; `+1.185 đ` đến `+2.370 đ/việc` chi phí cố định khi khối lượng giảm một nửa).

## 4. Bằng chứng

- [`report/team/bang_loi.md`](bang_loi.md): Bộ nhãn độc lập 1 (Phạm Thế Hùng), đối chiếu đồng thuận 18/20 (90%) với Máy 4 và bảng khắc phục 5 ca (commit `ed4865c`, PR #2 `5d6393f`).
- [`report/team/chi_so.md`](chi_so.md): Đặc tả 5 chỉ số E1, 10 event có `trace_id`, kiểm tra chéo và bảng 3 rủi ro kinh tế E2 đầy đủ số `simulated`.
- [`TEAM.md`](../../TEAM.md): Cập nhật phần đóng góp và bằng chứng của Máy 3 (`PhamTheHung-2A202603778`).

## 5. Công cụ AI đã dùng

- **Công cụ:** Trợ lý AI trong IDE (Antigravity).
- **Mục đích sử dụng:** Hỗ trợ đọc cấu trúc repo, trích xuất bảng 20 ca lỗi từ `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, chạy script Python kiểm tra lại 3 chỉ số E1 từ `src/logix_requests.csv`, rà soát quy tắc lab (nhãn `simulated`, không dùng từ cấm Gate 2a, 1 vai trò phụ trách) và định dạng bảng Markdown.
- **Tự kiểm tra kết quả:** Tự đọc và tự gắn độc lập toàn bộ 20 ca lỗi trước khi đối chiếu với Máy 4 (không sửa lại bộ nhãn độc lập sau khi so); tự kiểm tra từng tên event giữa `bang_loi.md` và `chi_so.md` cũng như đối chiếu các con số `simulated` ở bảng E2 với `ho_so_launch_v0.md`.

## 6. Tự đánh giá

- **Điểm đạt được:** Hoàn thành trọn vẹn phạm vi Máy 3 đúng tiến độ, chạy độc lập không gây xung đột git; 20 ca lỗi gắn độc lập đạt đồng thuận 90% với Máy 4 và cả 2 file (`bang_loi.md`, `chi_so.md`) vượt qua đầy đủ kiểm tra từ cấm, vai trò phụ trách và nhãn `simulated`.
- **Điểm có thể cải thiện:** Ở lần gắn nhãn độc lập ban đầu còn nhầm 2 ca biên (Ca 10 giữa `Hệ thống`/`Ngữ cảnh` và Ca 20 giữa `Ngầm`/`Hệ thống`); qua đối chiếu đã nắm rõ nguyên tắc phân biệt theo nguyên nhân gốc và mức độ lộ lỗi.
