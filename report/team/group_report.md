# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: **GeminiPro**
- Lớp: **L3B**
- Repo nhóm: `K5-L3B-DAY13-GeminiPro-LaunchEconomics`
- Thành viên & phân công 4 máy: xem chi tiết tại [`TEAM.md`](../../TEAM.md)
  - **Máy 1 (Nguyễn Văn Hiếu — 2A202603746):** Người viết code (`src/lab13.py`).
  - **Máy 2 (Nguyễn Văn Cường — 2A202603750):** Người kiểm số (`report/team/bang_chi_phi.md`, `report/team/pilot_plan.yaml`).
  - **Máy 3 (Phạm Thế Hùng — 2A202603778):** Người gắn nhãn 1 (`report/team/bang_loi.md`, `report/team/chi_so.md`).
  - **Máy 4 (Nguyễn Đức Minh — 2A202603765):** Người gắn nhãn 2 kiêm Giữ hồ sơ (`TEAM.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `docs/notes/nhan_loi_may4.md`).

## 2. Mục tiêu và cách tiếp cận

Mục tiêu của Lab 13 là xây dựng bộ hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN để bảo vệ trước hội đồng **Gate 2a** (duyệt kế hoạch pilot, không duyệt triển khai đại trà). Nhóm phân tách 4 máy chạy song song theo cơ chế zero-conflict trên từng file, đối chiếu đáp án từng checkpoint (CP1–CP5) và gắn nhãn `simulated` bắt buộc cho mọi kết quả xuất phát từ hai cột `_simulated`.

## 3. Giải pháp (Tóm tắt nhiệm vụ A–E)

- **Nhiệm vụ A · Mô hình chi phí ([`src/lab13.py`](../../src/lab13.py), [`bang_chi_phi.md`](bang_chi_phi.md)):** Vượt qua 3 phép thử A1 (`1,20 · 1,25 · 1,25`), xây dựng hàm `mo_hinh()` tính đầy đủ token + tool (kể cả lần lỗi) cộng chi phí xem lại/làm lại trên 1.200 yêu cầu (1.624 lần chạy), tách theo 4 loại yêu cầu và cộng chi phí cố định 40 triệu đ/tháng.
- **Nhiệm vụ B · Độ nhạy & kịch bản giới hạn ([`bang_chi_phi.md`](bang_chi_phi.md)):** Chạy 9 kịch bản đơn + 1 kịch bản cặp; xếp hạng yếu tố ảnh hưởng mạnh nhất; tính chi phí cả hệ thống ở giới hạn 1–3 lần chạy (B3) và kiểm tra kịch bản xem lại 100% ở tuần đầu (B4).
- **Nhiệm vụ C · Phân loại lỗi & khắc phục ([`bang_loi.md`](bang_loi.md), [`docs/notes/nhan_loi_may4.md`](../../docs/notes/nhan_loi_may4.md)):** Máy 3 và Máy 4 gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR (bám nguyên nhân gốc), đối chiếu đạt đồng thuận **18/20 (90%)** (vượt ngưỡng 80%, thống nhất 2 ca lệch là Ca 10 → `Ngữ cảnh`, Ca 20 → `Hệ thống`), và lập bảng phát hiện/khắc phục cho 5 ca đại diện (Ca 9, 7, 18, 4, 17).
- **Nhiệm vụ D · Thiết kế pilot ([`pilot_plan.yaml`](pilot_plan.yaml)):** Tính cỡ mẫu 3 phương án chia cụm (D1), kiểm định 5 tiêu chí tách tác động (D2), chọn chia ngẫu nhiên phân tầng theo nhân viên (20 + 20) chấp nhận MDE 6 điểm (`n = 859/nhóm`, `m ≥ 299`, `DE = 6,96`) và viết trước 3 luật dừng đủ 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ`.
- **Nhiệm vụ E · Chỉ số, rủi ro & Hồ sơ Gate 2a ([`chi_so.md`](chi_so.md), [`ho_so_launch_v0.md`](ho_so_launch_v0.md)):** Đặc tả chỉ số chính/dùng/an toàn, thiết kế 10 event gắn `trace_id`, lập bảng rủi ro kinh tế từ bảng độ nhạy và tổng hợp thành 1 trang hồ sơ launch v0.

## 4. Kết quả

- **Kinh tế đơn vị:** Chi phí mỗi việc thành công = **4.472 đ** (`simulated`), gấp **16,3 lần** hóa đơn token + tool (274,7 đ/yc). Chi phí cả hệ thống (gồm 222 ca chuyển nhân viên) = **5.865 đ/yc = 0,49×** mức 12.000 đ (`simulated`). Trong phạm vi pilot (`noi_dia` 0,22× và `hang_nang` 0,69×), chi phí đạt **3.414 đ/việc** (`simulated`), cộng cố định 40 triệu đ/tháng thành **4.599 đ** (`simulated`).
- **Độ nhạy & rủi ro:** Ba yếu tố nhạy nhất là **1. Số ca làm lại** (+51,8% lên 6.787 đ, `simulated`), **2. Tỉ lệ xem lại** (+40,7% lên 6.292 đ, `simulated`), **3. Lương nhân viên** (+23,1% lên 5.506 đ, `simulated`). Nếu xem lại 100% kéo dài, chi phí lên **11.743 đ (0,98×)** hoặc **12.414 đ (1,03×)** nếu làm lại 15,3 phút (`simulated`).
- **Chỉ số đợt chạy thử (1.200 yc, chưa đối chứng):** Chỉ số chính = **82,83%** (994/1.200); bỏ qua gợi ý = **27,12%** (48/177); mở lại 7 ngày = **4,25%** (51/1.200).
- **Đề xuất chốt Gate 2a (`ho_so_launch_v0.md`):** **`Go có điều kiện`** cho pilot phạm vi `noi_dia` + `hang_nang`, gắn 4 điều kiện có người phụ trách và hạn kiểm tra (sửa Ca 7 & 20 trước pilot; Giám đốc vận hành ký chấp nhận MDE 6 điểm / power 0,64 tại 5 điểm; bật đủ 10 event thay phút `simulated` sau tuần 1; giảm tỉ lệ xem lại theo bậc khi `sua + bo` < 15%).
- **Kết quả duyệt chéo hội đồng:** `[Cập nhật sau phiên duyệt chéo 17:00–17:45 và liên kết phiếu chấm]`.

## 5. Khó khăn và cách xử lý

- **Rủi ro đánh giá sai chi phí thực:** Nếu chỉ nhìn hóa đơn token + tool (274,7 đ) sẽ bỏ sót 92,5% chi phí giờ nhân viên (xem lại + làm lại), hoặc bỏ sót 222 ca chuyển nhân viên. Nhóm tính đầy đủ cả `cps` lẫn chi phí toàn hệ thống (B3) và chi phí cố định (A4).
- **Giới hạn cỡ mẫu với 40 nhân viên:** Chia cụm 20 + 20 chỉ đạt `n_hiệu_dụng` tối đa 1.000 < 1.251 (không đủ bắt MDE 5 điểm). Nhóm minh bạch hóa đánh đổi nâng MDE lên 6 điểm (power giảm còn 0,64 nếu tác động thật 5 điểm) và yêu cầu Giám đốc vận hành ký xác nhận trước pilot.
- **Các ca lỗi dễ nhầm lẫn ở CP3:** Đối chiếu độc lập giữa Máy 3 và Máy 4 đạt đồng thuận **18/20 (90%)**; hai ca lệch ban đầu được thống nhất theo nguyên nhân gốc của Google PAIR (Ca 10 → `Ngữ cảnh` do xung đột thông tin ứng dụng dù đúng chính sách; Ca 20 → `Hệ thống` do thiếu khoá chống trùng), hoàn chỉnh đủ 20/20 ca.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp và bằng chứng của từng thành viên nằm trong [`TEAM.md`](../../TEAM.md) và các file báo cáo cá nhân `report/team/MSSV_HoTen.md`.

## 7. Hạn chế và hướng cải thiện

- **Dữ liệu phút xem lại/làm lại đang ở dạng giả lập (`simulated`):** Cần đo thời gian thực từ 2 event `staff_review_decision` và `staff_rework_completed` ngay trong tuần 1 pilot để hiệu chỉnh lại mô hình chi phí.
- **Đợt chạy thử 1.200 yc thiếu nhóm đối chứng:** Không thể kết luận tác động nhân quả từ mức 82,83%; pilot phân tầng ngẫu nhiên 20 + 20 nhân viên sẽ giải quyết bài toán tách tác động.
- **Rủi ro chi phí nếu giữ xem lại 100%:** Cần kiểm chứng độ tin cậy để rút tỉ lệ xem lại theo bậc khi tỉ lệ sửa + bỏ xuống dưới 15%, giữ thời gian xem lại ≤ 4,8 phút/ca.

## 8. Tài liệu tham khảo

- `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` và `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` (AI20K K5 — Ngày 13).
- Erol et al., *Cost-of-Pass: An Economic Framework for Evaluating Language Models* (arXiv:2504.13359).
- Google PAIR, *People + AI Guidebook* — chương "Errors + Graceful Failure".
- Tài liệu `statsmodels` (`NormalIndPower`).
