# chuong trinh chinh: nhap -> tinh Need -> in ra
# de tai: deadlock, thuat toan Banker

from input_data import nhap_du_lieu, du_lieu_mau
from matrix import tinh_need, hien_thi_tat_ca


def main():
    print("De tai: Deadlock - Thuat toan Banker")
    print("Buoc 1: nhap du lieu, tinh ma tran Need\n")

    chon = input("1: nhap tay | 2: dung du lieu mau (1): ")
    if chon == "2":
        so_p, so_r, available, max_matrix, allocation = du_lieu_mau()
        print("Dang dung du lieu mau.")
    else:
        so_p, so_r, available, max_matrix, allocation = nhap_du_lieu()

    need = tinh_need(max_matrix, allocation)
    hien_thi_tat_ca(available, max_matrix, allocation, need)

    print("\nXong! Da tinh xong ma tran Need.")


if __name__ == "__main__":
    main()
