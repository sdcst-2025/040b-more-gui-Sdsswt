import tkinter as tk
from tkinter import ttk
from tkinter import*

window = tk.Tk()
window.title("")
window.geometry("650x600")

logo = PhotoImage(file="logo.png")
photo3 = tk.Label(window, image=logo)
photo3.place(x=250,y=500)

minimapimage = PhotoImage(file="main.png")
photo1 = tk.Label(window, image=minimapimage)
photo1.place(x=1,y=25)

pokemonimage = PhotoImage(file="minimap.png")
photo2 = tk.Label(window, image=pokemonimage)
photo2.place(x=515,y=75)

label1 = tk.Label(window,text="POKEMON ADVENTURES")
label1.place(x=250,y=1)

label1 = tk.Label(window,text="MINI MAP")
label1.place(x=525,y=50)

button = tk.Button(window,text="N ",height = 1, width = 2)
button.place(x=40,y=500)

button = tk.Button(window,text="NE",height = 1, width = 2)
button.place(x=65,y=500)

button = tk.Button(window,text="E",height = 1, width = 2)
button.place(x=65,y=525)

button = tk.Button(window,text="SE",height = 1, width = 2)
button.place(x=65,y=550)

button = tk.Button(window,text="S ",height = 1, width = 2)
button.place(x=40,y=550)

button = tk.Button(window,text="SW",height = 1, width = 2)
button.place(x=15,y=550)

button = tk.Button(window,text="W ",height = 1, width = 2)
button.place(x=15,y=525)

button = tk.Button(window,text="NW",height = 1, width = 2)
button.place(x=15,y=500)

buttonMap = tk.Button(window,text="MAP",height = 2, width = 12)
buttonMap.place(x=520,y=185)

buttonMap = tk.Button(window,text="INVENTORY",height = 2, width = 12)
buttonMap.place(x=520,y=225)

buttonMap = tk.Button(window,text="POKEDEX",height = 2, width = 12)
buttonMap.place(x=520,y=265)

buttonMap = tk.Button(window,text="ROSTER",height = 2, width = 12)
buttonMap.place(x=520,y=305)

buttonMap = tk.Button(window,text="JOURNAL",height = 2, width = 12)
buttonMap.place(x=520,y=345)

buttonMap = tk.Button(window,text="HELP",height = 2, width = 12)
buttonMap.place(x=520,y=385)

buttonMap = tk.Button(window,text="SHOP",height = 2, width = 12)
buttonMap.place(x=520,y=425)

window.mainloop()