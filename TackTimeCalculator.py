#program di buat tanggal 22-06-2022
#program di buat dalam rangka One Day, One :

import tkinter as tk


def cal_tacktime():
    avail = float(e1.get())
    volume = float(e2.get())
    tacktime = (avail*60*60*20.5) / volume
    text.set("Tack Time Result : "+str(tacktime)+ "Second")
    l3.config


master = tk.Tk()
master.title("Tack Time Calculator")

l1=tk.Label(master, text="Available Time (Hour/Day)")
l2=tk.Label(master, text="Volume (Pcs/Month)")
e1=tk.Entry(master)
e2=tk.Entry(master)

btn=tk.Button(master, text="Calculate", command=cal_tacktime)

text = tk.StringVar()
text.set(" ")

l3=tk.Label(master,font=('Helvetica', 12, 'bold'),textvariable=text)

l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
btn.grid(row=2, column=1)
l3.grid(row=3, column=1)

master.mainloop()




