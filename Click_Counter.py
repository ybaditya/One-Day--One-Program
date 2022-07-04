#This Tk for Click and Count use Tkinter
#This Program is Made to challenge myself, I call the program is One Day, One Program
#Program at June, 28, 2022
#Thank you

import tkinter as tk

count=0

def cal_add():
    global count
    count += 1
    text.set("Your Counter : "+ str(count))
    lhasil.config

def cal_minus():
    global count
    count -= 1
    text.set("Your Counter : "+ str(count))
    lhasil.config

def cal_double():
    global count
    count *= 2
    text.set("Your Counter : "+ str(count))
    lhasil.config


master = tk.Tk()
master.title("Click to Increase Count")
master.geometry("300x300")

btn=tk.Button(master, text="Click +1", command=cal_add)
btn.pack()

btn=tk.Button(master, text="Click -1", command=cal_minus)
btn.pack()

btn=tk.Button(master, text="Click x2", command=cal_double)
btn.pack()


text = tk.StringVar()
text.set("0")

lhasil=tk.Label(master,font=('Helvetica', 12, 'bold'),textvariable=text)
lhasil.pack()


master.mainloop()


