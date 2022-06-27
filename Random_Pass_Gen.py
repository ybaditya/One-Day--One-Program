#program di buat tanggal 24-06-2022
#program di buat dalam rangka One Day, One :

import tkinter as tk
import random

def random_password():
    highAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowAlphabet = "abcdefghijklmnopqrstuvwxyz"
    number = "0123456789"
    symbol = "$%^&*?><!@#"
    allpass = highAlphabet + lowAlphabet + number + symbol
    length = int(e1.get())
    temp = random.sample(allpass, length)
    password ="".join(temp)
    text.set("Your Password : "+ str(password))
    l3.config


master = tk.Tk()
master.title("Tack Time Calculator")

l1=tk.Label(master, text="Enter Length of Password (Max : 20)")
e1=tk.Entry(master)

btn=tk.Button(master, text="GENERATE", command=random_password)

text = tk.StringVar()
text.set(" ")

l3=tk.Label(master,font=('Helvetica', 12, 'bold'),textvariable=text)

l1.grid(row=0, column=0)
e1.grid(row=0, column=1)
btn.grid(row=1, column=1)
l3.grid(row=2, column=1)

master.mainloop()


