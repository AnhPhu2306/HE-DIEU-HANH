# Tinh ma tran Need va in ra man hinh


def tinh_need(max_matrix, allocation):
    # Need[i][j] = Max[i][j] - Allocation[i][j]
    need = []
    for i in range(len(max_matrix)):
        dong = []
        for j in range(len(max_matrix[i])):
            gia_tri = max_matrix[i][j] - allocation[i][j]
            dong.append(gia_tri)
        need.append(dong)
    return need


def in_ma_tran(ten, ma_tran):
    print("\n" + ten)
    for i in range(len(ma_tran)):
        print("P" + str(i) + ":", ma_tran[i])


def in_available(available):
    print("\nAvailable:", available)


def hien_thi_tat_ca(available, max_matrix, allocation, need):
    print("\n===== CAC MA TRAN =====")
    in_available(available)
    in_ma_tran("Max", max_matrix)
    in_ma_tran("Allocation", allocation)
    in_ma_tran("Need", need)
