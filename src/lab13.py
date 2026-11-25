"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python lab13.py (cần pandas và statsmodels).
Không cần khoá API. Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import sys
from statistics import NormalDist

import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# Ba hàm A1 được kiểm bằng kiem_tra_dap_an_biet_truoc().
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if not 0 < p <= 1 or (k is not None and k < 1):
        raise ValueError('Cần 0 < p <= 1 và k là số nguyên dương')
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if not 0 < p <= 1 or (k is not None and k < 1):
        raise ValueError('Cần 0 < p <= 1 và k là số nguyên dương')
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# CP1 tính chi phí từ trace; CP2 gọi lại cùng hàm với tham số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        if max_lan_chay < 1:
            raise ValueError('max_lan_chay phải ít nhất là 1')
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    token = tien_token.sum()
    tool = tien_tool.sum()
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    if not thanh_cong:
        raise ValueError('Không có việc thành công để tính chi phí mỗi việc')
    return dict(token=token, tool=tool,
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(token + tool) / len(reqs))


def co_mau_hai_ti_le(p1, p2, alpha=0.05, power=0.8):
    """Số yêu cầu mỗi nhóm theo xấp xỉ chuẩn hai tỉ lệ độc lập (D1)."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    p_trung_binh = (p1 + p2) / 2
    tu_so = (za * math.sqrt(2 * p_trung_binh * (1 - p_trung_binh))
              + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    return math.ceil(tu_so / (p2 - p1) ** 2)


def in_bang(runs, reqs):
    """In số cho người phụ trách bảng chi phí và kế hoạch pilot."""
    goc = mo_hinh(runs, reqs)
    print('\nA2 · Mô hình chi phí (simulated ở các dòng có giờ nhân viên)')
    for ten, gia_tri in goc.items():
        nhan = ' [simulated]' if ten in {'xem_lai', 'lam_lai', 'tong', 'cps'} else ''
        print(f'{ten:18s} {gia_tri:>14,.2f}{nhan}')
    print(f"Bội số so với hoá đơn/yêu cầu: {goc['cps'] / goc['hoa_don_moi_yc']:.2f}× [simulated]")
    khong_thanh_cong = len(reqs) - goc['thanh_cong']
    cp_he_thong = (goc['tong'] + khong_thanh_cong * BASELINE) / len(reqs)
    print(f'Chi phí cả hệ thống/yêu cầu: {cp_he_thong:,.0f}đ '
          f'({cp_he_thong/BASELINE:.2f}× baseline; gồm {khong_thanh_cong} ca nhân viên làm thay) [simulated]')

    print('\nA3 · Theo loại yêu cầu (CPS simulated)')
    for loai, nhom in reqs.groupby('loai', sort=False):
        chi_phi = mo_hinh(runs, nhom)
        so_lan = nhom['so_lan_chay'].sum() / len(nhom)
        print(f"{loai:12s} n={len(nhom):4d} thành công={chi_phi['thanh_cong']/len(nhom):6.1%} "
              f"lần/yêu cầu={so_lan:.2f} cps={chi_phi['cps']:,.0f}đ "
              f"so baseline={chi_phi['cps']/BASELINE:.2f}× [simulated]")
    ti_le_ok = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    ti_le_ok['ok'] = ti_le_ok['status'].eq('ok')
    print('Tỉ lệ run status=ok theo lần thử (mẫu giảm dần ở lần 2, 3):')
    for loai, nhom in ti_le_ok.groupby('loai', sort=False):
        ty_le = nhom.groupby('attempt')['ok'].mean()
        print(f'{loai:12s} ' + ', '.join(f'lần {lan}: {gia_tri:.1%}'
                                          for lan, gia_tri in ty_le.items()))

    print('\nA4 · Chi phí cố định trong phạm vi noi_dia + hang_nang')
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    cp_pham_vi = mo_hinh(runs, pham_vi)
    for khoi_luong in (45000, 22500):
        thanh_cong_thang = khoi_luong * cp_pham_vi['thanh_cong'] / len(reqs)
        co_dinh_moi_viec = 40_000_000 / thanh_cong_thang
        cp_day_du = cp_pham_vi['cps'] + co_dinh_moi_viec
        print(f'{khoi_luong:,} yc/tháng: {thanh_cong_thang:,.0f} việc thành công, '
              f'cố định={co_dinh_moi_viec:,.0f}đ/việc, '
              f'tổng={cp_day_du:,.0f}đ/việc ({cp_day_du/BASELINE:.2f}×) [simulated]')

    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi': dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi': dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương tăng 25%': dict(luong_phut=2500),
        'Tối đa 2 lần chạy': dict(max_lan_chay=2),
        'Chỉ 1 lần chạy': dict(max_lan_chay=1),
    }
    print('\nB1 · Độ nhạy (CPS simulated)')
    tac_dong = {}
    for ten, tham_so in kich_ban.items():
        cps = mo_hinh(runs, reqs, **tham_so)['cps']
        thay_doi = (cps / goc['cps'] - 1) * 100
        tac_dong[ten] = thay_doi
        print(f'{ten:26s} {cps:>9,.0f}đ {thay_doi:+6.1f}% [simulated]')
    cp_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'B2 · Token × 2 + xem lại × 2: {cp_cap:,.0f}đ, '
          f'{(cp_cap/goc["cps"]-1)*100:+.1f}% [simulated]')
    xep_hang = sorted((ten for ten in tac_dong if tac_dong[ten] > 0),
                      key=lambda ten: tac_dong[ten], reverse=True)[:3]
    print('B2 · Ba yếu tố tăng chi phí mạnh nhất: '
          + ' · '.join(f'{i}. {ten} (+{tac_dong[ten]:.1f}%)'
                     for i, ten in enumerate(xep_hang, 1)))

    print('\nB3 · Giới hạn lần chạy (chi phí simulated)')
    for k in (1, 2, 3):
        ket_qua = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_thanh_cong = len(reqs) - ket_qua['thanh_cong']
        ca_he_thong = ket_qua['tong'] + khong_thanh_cong * BASELINE
        print(f'{k} lần: trợ lý={ket_qua["tong"]:,.0f}đ, không thành công={khong_thanh_cong}, '
              f'cả hệ thống={ca_he_thong:,.0f}đ, cps={ket_qua["cps"]:,.0f}đ [simulated]')

    print('\nB4 · Xem lại 100% trong phạm vi noi_dia + hang_nang')
    run_pham_vi = runs[runs['request_id'].isin(pham_vi['request_id'])]
    co_ok = run_pham_vi.loc[run_pham_vi['status'] == 'ok', 'request_id'].nunique()
    so_lam_lai = (pham_vi['ket_qua'] == 'lam_lai').sum()
    tien_may = cp_pham_vi['token'] + cp_pham_vi['tool']
    phut_lam_lai_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    for phut_lam_lai in (9, phut_lam_lai_tb):
        tien_lam_lai = so_lam_lai * phut_lam_lai * LUONG_PHUT
        tong = tien_may + co_ok * 5 * LUONG_PHUT + tien_lam_lai
        cps = tong / cp_pham_vi['thanh_cong']
        phut_hoa_von = (BASELINE * cp_pham_vi['thanh_cong'] - tien_may - tien_lam_lai) / (co_ok * LUONG_PHUT)
        print(f'{co_ok} yêu cầu xem lại, {so_lam_lai} ca làm lại × {phut_lam_lai:.2f} phút: '
              f'cps={cps:,.0f}đ ({cps/BASELINE:.2f}×), '
              f'xem lại hoà vốn ≤{phut_hoa_von:.2f} phút [simulated]')

    print('\nD1 · Cỡ mẫu pilot (baseline 70%, alpha 5%, power 80%, ICC 0,02)')
    n5 = co_mau_hai_ti_le(0.70, 0.75)
    de75 = 1 + (75 - 1) * 0.02
    n_nhan_vien = math.ceil(n5 * de75 / 75)
    n6 = co_mau_hai_ti_le(0.70, 0.76)
    m6 = math.ceil(n6 * (1 - 0.02) / (20 - n6 * 0.02))
    de6 = 1 + (m6 - 1) * 0.02
    print(f'a) Theo yêu cầu, chênh 5 điểm: {n5:,} yêu cầu/nhóm')
    print(f'b) Theo nhân viên, m=75: DE={de75:.2f}, n={math.ceil(n5*de75):,} '
          f'yêu cầu/nhóm, {n_nhan_vien} nhân viên/nhóm '
          f'({2*n_nhan_vien} tổng > 40 hiện có)')
    print(f'c) 20 nhân viên/nhóm: n hiệu dụng tối đa={20/0.02:,.0f}/nhóm')
    print(f'd) 6 depot/nhóm: n hiệu dụng tối đa={6/0.02:,.0f}/nhóm')
    print(f'e) Chênh 6 điểm: n={n6:,}/nhóm, 20 nhân viên/nhóm cần '
          f'm≥{m6} yêu cầu/người, DE={de6:.2f}')
    print(f'Tỉ lệ mở lại 7 ngày hiện tại: {reqs["mo_lai_trong_7_ngay"].mean():.2%} '
          f'({reqs["mo_lai_trong_7_ngay"].sum()}/{len(reqs)}); '
          f'trong phạm vi={pham_vi["mo_lai_trong_7_ngay"].mean():.2%}')

    # Power khi tác động thật chỉ +5 điểm nhưng cỡ mẫu thiết kế cho +6 điểm.
    h = abs(2 * math.asin(math.sqrt(0.70)) - 2 * math.asin(math.sqrt(0.75)))
    z = h * math.sqrt(n6 / 2)
    nguong = NormalDist().inv_cdf(1 - 0.05 / 2)
    power5 = NormalDist().cdf(z - nguong) + NormalDist().cdf(-z - nguong)
    try:
        from statsmodels.stats.power import NormalIndPower
        from statsmodels.stats.proportion import proportion_effectsize
        power5 = NormalIndPower().power(
            effect_size=proportion_effectsize(0.70, 0.75), nobs1=n6,
            alpha=0.05, ratio=1.0)
    except ImportError:
        pass  # Cùng phép xấp xỉ chuẩn; dùng được cả khi chưa cài statsmodels.
    print(f'Power khi tác động thật +5 điểm với n={n6}/nhóm: {power5:.3f}')


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    in_bang(runs, reqs)
