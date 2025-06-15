import tkinter as tk
from tkinter import messagebox

def click(event):
    current = str(entry.get())
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")
            entry.delete(0, tk.END)
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

entry = tk.Entry(root, font="Arial 20", bd=5, relief=tk.RIDGE, justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

btns_frame = tk.Frame(root)
btns_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    row_frame = tk.Frame(btns_frame)
    row_frame.pack(expand=True, fill="both")
    for btn in row:
        b = tk.Button(row_frame, text=btn, font="Arial 18", relief=tk.GROOVE)
        b.pack(side="left", expand=True, fill="both", padx=2, pady=2)
        b.bind("<Button-1>", click)

root.mainloop()
