import numbers
import tkinter as tk

def check_answer():
    number = int(enter_number.get())
    if number > 1 :
        for i in range(2,number//2):
            if(number % i) == 0:
                enter_result.insert(0, str(number) + " is not a prime number")
                break
        else:
            enter_result.insert(0, str(number) + " is a prime number")
    else:
        enter_result.insert(0, str(number) + " is neither prime nor composite")


def reset_button():
    enter_result.delete(0, "end")


   

master = tk.Tk()
master.title("Prime Number Check!")
master.geometry("300x150")

label_direction =tk.Label(master, text="Enter a Number :")
label_direction.pack()
enter_number = tk.Entry(master)
enter_number.pack()
check_button= tk.Button(master, text="Check", command=check_answer)
check_button.pack()

label_direction2 =tk.Label(master, text="The Result : ")
label_direction2.pack()

enter_result = tk.Entry(master)
enter_result.pack()

reset_button= tk.Button(master, text="Reset", command=reset_button)
reset_button.pack()

master.mainloop()
