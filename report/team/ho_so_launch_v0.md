# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi **Giả lập**. Người phụ trách là một vai trò cụ thể có quyền quyết định, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot theo quy tắc 5 trong `README.md`.

Nhóm: **GeminiPro** · Lớp: **L3B**

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.472 đ** (`simulated`), gấp **16,3 lần** hóa đơn token + tool (274,7 đ/yc, đo từ trace). Trong phạm vi pilot (`noi_dia` + `hang_nang`): **3.414 đ/việc** (`simulated`); cộng cố định 40 triệu đ/tháng (1.185 đ/việc ở 45.000 yc/tháng) thành **4.599 đ** (`simulated`). | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | **1. Số ca làm lại** (+51,8% lên **6.787 đ** khi gấp đôi, `simulated`); **2. Tỉ lệ xem lại** (+40,7% lên **6.292 đ**, `simulated`); **3. Lương nhân viên** (+23,1% lên **5.506 đ** khi tăng 25%, `simulated`). | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Chi phí cả hệ thống (gồm 222 ca chuyển nhân viên) = **5.865 đ/yc = 0,49×** mức 12.000 đ (`simulated`). Theo phạm vi (`simulated`): `noi_dia` **0,22×** (2.696 đ), `hang_nang` **0,69×** (8.221 đ), `quoc_te` **1,88×** (22.515 đ, loại), `doi_tac` **0,85×** (10.215 đ, loại). | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Đợt chạy thử 1.200 yc (chưa có đối chứng): Chính (đóng ≤ 24h, không mở lại 7 ngày) = **82,83%** (994/1.200); Dùng (bỏ qua gợi ý `sua` + `bo`) = **27,12%** (48/177); An toàn (mở lại 7 ngày) = **4,25%** (51/1.200). Log đủ **10 event** gắn `trace_id`. | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Gắn nhãn độc lập **20 ca lỗi** theo 5 loại Google PAIR đạt đồng thuận **18/20 (90%)** (vượt ngưỡng 80%, đã thống nhất đủ 20/20 ca). Đã lập bảng khắc phục **5 ca đại diện** (Ca 9, 7, 18, 4, 17) kèm event cảnh báo và ngưỡng đo cụ thể. | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia ngẫu nhiên phân tầng theo **nhân viên (20 can thiệp + 20 đối chứng)** trong 6 depot, phạm vi chỉ `noi_dia` + `hang_nang`. Cỡ mẫu **859 yc/nhóm** (`m ≥ 299` yc/người, `DE = 6,96`), chấp nhận MDE **6 điểm** (power còn **0,64** nếu tác động thật 5 điểm) kèm **3 luật dừng** đủ 4 vế. | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | (1) Số ca làm lại tăng gấp đôi làm chi phí tăng **+51,8%** lên **6.787 đ** (`simulated`); (2) Nếu xem lại 100% kéo dài, chi phí lên **11.743 đ (0,98×)** (làm lại 9 phút) hoặc **12.414 đ (1,03×)** nếu làm lại 15,3 phút (`simulated`). | Giả lập | PM trợ lý hoàn phí |

**Đề xuất Gate 2a:** **`Go có điều kiện`** cho kế hoạch pilot phạm vi `noi_dia` + `hang_nang` (loại `quoc_te` 1,88× và `doi_tac` 0,85×, `simulated`), với **4 điều kiện bắt buộc**:

1. **Khóa chống trùng và đối soát sổ cái (Ca 7, 20):** `Kỹ sư trưởng agent` hoàn tất khóa chống trùng (`idempotency_key`) và đối soát sổ cái trả `ok` trước khi báo hoàn thành — **Hạn kiểm tra:** trước ngày bắt đầu pilot.
2. **Ký chấp nhận đánh đổi cỡ mẫu:** `Giám đốc vận hành LogiX-VN` ký duyệt mức chênh tối thiểu 6 điểm (chấp nhận power còn 0,64 nếu tác động thật 5 điểm) — **Hạn kiểm tra:** trước ngày bắt đầu pilot.
3. **Bật log và thay số giả lập bằng đo thật:** `Kỹ sư trưởng agent` bật đủ 10 event có `trace_id`, thay cột phút `simulated` bằng thời gian xem lại/làm lại đo thật — **Hạn kiểm tra:** ngay sau tuần 1 pilot.
4. **Lộ trình giảm tỉ lệ xem lại theo bậc:** `Trưởng nhóm CSKH` kích hoạt giảm tỉ lệ xem lại theo bậc ngay khi tỉ lệ sửa + bỏ < 15% (vì xem lại 100% tốn 0,98×–1,03×, `simulated`, không tiết kiệm) — **Hạn kiểm tra:** cuối bước rollout 0,25 (tuần 2 pilot).
