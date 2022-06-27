#program di buat tanggal 23-06-2022
#program di buat dalam rangka One Day, One :

import tkinter as tk


def cal_deposito():
    dana = float(e1.get())
    tenor = float(e2.get())
    bunga = float(e3.get())
    pajak = float(e4.get())

    besarbunga = dana*((bunga/100)/12)*tenor
    bungakenapajak = besarbunga-(besarbunga*(pajak/100))
    danatotal = dana + bungakenapajak
    text.set("Dana Total : IDR "+str(danatotal))
    lhasil.config


master = tk.Tk()
master.title("Tack Time Calculator")

l1=tk.Label(master, text="Dana Awal (IDR)")
l2=tk.Label(master, text="Tenor (Month)")
l3=tk.Label(master, text="Bunga/Tahun (%)")
l4=tk.Label(master, text="Pajak Deposito (%)")

e1=tk.Entry(master)
e2=tk.Entry(master)
e3=tk.Entry(master)
e4=tk.Entry(master)



btn=tk.Button(master, text="Calculate", command=cal_deposito)

text = tk.StringVar()
text.set(" ")

lhasil=tk.Label(master,font=('Helvetica', 12, 'bold'),textvariable=text)

l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
l3.grid(row=2, column=0)
l4.grid(row=3, column=0)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)

btn.grid(row=4, column=1)
lhasil.grid(row=5, column=1)

master.mainloop()


