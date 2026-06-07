# Giao dien don gian bang Tkinter

import os
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox

# Tao cua so chinh
cua_so = tk.Tk()
cua_so.title("Thuat toan Banker")
cua_so.geometry("500x350")
cua_so.configure(bg="lightblue")


def chay_chuong_trinh():
    # Mo main.py trong cua so console moi
    thu_muc = os.path.dirname(os.path.abspath(__file__))
    duong_dan = os.path.join(thu_muc, "main.py")
    subprocess.Popen([sys.executable, duong_dan], creationflags=subprocess.CREATE_NEW_CONSOLE)
    messagebox.showinfo("Thong bao", "Da mo chuong trinh!\nHay nhap du lieu o cua so console.")


def thoat():
    cua_so.destroy()


# Tieu de
nhan_tieu_de = tk.Label(cua_so, text="Mo phong thuat toan Banker", font=("Arial", 18, "bold"), bg="lightblue")
nhan_tieu_de.pack(pady=30)

nhan_mo_ta = tk.Label(cua_so, text="De tai: Giai quyet Deadlock\nHe dieu hanh", font=("Arial", 11), bg="lightblue")
nhan_mo_ta.pack(pady=10)

# Nut bam
nut_chay = tk.Button(cua_so, text="Chay chuong trinh", width=18, height=2, bg="green", fg="white", command=chay_chuong_trinh)
nut_chay.pack(pady=20)

nut_thoat = tk.Button(cua_so, text="Thoat", width=18, height=2, bg="red", fg="white", command=thoat)
nut_thoat.pack(pady=10)

cua_so.mainloop()
