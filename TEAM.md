# Team

## Thông tin nhóm

- Tên nhóm: GeminiPro
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-GeminiPro-LaunchEconomics`
- URL repo, nhánh nộp, commit chốt: `https://github.com/miao1114/K5-L3B-DAY13-GeminiPro-LaunchEconomics`, nhánh `main` (đang tổng hợp từ nhánh `P4`), commit chốt `[cập nhật lúc 17:45]`

## Thành viên

| STT | Máy | Họ tên | MSSV | Email | GitHub | Vai trò (theo bảng phân công) | File phụ trách |
| --: | --- | ------ | ---- | ----- | ------ | ----------------------------- | -------------- |
| 1 | Máy 4 | Nguyễn Đức Minh | 2A202603765 | 26ai.minhnd5@vinuni.edu.vn | miao1114 | PM & Hồ sơ tổng (Người gắn nhãn 2 kiêm Giữ hồ sơ) | `TEAM.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `docs/notes/nhan_loi_may4.md` |
| 2 | Máy 1 | Nguyễn Văn Hiếu | 2A202603746 | 26ai.hieunv3@vinuni.edu.vn | lunaHieu | Dev / Data (Người viết code) | `src/lab13.py` |
| 3 | Máy 3 | Phạm Thế Hùng | 2A202603778 | 26ai.hungpt5@vinuni.edu.vn | thehung1406 | Lỗi & Telemetry (Người gắn nhãn 1) | `report/team/bang_loi.md`, `report/team/chi_so.md` |
| 4 | Máy 2 | Nguyễn Văn Cường | 2A202603750 | 26ai.cuongnv2@vinuni.edu.vn | nvcuong96 | Kinh tế & Pilot (Người kiểm số) | `report/team/bang_chi_phi.md`, `report/team/pilot_plan.yaml` |

Phân công chi tiết 4 máy:

- **Máy 1 · Dev / Data (`src/lab13.py`):** Viết code chạy lần lượt 3 cụm (TODO CP1 → TODO CP2 → TODO CP4 gồm `NormalIndPower` & tỉ lệ `mo_lai_trong_7_ngay`), xuất kết quả ra terminal gửi vào nhóm chat cho Máy 2 & Máy 4 ngay khi xong từng CP.
- **Máy 2 · Kinh tế & Pilot (`report/team/bang_chi_phi.md`, `report/team/pilot_plan.yaml`):** Soạn sẵn khung bảng, chữ giải thích (≤ 3 dòng/câu) và 3 luật dừng (`NẾU – TRONG – THÌ – KHÔNG THÌ`); khi nhận số từ Máy 1, điền bảng A2, A3, A4, B1–B4 (gắn nhãn `simulated`) và D1, D2 vào YAML; push trước 16:40 để Máy 4 ghép hồ sơ.
- **Máy 3 · Lỗi & Telemetry (`report/team/bang_loi.md`, `report/team/chi_so.md`):** Chạy độc lập 100%: (1) gắn bộ nhãn 1 cho 20 ca lỗi, (2) soạn bảng khắc phục 5 ca (cách phát hiện đo được + 1 vai trò phụ trách), (3) soạn danh sách ≥ 6 event có `trace_id` và 2 chỉ số tự đề xuất trong `chi_so.md`; gửi 20 nhãn cho Máy 4 lúc 15:35 đối chiếu đồng thuận (≥ 16/20 ca).
- **Máy 4 · PM & Hồ sơ tổng (`TEAM.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`):** Điền `TEAM.md`, dựng khung 7 mục `ho_so_launch_v0.md`; đúng 15:35 (CP3) gắn nhãn độc lập 20 ca lỗi (bộ nhãn 2) rồi đối chiếu với Máy 3; 16:36 gom số chốt từ Máy 2 & Máy 3 điền vào `ho_so_launch_v0.md`, kiểm tra quy tắc cấm từ và điều phối push bài lúc 17:00 (duyệt chéo) và 17:45 (nộp cuối).

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/team/` theo dạng `report/team/MSSV_HoTen.md` (ví dụ: `report/team/20241234_NguyenVanAn.md`).

## NguyenDucMinh-2A202603765

### Phần việc phụ trách

- Máy 4 (PM & Hồ sơ tổng): `TEAM.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `docs/notes/nhan_loi_may4.md`, và báo cáo cá nhân `report/team/2A202603765_NguyenDucMinh.md`.

### Đóng góp cụ thể

- Hoàn thiện `TEAM.md`, `report/team/group_report.md` và dựng hoàn chỉnh hồ sơ 1 trang `report/team/ho_so_launch_v0.md` đủ 7 mục + đề xuất `Go có điều kiện` kèm 4 điều kiện có vai trò phụ trách và hạn kiểm tra.
- Gắn nhãn độc lập 20 ca lỗi (bộ nhãn 2) theo 5 loại Google PAIR vào `docs/notes/nhan_loi_may4.md` để đối chiếu CP3 với Máy 3.
- Kiểm tra chất lượng Gate 2a (0 từ cấm, câu giải thích ≤ 3 dòng có số, gắn nhãn `simulated` đầy đủ, 1 vai trò/mục).

### Bằng chứng

- `TEAM.md`, `docs/notes/nhan_loi_may4.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `report/team/2A202603765_NguyenDucMinh.md` (nhánh `P4`, commit `a61097e`).

## NguyenVanHieu-2A202603746

### Phần việc phụ trách

- Máy 1 (Dev / Data): xây dựng và chạy toàn bộ `src/lab13.py` (CP1, CP2, CP4).

### Đóng góp cụ thể

- Hoàn thành 3 hàm A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`) và hàm kiểm thử `kiem_tra_dap_an_biet_truoc()` (đạt 1,20 · 1,25 · 1,25).
- Hoàn thành hàm `mo_hinh()` và `in_bang()` tính đầy đủ A2, A3 (tách theo `loai` + tỉ lệ `ok` theo `attempt`), A4 (chi phí cố định 40 triệu/tháng ở 45.000 và 22.500 yc/tháng), B1–B4 (9 kịch bản đơn, kịch bản cặp, xếp hạng 3 yếu tố, chi phí cả hệ thống 1–3 lần chạy, xem lại 100% và mức hoà vốn).
- Hoàn thành phần D1 (`co_mau_hai_ti_le` cho 5 câu a–e, tỉ lệ `mo_lai_trong_7_ngay`, và tính power với `NormalIndPower` khi tác động thật +5 điểm ở n=859).

### Bằng chứng

- `src/lab13.py` (commit `9b7a85b`, đã merge vào `main` qua PR #1 `06ad45a`).
- File báo cáo cá nhân: `report/team/2A202603746_NguyenVanHieu.md` `[Chờ Máy 1 bổ sung]`.

## PhamTheHung-2A202603778

### Phần việc phụ trách

- Máy 3 (Lỗi & Telemetry): hoàn thiện độc lập `report/team/bang_loi.md` (bộ nhãn 1 + bảng khắc phục 5 ca) và `report/team/chi_so.md` (E1, danh sách event có `trace_id`, khung E2).

### Đóng góp cụ thể

- Gắn bộ nhãn độc lập 1 cho toàn bộ 20 ca lỗi trong `report/team/bang_loi.md` và hoàn thiện bảng khắc phục 5 ca đại diện (Ca 9, 7, 18, 4, 17) với cách phát hiện đo được (event, ngưỡng, tần suất) và 1 vai trò phụ trách cụ thể.
- Hoàn thiện E1 trong `report/team/chi_so.md`: tính thử 3 chỉ số trên 1.200 yêu cầu (82,83%, 27,12%, 4,25%), đề xuất 2 chỉ số mới (tỉ lệ dùng trợ lý nhóm can thiệp, tỉ lệ đơn sai tiền qua `audit_sample_checked`), thiết kế 10 event gắn `trace_id` và đối chiếu công thức tính từng chỉ số.
- Hoàn thiện 3 dòng rủi ro kinh tế E2 trong `report/team/chi_so.md` kèm đầy đủ số liệu `simulated` từ mô hình chi phí nhóm (`PM trợ lý hoàn phí`, `Trưởng nhóm CSKH`).

### Bằng chứng

- `report/team/bang_loi.md`, `report/team/chi_so.md` (PR #2 `5d6393f` và PR chốt E2 + báo cáo cá nhân).
- File báo cáo cá nhân: `report/team/2A202603778_PhamTheHung.md`.

## NguyenVanCuong-2A202603750

### Phần việc phụ trách

- Máy 2 (Kinh tế & Pilot): kiểm số đối chiếu, hoàn thiện `report/team/bang_chi_phi.md` (A2–A4, B1–B4) và `report/team/pilot_plan.yaml` (D1–D3, 3 luật dừng 4 vế).

### Đóng góp cụ thể

- `[Đang thực hiện — chờ Máy 2 push trước 16:40 để chốt bảng số liệu và pilot_plan.yaml]`.

### Bằng chứng

- `report/team/bang_chi_phi.md`, `report/team/pilot_plan.yaml`, `report/team/2A202603750_NguyenVanCuong.md` `[Chờ Máy 2 push]`.
