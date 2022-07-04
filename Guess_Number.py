#this Tk for Game to Guess a random number
#This Program is Made to challenge myself, I call the program is One Day, One Program
#Program at June, 29, 2022
#Thank you

import tkinter as tk
import random 

random_number = random.randint(1, 99)
life = 10

def check_answer():
    number = int(enter_number.get())
    global random_number
    global life
    if number == random_number:
        text.set("Congrat, Your Guess Is Right")
        label_result.config
    elif life == 0 :
        text.set("Game Over, The Correct Number is :"+ str(random_number))
        label_result.config
    elif number > random_number:
        life -= 1
        text.set("Too High, Your remaining life :"+ str(life))
        label_result.config
    elif number < random_number:
        life -= 1
        text.set("Too Low, Your remaining life :"+ str(life))
        label_result.config


master = tk.Tk()
master.title("Guess a Random Number")
master.geometry("300x150")

label_direction =tk.Label(master, text="Guess a Number between 1 to 99")
label_direction.pack()

enter_number = tk.Entry(master)
enter_number.pack()

check_button= tk.Button(master, text="Check", command=check_answer)
check_button.pack()


text = tk.StringVar()
text.set("You Have 10 Life")

label_result=tk.Label(master,font=('Helvetica', 12, 'bold'),textvariable=text)
label_result.pack()


master.mainloop()


