# tinh Need va in cac ma tran


def tinh_need(max_matrix, allocation):
    # cong thuc: Need = Max - Allocation
    need = []
    for i in range(len(max_matrix)):
        dong = []
        for j in range(len(max_matrix[i])):
            dong.append(max_matrix[i][j] - allocation[i][j])
        need.append(dong)
    return need


def in_ma_tran(ten, ma_tran):
    print("\n", ten)
    for i in range(len(ma_tran)):
        print("P", i, ":", ma_tran[i])


def in_available(available):
    print("\n Available:", available)


def hien_thi_tat_ca(available, max_matrix, allocation, need):
    print("\n===== KET QUA CAC MA TRAN =====")
    in_available(available)
    in_ma_tran("Max", max_matrix)
    in_ma_tran("Allocation", allocation)
    in_ma_tran("Need (Max - Allocation)", need)
