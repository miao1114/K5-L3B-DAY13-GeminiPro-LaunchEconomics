# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245,585.13 | `logix_runs.csv` | đo từ trace |
| Tool | 84,000.00 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93,804.49 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1,780,000.00 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2,264,000.00 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4,373,585.13 | | simulated |
| Số việc thành công | 978.00 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4,471.97 | | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274.65 | | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? 
- Chi phí mỗi việc thành công gấp 16.28 lần hoá đơn chia số yêu cầu
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? 
- Khoản lớn nhất là làm lại, 51,8% [simulated], tiếp theo là xem lại 40,7% [simulated]. Giờ nhân viên chiếm 92,5% tổng chi phí. Nếu số của bạn chỉ gấp 1–2 lần hoá đơn, bạn đã quên giờ của nhân viên.


## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95.0% | 1.11 | 2,696đ | 0.22× |
| hang_nang | 158 | 74.1% | 1.47 | 8,221đ | 0.69× |
| quoc_te | 150 | 27.3%  | 2.32 | 22,515đ | 1.88x |
| doi_tac | 68 | 54.4% | 1.88 | 10,215đ | 0.85× |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? 
- Với quoc_te, lần 1 đúng 30%, lần 2 chỉ 11,4%, lần 3 chỉ 2,2%. Lỗi lặp lại trên cùng yêu cầu nên chạy lại chỉ tốn thêm tiền.
- Kết luận: quoc_te không đáng để trợ lý xử lý (1,88×, thành công 27,3%), và chạy lại tới 3 lần không giúp. doi_tac sát ngưỡng (0,85×) và có điều khoản riêng, nên cũng loại khỏi phạm vi pilot.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33,750 | 1,185đ | 4,599đ | 0.38× |
| Một nửa khối lượng | 16,875 | 2,370đ | 5,784đ | 0.48× |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? ...
- Ở 45.000 yêu cầu/tháng, tổng là 4.599đ/việc; ở nửa tải (22.500), là 5.784đ — cả hai vẫn thấp hơn baseline 12.000đ nên chưa đổi kết luận [simulated].
- Với phí cố định 40 triệu/tháng, ngưỡng hòa vốn ước tính khoảng 6.200 yêu cầu/tháng (4.659 việc thành công, giả định tỉ lệ thành công 75%); thấp hơn mức này thì trợ lý có thể đắt hơn nhân viên [simulated].

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4,723đ | +5.6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4,346đ | -2.8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6,292đ | +40.7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3,562đ | -20.3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 |  6,787đ | +51.8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3,315đ | -25.9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5,506đ | +23.1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4,237đ | -5.2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4,111đ | -8.1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: 6,543đ, +46.3%
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. Làm lại gấp đôi (+51.8%) · 2. Xem lại gấp đôi (+40.7%) · 3. Lương tăng 25% (+23.1%)

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý [simulated] | Số yêu cầu không thành công | Chi phí cả hệ thống [simulated] | Chi phí mỗi việc thành công [simulated] |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3,621,781đ | 319 | 7,449,781đ | 4,111đ |
| 2 lần | 4,093,220đ | 234 | 6,901,220đ | 4,237đ |
| 3 lần | 4,373,585đ | 222 | 7,037,585đ | 4,472đ |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? ...
- Giới hạn 2 lần rẻ nhất cho công ty (6.901.220đ), nhưng không trùng với CPS thấp nhất: 1 lần chạy thấp nhất, 4.111đ/việc thành công.
- Chạy tối đa 3 lần giảm số việc thất bại còn 222, nhưng tổng chi phí cao hơn giới hạn 2 lần 136.365đ [simulated].

## B4 · Nếu phải xem lại tất cả

-Chi phí mỗi việc thành công khi xem lại 100% (noi_dia + hang_nang), so với 12.000 đ: ...
- Xem lại 100% (948 yêu cầu, `noi_dia` + `hang_nang`): 48 ca làm lại × 9,00 phút cho CPS 11.743đ (0,98×); × 15,30 phút cho 12.415đ (1,03×), so với baseline 12.000đ [simulated].
- Kết quả này nói gì về thứ pilot cần học được? ...
- Ngưỡng hòa vốn của thời gian xem lại là ≤5,12 phút hoặc ≤4,80 phút tùy kịch bản [simulated]; pilot cần đo thời gian xem lại thực tế và xác định cách giảm thời gian/tỷ lệ xem lại.
