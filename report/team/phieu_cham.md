# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): **GeminiPro (L3B)**
- Nhóm được chấm: **MRX (L3B)**

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | **10** | Đề xuất `Go có điều kiện` khớp số liệu: nêu rõ xem lại 100% tốn 11.743–12.415 đ (0,98–1,03×, `simulated`), MDE 6 điểm (power ~0,64 ở 5 điểm), mở lại 4,25% và không có đối chứng; kèm 4 điều kiện có vai trò và hạn kiểm tra (`2026-12-10`, `2026-12-15`, `2026-12-29`). |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | **10** | Cả `ho_so_launch_v0` (Mục 1, 2, 3, 7) và `chi_so` (E2) đều gắn nhãn `simulated` và trạng thái `Giả lập` đầy đủ; không dùng từ cấm; thu hẹp phạm vi chỉ giữ `noi_dia` + `hang_nang`, loại `quoc_te` (22.515 đ = 1,88×, thành công 27,3%) và `doi_tac` (0,85×). |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | **10** | Chia theo nhân viên 20 + 20 cụm ngẫu nhiên phân tầng theo depot, có đối chứng đồng thời; đủ cỡ mẫu 859/nhóm (`m ≥ 299`, `DE = 6,96`) cho MDE 6 điểm; `pilot_plan.yaml` đủ 3 luật dừng 4 vế có ngưỡng, thời hạn (`7 ngày`, `2 tuần`, `1 tuần`), người có quyền dừng (`Giám đốc vận hành` tắt trong 30 phút) và ngày quyết định `2027-01-05`. |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** **Go có điều kiện** *(đồng thuận với đề xuất của nhóm MRX)*

**Lý do:** Hồ sơ của nhóm MRX đầy đủ cả 7 mục trên 1 trang và khớp chéo với `chi_so.md` (đủ 5 chỉ số E1, 9 event có `trace_id`, 2 dòng rủi ro E2 có `simulated`). Nhóm minh bạch hóa đầy đủ các con số bất lợi (xem lại 100% tốn 0,98–1,03×, power giảm còn 0,64 ở 5 điểm, đồng thuận lỗi ban đầu 75% đã viết lại định nghĩa) và khóa chặt bằng 4 điều kiện có hạn kiểm tra rõ ràng trước khi mở pilot. *(Góp ý nhỏ: trang hồ sơ nên ghi thêm `m ≥ 299` yc/nhân viên và mốc thời gian/ngưỡng kích hoạt giảm xem lại theo bậc).*

**Một câu hỏi cho đội trình:** Ở Điều kiện 4 (giảm xem lại theo bậc), nhóm chọn ngưỡng tỉ lệ sửa + bỏ gợi ý là bao nhiêu để bắt đầu giảm tỉ lệ xem lại, và trong 3 luật dừng (6%, 8.000 đ, 40%) thì thời hạn theo dõi liên tiếp là bao lâu trước khi Giám đốc vận hành bấm dừng?

**Câu trả lời của đội trình (ghi lại tại buổi):** Nhóm bắt đầu giảm xem lại một bậc khi tỉ lệ sửa + bỏ dưới 15% trong 2 tuần liên tiếp và chỉ số an toàn vẫn đạt ngưỡng (hiện đang là 27,12%, nên chưa giảm ngay); còn về luật dừng, chỉ luật an toàn 6% mới khiến Giám đốc vận hành tắt trợ lý trong 30 phút sau 7 ngày liên tiếp vượt ngưỡng, còn luật chi phí 8.000 đ (2 tuần) và luật bỏ qua gợi ý 40% (1 tuần) chỉ chặn mở rộng và kích hoạt hành động khắc phục chứ không tắt trợ lý.
