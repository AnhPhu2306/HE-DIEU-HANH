# Chuong trinh chinh - Mo phong thuat toan Banker
# De tai: Giai quyet deadlock bang thuat toan Banker

from input_data import nhap_du_lieu, du_lieu_mau
from matrix import tinh_need, hien_thi_tat_ca
from banker import kiem_tra_an_toan
from request import yeu_cau_tai_nguyen


def main():
    print("===== THUAT TOAN BANKER =====")
    print("1 - Nhap tay")
    print("2 - Dung du lieu mau")
    chon = input("Chon (mac dinh 2): ")

    if chon == "1":
        so_p, so_r, available, max_matrix, allocation = nhap_du_lieu()
    else:
        so_p, so_r, available, max_matrix, allocation = du_lieu_mau()
        print("Dang dung du lieu mau.")

    # --- Tinh va in ma tran Need ---
    need = tinh_need(max_matrix, allocation)
    hien_thi_tat_ca(available, max_matrix, allocation, need)

    # --- Kiem tra an toan ---
    print("\n===== KIEM TRA AN TOAN =====")
    an_toan, chuoi = kiem_tra_an_toan(so_p, available, max_matrix, allocation)

    if an_toan == True:
        print("Ket qua: HE THONG AN TOAN (SAFE)")
        print("Chuoi an toan:", chuoi)
    else:
        print("Ket qua: HE THONG KHONG AN TOAN (UNSAFE)")

    # ---  Yeu cau tai nguyen (neu muon) ---
    print("\n===== YEU CAU TAI NGUYEN =====")
    co_yc = input("Ban co muon yeu cau tai nguyen khong? (y/n): ")

    if co_yc == "y" or co_yc == "Y":
        id_tt = int(input("Nhap ID tien trinh (0 den " + str(so_p - 1) + "): "))
        print("Nhap yeu cau (" + str(so_r) + " so, cach nhau bang dau cach):")
        yeu_cau = list(map(int, input().split()))

        print("\nDang xu ly yeu cau cua P" + str(id_tt) + ":", yeu_cau)
        ket_qua = yeu_cau_tai_nguyen(so_p, available, max_matrix, allocation, id_tt, yeu_cau)

        if ket_qua == True:
            need = tinh_need(max_matrix, allocation)
            print("\n===== SAU KHI CAP TAI NGUYEN =====")
            hien_thi_tat_ca(available, max_matrix, allocation, need)

    print("\n===== HET CHUONG TRINH =====")


if __name__ == "__main__":
    main()
#py main.py      # chạy console
#py gui.py       # chạy giao diện
