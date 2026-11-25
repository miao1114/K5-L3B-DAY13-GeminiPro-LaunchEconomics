# Báo cáo cá nhân — Nguyễn Văn Cường

## 1. Thông tin thành viên

- Họ tên: Nguyễn Văn Cường
- MSSV: 2A202603750
- Email: 26ai.cuongnv2@vinuni.edu.vn
- Vai trong nhóm: Người kiểm số
- Phần việc được phân công: Máy 2 — Kinh tế & Pilot

## 2. Phần việc phụ trách

Phụ trách phần phân tích kinh tế và hỗ trợ kế hoạch pilot: đọc cấu trúc bảng chi phí và YAML, chuẩn bị cách trình bày kết quả; tiếp nhận số liệu chạy từ Máy 1 để hoàn thiện các mục A2–A4, B1–B4 và ghi lại các phép tính cỡ mẫu D1.

## 3. Đóng góp cụ thể

- Tổng hợp chi phí theo trace và theo loại yêu cầu; phân biệt chi phí đo từ trace với các chi phí giả lập.
- Phân tích chi phí cố định 40 triệu đồng/tháng: tổng chi phí mỗi việc thành công là 4.599đ ở 45.000 yêu cầu/tháng và 5.784đ ở nửa khối lượng; cả hai thấp hơn baseline 12.000đ.
- So sánh giới hạn chạy lại: giới hạn 2 lần có chi phí toàn hệ thống thấp nhất (6.901.220đ), còn giới hạn 1 lần có CPS thấp nhất (4.111đ).
- Đánh giá kịch bản xem lại 100%: CPS dao động từ 11.743đ đến 12.415đ tùy giả định thời gian; nêu việc cần đo trong pilot là thời gian và tỷ lệ xem lại thực tế.
- Ghi lại các kết quả cỡ mẫu D1, gồm 1.251 yêu cầu/nhóm khi chia theo yêu cầu và 859 yêu cầu/nhóm trong kịch bản chênh lệch 6 điểm.

## 4. Bằng chứng

- [Bảng chi phí A và B](./bang_chi_phi.md): các bảng A2–A4, B1–B4 và phần diễn giải kết quả kinh tế.
- [Kế hoạch pilot](./pilot_plan.yaml): ghi chú kết quả tính cỡ mẫu D1, tỷ lệ mở lại và power của kịch bản n=859 mỗi nhóm.

## 5. Công cụ AI đã dùng

Đã dùng Copilot trong VS Code để hỗ trợ diễn đạt ngắn gọn các kết quả và tổ chức nội dung báo cáo. Các con số đầu vào được đối chiếu với kết quả chạy do nhóm cung cấp; các kết luận so sánh được kiểm tra lại bằng phép tính từ những số liệu đó.

## 6. Tự đánh giá

Phần phân tích giúp phân biệt mục tiêu tối ưu chi phí toàn hệ thống với CPS, đồng thời làm rõ rủi ro khi khối lượng thấp hoặc phải xem lại nhiều. Các kết quả phụ thuộc vào giả định simulated; bước tiếp theo là xác nhận các giả định này trong pilot và hoàn thiện các nội dung thiết kế pilot còn lại.
