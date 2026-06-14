# Nhap du lieu cho thuat toan Banker


def nhap_du_lieu():
    print("===== NHAP DU LIEU =====")

    so_p = int(input("So tien trinh: "))
    so_r = int(input("So tai nguyen: "))

    print("Nhap Available (" + str(so_r) + " so, cach nhau bang dau cach):")
    available = list(map(int, input().split()))

    print("\nNhap ma tran Max:")
    max_matrix = []
    for i in range(so_p):
        print("P" + str(i) + ":", end=" ")
        dong = list(map(int, input().split()))
        max_matrix.append(dong)

    print("\nNhap ma tran Allocation:")
    allocation = []
    for i in range(so_p):
        print("P" + str(i) + ":", end=" ")
        dong = list(map(int, input().split()))
        allocation.append(dong)

    return so_p, so_r, available, max_matrix, allocation


def du_lieu_mau():
    # Vi du trong sach giao trinh: 5 tien trinh, 3 loai tai nguyen
    so_p = 5
    so_r = 3
    available = [3, 3, 2]
    max_matrix = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3],
    ]
    allocation = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2],
    ]
    # Tinh available = instances - tong(allocation)
    available = []
    for j in range(so_r):
        sum_alloc = sum(allocation[i][j] for i in range(so_p))
        available.append(instances[j] - sum_alloc)
    return so_p, so_r, available, max_matrix, allocation
