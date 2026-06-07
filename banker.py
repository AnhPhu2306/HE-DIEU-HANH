# Thuat toan kiem tra an toan (Safety Algorithm)

from matrix import tinh_need


def kiem_tra_an_toan(so_p, available, max_matrix, allocation):
    need = tinh_need(max_matrix, allocation)
    so_r = len(available)

    # finish[i] = True nghia la tien trinh Pi da chay xong
    finish = []
    for i in range(so_p):
        finish.append(False)

    chuoi_an_toan = []
    work = available.copy()  # tai nguyen con lai khi mo phong

    # Lap den khi tim du tat ca tien trinh
    while len(chuoi_an_toan) < so_p:
        tim_duoc = False

        for i in range(so_p):
            if finish[i] == True:
                continue

            # Kiem tra Need[i] <= Work khong
            du_dieukien = True
            for j in range(so_r):
                if need[i][j] > work[j]:
                    du_dieukien = False
                    break

            if du_dieukien == True:
                # Pi chay xong, tra lai tai nguyen
                for j in range(so_r):
                    work[j] = work[j] + allocation[i][j]
                chuoi_an_toan.append(i)
                finish[i] = True
                tim_duoc = True

        # Khong tim duoc tien trinh nao thi he thong khong an toan
        if tim_duoc == False:
            return False, []

    return True, chuoi_an_toan
