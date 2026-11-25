# Báo cáo cá nhân — Nguyễn Văn Hiếu

## 1. Thông tin thành viên

- Họ tên: Nguyễn Văn Hiếu
- MSSV: 2A202603746
- Email: 26ai.hieunv3@vinuni.edu.vn
- Vai trong nhóm: Máy 1 — Dev / Data (Người viết code)

## 2. Phần việc phụ trách

Phụ trách `src/lab13.py`: tính nhiệm vụ A (A1–A4), B (B1–B4), năm câu cỡ mẫu D1, power bằng `NormalIndPower` và tỉ lệ `mo_lai_trong_7_ngay`. Xuất số từ terminal để Máy 2 điền bảng chi phí, kế hoạch pilot và Máy 4 đối chiếu hồ sơ tổng.

## 3. Đóng góp cụ thể

- Hoàn thiện ba hàm A1 và phép thử đáp án biết trước: `1,20 · 1,25 · 1,25` — **ĐẠT**.
- Xây dựng `mo_hinh()` cộng token và tool của mọi lần chạy, kể cả lần lỗi, cộng thời gian xem lại/làm lại `simulated`, rồi chia cho số yêu cầu `thanh_cong`. Trên 1.624 lần chạy và 1.200 yêu cầu, tổng chi phí là **4.373.585,13 đ**, có **978** việc thành công và chi phí **4.471,97 đ/việc** `simulated`. Khoản **93.804,49 đ** của lần chạy thứ 2–3 đã nằm trong token và tool, không cộng hai lần.
- Tách A3 theo bốn loại: `noi_dia` **2.696 đ**, `hang_nang` **8.221 đ**, `quoc_te` **22.515 đ**, `doi_tac` **10.215 đ/việc** (`simulated`). Tính A4 cho phạm vi nội địa + hàng nặng: **4.599 đ/việc** ở 45.000 yêu cầu/tháng và **5.784 đ/việc** khi khối lượng còn một nửa (`simulated`).
- Chạy đủ chín kịch bản B1 và kịch bản kết hợp B2; xếp hạng tác động tăng chi phí: làm lại **+51,8%**, xem lại **+40,7%**, lương **+23,1%** (`simulated`). B3 cho thấy giới hạn **2 lần chạy** có tổng chi phí cả hệ thống thấp nhất: **6.901.220 đ** (`simulated`). B4 xem lại 100% cho **11.743 đ/việc** với 9 phút làm lại và **12.415 đ/việc** với thời gian làm lại trung bình từ dữ liệu (`simulated`).
- Tính D1: **1.251** yêu cầu/nhóm để thấy chênh 5 điểm khi chia theo yêu cầu; với 75 yêu cầu/nhân viên cần **42** nhân viên/nhóm, vượt 40 người hiện có. Với 20 nhân viên/nhóm và MDE 6 điểm cần ít nhất **299** yêu cầu/người. Tỉ lệ mở lại 7 ngày là **4,25%** toàn mẫu và **3,97%** trong phạm vi nội địa + hàng nặng; power còn **0,642** nếu tác động thật là 5 điểm nhưng cỡ mẫu thiết kế cho 6 điểm.

## 4. Bằng chứng

- [`src/lab13.py`](../../src/lab13.py): commit `9b7a85b`, đã merge vào `main` qua PR #1 (`06ad45a`).
- Tự chạy `python -m pip install -r requirements.txt`, lệnh kiểm import báo `san sang`, rồi chạy `python lab13.py` trong `src/` đến hết; A1 in **ĐẠT** và các bảng A–B–D1 có số.
- Tự chạy riêng ba giá trị A1 và kiểm A2 trực tiếp từ hai CSV: 1.624 lần chạy, 1.200 yêu cầu, 978 việc thành công, tổng **4.373.585,13 đ** và **4.471,97 đ/việc** (`simulated`), khớp với output `lab13.py`.

## 5. Công cụ AI đã dùng

Dùng Codex (ChatGPT) để hỗ trợ triển khai và rà soát `src/lab13.py`, giải thích công thức chi phí/cỡ mẫu và kiểm tra sự phù hợp với hướng dẫn. Tôi tự chạy các lệnh setup và `python lab13.py` trên máy, đối chiếu ba phép thử A1 và tính lại A2 trực tiếp từ CSV. Các con số trong báo cáo lấy từ output đã chạy; hai cột phút `_simulated` được ghi nhãn `simulated`.

## 6. Tự đánh giá

Đã hoàn thành và chạy được phần code Máy 1. Tôi phân biệt được chi phí mỗi việc thành công với chi phí cả hệ thống: lần lỗi vẫn tốn tiền, còn yêu cầu không thành công cần nhân viên làm thay. Loại `quoc_te` có tỉ lệ thành công **27,3%** và CPS **22.515 đ**, cao hơn baseline **12.000 đ**, nên không phù hợp với phạm vi pilot đề xuất. Trong các lần chạy quốc tế, tỉ lệ `status=ok` giảm từ **30,0%** ở lần 1 xuống **11,4%** ở lần 2 và **2,2%** ở lần 3; đây là các nhóm ca còn lại sau mỗi lần thử, nên chạy lại đến 3 lần vẫn không cứu được nhiều ca khó. Kết quả chi phí phụ thuộc phút `simulated`; pilot cần đo thời gian thực và có nhóm đối chứng trước khi kết luận tác động của trợ lý.
