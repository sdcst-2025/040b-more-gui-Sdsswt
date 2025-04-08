import tkinter as tk
from tkinter import ttk
from tkinter import*

window = tk.Tk()
window.title("tk")
window.geometry("500x150")

entry1 = tk.Entry(window,text="Entry widgets can be typed in",)

label1 = tk.Label(window,text="principle")
label1.place(x=50,y=10)

label1 = tk.Label(window,text="intrest rate")
label1.place(x=200,y=10)

label1 = tk.Label(window,text="years")
label1.place(x=350,y=10)

label1 = tk.Label(window,text="amount")
label1.place(x=100,y=75)

entry1 = tk.Entry(window,text="")
entry1.place(x=50,y=30)

entry1 = tk.Entry(window,text="")
entry1.place(x=200,y=30)

entry1 = tk.Entry(window,text="")
entry1.place(x=150,y=75)

combobox1 = ttk.Combobox(window,text="")
combobox1.place(x=350,y=30)
window.mainloop()