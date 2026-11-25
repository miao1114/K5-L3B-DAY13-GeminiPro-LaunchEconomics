# Báo cáo cá nhân — NguyenDucMinh-2A202603765

## 1. Thông tin thành viên

- Họ tên: Nguyễn Đức Minh
- MSSV: `2A202603765`
- Email: `26ai.minhnd5@vinuni.edu.vn`
- Vai trong nhóm: Người gắn nhãn 2 kiêm Giữ hồ sơ (Máy 4)

## 2. Phần việc phụ trách

- **Quản lý thông tin nhóm & báo cáo tổng hợp:** Cập nhật `TEAM.md` (phân công 4 máy, phạm vi file zero-conflict) và viết `report/team/group_report.md`.
- **Gắn nhãn độc lập 20 ca lỗi (CP3):** Trích xuất và phân loại độc lập 20 ca lỗi từ đề bài theo 5 loại Google PAIR vào `docs/notes/nhan_loi_may4.md`, gửi Máy 3 đối chiếu đồng thuận ghép vào `report/team/bang_loi.md`.
- **Giữ hồ sơ & kiểm soát chất lượng Gate 2a:** Tổng hợp trang hồ sơ 1 trang `report/team/ho_so_launch_v0.md` đủ 7 mục + đề xuất `Go có điều kiện` kèm 4 điều kiện, và chạy kiểm tra tuân thủ 5 quy tắc lab trước khi chốt nộp.

## 3. Đóng góp cụ thể

- **Nhiệm vụ C (CP3):** Gắn nhãn độc lập 20/20 ca lỗi theo đúng nguyên nhân gốc (`Do người dùng`: 1, 6, 9, 14; `Hệ thống`: 2, 7, 8, 15, 20; `Ngữ cảnh`: 3, 10, 16, 18; `Giới hạn hệ thống`: 4, 11, 13, 19; `Ngầm`: 5, 12, 17), kèm lý do ≤ 2 dòng/ca; ghép vào `report/team/bang_loi.md` đối chiếu với Máy 3 đạt đồng thuận **18/20 (90%)** (vượt ngưỡng 80%) và thống nhất 2 ca lệch (Ca 10 → `Ngữ cảnh`, Ca 20 → `Hệ thống`).
- **Nhiệm vụ E (`ho_so_launch_v0.md`):** Chuẩn hóa đủ 7 mục cốt lõi trên 1 trang, bảo đảm mọi con số từ hai cột `_simulated` đều có nhãn `simulated`, dùng đúng 3 giá trị trạng thái (`Xong, có bằng chứng` · `Chưa` · `Giả lập`), gán đúng 1 vai trò có quyền quyết định cho mỗi mục, không khẳng định sai rằng trợ lý "đã nâng" chỉ số từ đợt chạy thử không đối chứng, và chốt đề xuất **`Go có điều kiện`** kèm 4 điều kiện có người phụ trách và hạn kiểm tra cụ thể.
- **Tổng hợp & kiểm định chất lượng:** Hoàn thiện `TEAM.md`, `report/team/group_report.md` và thực hiện kiểm tra tự động 4 tiêu chí chất lượng (0 vi phạm quy tắc 5, câu giải thích ≤ 3 dòng có số liệu, đủ nhãn `simulated`, không ghi "cả đội" ở cột người phụ trách).

## 4. Bằng chứng

- [`TEAM.md`](../../TEAM.md): Bảng thành viên 4 máy, phạm vi file và mục đóng góp cá nhân.
- [`docs/notes/nhan_loi_may4.md`](../../docs/notes/nhan_loi_may4.md): Bảng gắn nhãn độc lập 20 ca lỗi (20/20 khớp chuẩn Google PAIR) và nhật ký kiểm tra chất lượng.
- [`report/team/ho_so_launch_v0.md`](ho_so_launch_v0.md): Hồ sơ launch v0 dài 1 trang (7 mục + đề xuất `Go có điều kiện` với 4 điều kiện).
- [`report/team/group_report.md`](group_report.md): Báo cáo nhóm tổng hợp nhiệm vụ A–E và kết quả Gate 2a.

## 5. Công cụ AI đã dùng

- **Công cụ:** Trợ lý AI trong IDE (Antigravity).
- **Mục đích sử dụng:** Hỗ trợ trích xuất nội dung 20 ca lỗi từ file đề bài `.docx`, rà soát nhất quán số liệu giữa `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` và các file hồ sơ Máy 4, biên tập bảng Markdown gọn trong 1 trang và chạy lệnh kiểm tra tự động (ràng buộc từ cấm, độ dài dòng, nhãn `simulated`).
- **Tự kiểm tra kết quả:** Đọc đối chiếu trực tiếp từng con số (4.472 đ, 16,3×, 4.599 đ, 5.865 đ = 0,49×, 82,83%, 27,12%, 4,25%, 859 yc/nhóm, power 0,64, 11.743 đ / 12.414 đ) và từng nhãn lỗi 1–20 với tài liệu hướng dẫn chuẩn; xác nhận phạm vi zero-conflict không chỉnh sửa file của Máy 1, 2, 3.

## 6. Tự đánh giá

- **Điểm đạt được:** Hoàn thành đúng phạm vi Máy 4 không gây xung đột git với 3 máy còn lại; hồ sơ launch v0 trình bày gọn 1 trang, minh bạch con số bất lợi (MDE 6 điểm làm power còn 0,64 ở 5 điểm; xem lại 100% tốn 0,98×–1,03×, `simulated`) và gắn điều kiện kiểm soát rõ ràng trước khi mở pilot.
- **Điểm cần phối hợp tiếp:** Ghép phiếu chấm duyệt chéo `report/team/phieu_cham.md` và cập nhật kết quả hội đồng vào mục 4 của `group_report.md` sau phiên duyệt chéo 17:00–17:45.
