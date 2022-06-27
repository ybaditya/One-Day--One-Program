#This Tk for Calculate BMI use Tkinter
#This Program is Made to challenge myself, I call the program is One Day, One Program
#Program at June, 26, 2022
#Thank you

import tkinter as tk


def cal_bmi():
    height = int(e1.get())
    weight = int(e2.get())
    BMI = weight / int((height/100)**2)

    if BMI < 18.5 :
        text.set("Your BMI Index: " + str(BMI) + " UnderWeight")
        lhasil.config
    elif BMI > 18.5 and BMI < 24.9 :
        text.set("Your BMI Index: " + str(BMI) + " Normal")
        lhasil.config
    elif BMI > 25 and BMI < 29.9 :
        text.set("Your BMI Index: " + str(BMI) + " OverWeight")
        lhasil.config   
    elif BMI > 30 :
        text.set("Your BMI Index: " + str(BMI) + " very OverWeight")
        lhasil.config   
    else :
        text.set("Wrong Format")
        lhasil.config   

master = tk.Tk()
master.title("BMI Calculator")

l1=tk.Label(master, text="Enter Your Height (Cm)")
l2=tk.Label(master, text="Enter Your Weight (Kg)")

e1=tk.Entry(master)
e2=tk.Entry(master)


btn=tk.Button(master, text="Calculate", command=cal_bmi)

text = tk.StringVar()
text.set(" ")

lhasil=tk.Label(master,font=('Helvetica', 12, 'bold'),textvariable=text)

l1.grid(row=0, column=0)
l2.grid(row=1, column=0)


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

btn.grid(row=2, column=1)
lhasil.grid(row=3, column=1)

master.mainloop()


