import tkinter as tk
from tkinter import messagebox

from main import main

def run_program():
    try:
        main()

        messagebox.showinfo(
            "Thong bao",
            "Chuong trinh da chay xong!"
        )

    except Exception as e:
        messagebox.showerror(
            "Loi",
            str(e)
        )

def exit_program():
    window.destroy()

window = tk.Tk()

window.title("Deadlock Banker Algorithm")
window.geometry("600x400")
window.configure(bg="#EAF4FF")

title = tk.Label(
    window,
    text="Deadlock - Banker Algorithm",
    font=("Arial", 20, "bold"),
    bg="#EAF4FF",
    fg="#003366"
)

title.pack(pady=30)

description = tk.Label(
    window,
    text="Operating System Project\nBanker's Algorithm Simulation",
    font=("Arial", 12),
    bg="#EAF4FF"
)

description.pack(pady=10)

run_button = tk.Button(
    window,
    text="Run Program",
    width=20,
    height=2,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12),
    command=run_program
)

run_button.pack(pady=20)

exit_button = tk.Button(
    window,
    text="Exit",
    width=20,
    height=2,
    bg="#D9534F",
    fg="white",
    font=("Arial", 12),
    command=exit_program
)

exit_button.pack(pady=10)

window.mainloop()