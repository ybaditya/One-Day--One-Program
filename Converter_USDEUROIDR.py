#This Tk for Calculate USD to IDR, USD to EURO
#This Program is Made to challenge myself, I call the program is One Day, One Program
#Program at June, 21, 2022
#Thank you

import tkinter as tk

def usd_to_idr():
    angka1 = textbox.get()
    dollar = float(angka1)*14500
    text.set("Rp. " + str(dollar))
    label2.config(font=('Helvetica', 15, 'bold'), fg="green")

def usd_to_euro():
    angka2 = textbox.get()
    euro = float(angka2)*0.95
    text.set("EUR. " + str(euro))
    label2.config(font=('Helvetica', 15, 'bold'), fg="green")


window = tk.Tk()
window.title("USD to IDR Converter")
window.geometry("800x300")

label1=tk.Label(window,text="USD",font=('Helvetica', 12, 'bold'))
label1.pack()

textbox=tk.Entry(window,font=('Helvetica', 12, 'bold'),width=5,justify=tk.CENTER)
textbox.pack()

btn1=tk.Button(window, text="TO IDR", command=usd_to_idr)
btn1.pack()

btn2=tk.Button(window, text="TO EURO", command=usd_to_euro)
btn2.pack()

text = tk.StringVar()
text.set("IDR")

label2=tk.Label(window,font=('Helvetica', 12, 'bold'),textvariable=text)
label2.pack()

window.mainloop()

