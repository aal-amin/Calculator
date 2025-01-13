import tkinter as tk
from tkinter import ttk
from tkinter import font

root = tk.Tk()
root.title("calculator")
root.iconbitmap(r'C:\Users\User\Downloads\4564840793_c2614a717c_z_nmI_icon.ico')
root.geometry("269x500")
root.resizable(False, False)
root.configure(bg="#5A5C68")


def display(value):
    entry.insert(tk.END, value)


def btn_equel():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


text_value = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/", ".", "=", "%"]

entry = tk.Entry(root, background="#C1D798", font=("arial, 25"), justify="right", border=10)
entry.place(relx=0.03, rely=0.02, relheight=0.15, relwidth=0.94)

my_font = font.Font(family="Arial", size=20, weight="bold") 

tk.Button(root, text="C", font=my_font, background="Light Gray", bd=5, width=2, height=1, foreground="white", command=lambda: entry.delete(len(entry.get())-1, tk.END)).place(relx=0.05, y=140)
tk.Button(root, text="CL", font=my_font, background="Light Gray", bd=5, width=2, height=1, foreground="white", command=lambda:entry.delete(0, tk.END)).place(relx=0.29, y=140)
tk.Button(root, text=text_value[16], font=my_font, background="Light Gray", bd=5, width=2, height=1, foreground="white", command=lambda t = text_value[16]: display(t)).place(relx=0.53, y=140)
tk.Button(root, text=text_value[12], font=my_font, background="Light Gray", bd=5, width=2, height=1, foreground="white", command=lambda t = text_value[12]: display(t)).place(relx=0.77, y=140)

tk.Button(root, text=text_value[7], font=("Arial, 19"), background="#373B44", bd=4, width=2, height=1, foreground="white", command=lambda t = text_value[7]: display(t)).place(relx=0.05, rely=0.425)
tk.Button(root, text=text_value[8], font=("Arial, 19"), background="#373B44", bd=4, width=2, height=1, foreground="white", command=lambda t = text_value[8]: display(t)).place(relx=0.29, rely=0.425)
tk.Button(root, text=text_value[9], font=("Arial, 19"), background="#373B44", bd=4, width=2, height=1, foreground="white", command=lambda t = text_value[9]: display(t)).place(relx=0.53, rely=0.425)
tk.Button(root, text=text_value[13], font=my_font, background="Light Gray", bd=5, width=2, height=1, foreground="white", command=lambda t = text_value[13]: display(t)).place(relx=0.77, rely=0.425)

tk.Button(root, text=text_value[4], font=("Arial, 19"), background="#373B44", bd=4, width=2, height=1, foreground="white", command=lambda t = text_value[4]: display(t)).place(relx=0.05, rely=0.573)
tk.Button(root, text=text_value[5], font=("Arial, 19"), background="#373B44", bd=4, width=2, height=1, foreground="white", command=lambda t = text_value[5]: display(t)).place(relx=0.29, rely=0.573)
tk.Button(root, text=text_value[6], font=("Arial, 19"), background="#373B44", bd=4, width=2, height=1, foreground="white", command=lambda t = text_value[6]: display(t)).place(relx=0.53, rely=0.573)
tk.Button(root, text=text_value[10], font=my_font, background="Light Gray", bd=5, width=2, height=1, foreground="white", command=lambda t = text_value[10]: display(t)).place(relx=0.77, rely=0.573)

tk.Button(root, text=text_value[1], font=("Arial, 19"), background="#373B44", bd=4, width=2, height=1, foreground="white", command=lambda t = text_value[1]: display(t)).place(relx=0.05, rely=0.72)
tk.Button(root, text=text_value[2], font=("Arial, 19"), background="#373B44", bd=4, width=2, height=1, foreground="white", command=lambda t = text_value[2]: display(t)).place(relx=0.29, rely=0.72)
tk.Button(root, text=text_value[3], font=("Arial, 19"), background="#373B44", bd=4, width=2, height=1, foreground="white", command=lambda t = text_value[3]: display(t)).place(relx=0.53, rely=0.72)
tk.Button(root, text=text_value[11], font=my_font, background="Light Gray", bd=5, width=2, height=1, foreground="white", command=lambda t = text_value[11]: display(t)).place(relx=0.77, rely=0.72)

tk.Button(root, text=text_value[0], font=("Arial, 20"), background="#373B44", bd=4, width=6, height=1, foreground="white", command=lambda t = text_value[0]: display(t)).place(relx=0.05, rely=0.87)
tk.Button(root, text=text_value[14], font=("Arial, 19"), background="#373B44", bd=4, width=2, height=1, foreground="white", command=lambda t = text_value[14]: display(t)).place(relx=0.53, rely=0.87)
tk.Button(root, text=text_value[15], font=my_font, background="Light Gray", bd=5, width=2, height=1, foreground="white", command=btn_equel).place(relx=0.77, rely=0.87)


root.mainloop()