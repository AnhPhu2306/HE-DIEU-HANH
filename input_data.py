# file nhap du lieu cho thuat toan Banker


def nhap_du_lieu():
    print("===== NHAP DU LIEU HE THONG =====")

    so_p = int(input("Nhap so tien trinh: "))
    so_r = int(input("Nhap so tai nguyen: "))

    # Available: tai nguyen con trong he thong
    print("\nNhap Available (", so_r, "so, cach nhau bang dau cach):")
    available = list(map(int, input().split()))

    # Max: so tai nguyen toi da ma moi tien trinh can
    print("\nNhap ma tran Max:")
    max_matrix = []
    for i in range(so_p):
        print("P", i, end=": ")
        dong = list(map(int, input().split()))
        max_matrix.append(dong)

    # Allocation: tai nguyen da cap cho tung tien trinh
    print("\nNhap ma tran Allocation:")
    allocation = []
    for i in range(so_p):
        print("P", i, end=": ")
        dong = list(map(int, input().split()))
        allocation.append(dong)

    return so_p, so_r, available, max_matrix, allocation


def du_lieu_mau():
    # vi du trong sach: 5 tien trinh, 3 tai nguyen
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
    return so_p, so_r, available, max_matrix, allocation
