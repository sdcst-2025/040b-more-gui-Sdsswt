import tkinter as tk
from tkinter import ttk
from tkinter import*

window = tk.Tk()
window.title("tk")
window.geometry("470x100")

entry1 = tk.Entry(window,text="Entry widgets can be typed in",)

label1 = tk.Label(window,text="Principle")
label1.place(x=15,y=10)

label1 = tk.Label(window,text="Intrest rate")
label1.place(x=165,y=10)

label1 = tk.Label(window,text="Years")
label1.place(x=315,y=10)

label1 = tk.Label(window,text="Amount")
label1.place(x=115,y=75)

entry1 = tk.Entry(window,text="")
entry1.place(x=15,y=30)

entry1 = tk.Entry(window,text="")
entry1.place(x=165,y=30)

entry1 = tk.Entry(window,text="")
entry1.place(x=165,y=75)

combobox1 = ttk.Combobox(window,text="")
combobox1.place(x=315,y=30)
window.mainloop()