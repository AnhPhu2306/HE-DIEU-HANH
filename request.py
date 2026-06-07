# Xu ly yeu cau cap tai nguyen (Request Resource)

from banker import kiem_tra_an_toan
from matrix import tinh_need


def yeu_cau_tai_nguyen(so_p, available, max_matrix, allocation, id_tien_trinh, yeu_cau):
    need = tinh_need(max_matrix, allocation)
    so_r = len(available)

    # Buoc 1: yeu cau khong duoc lon hon Need
    for j in range(so_r):
        if yeu_cau[j] > need[id_tien_trinh][j]:
            print("Loi: Yeu cau lon hon Need!")
            return False

    # Buoc 2: yeu cau khong duoc lon hon Available
    for j in range(so_r):
        if yeu_cau[j] > available[j]:
            print("Loi: Khong du tai nguyen!")
            return False

    # Luu lai de phuc hoi neu tu choi
    available_cu = available.copy()
    allocation_cu = allocation[id_tien_trinh].copy()

    # Buoc 3: thu cap tai nguyen
    for j in range(so_r):
        available[j] = available[j] - yeu_cau[j]
        allocation[id_tien_trinh][j] = allocation[id_tien_trinh][j] + yeu_cau[j]

    # Buoc 4: kiem tra he thong con an toan khong
    an_toan, chuoi = kiem_tra_an_toan(so_p, available, max_matrix, allocation)

    if an_toan == True:
        print("Chap nhan yeu cau!")
        print("Chuoi an toan:", chuoi)
        return True
    else:
        # Phuc hoi lai nhu cu
        for j in range(so_r):
            available[j] = available_cu[j]
            allocation[id_tien_trinh][j] = allocation_cu[j]
        print("Tu choi yeu cau! (He thong se khong an toan)")
        return False
