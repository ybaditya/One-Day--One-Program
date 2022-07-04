import tkinter as tk
import pyshorteners

def check_answer():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(enter_url.get())
    enter_url2.insert(0, short_url)

   

master = tk.Tk()
master.title("Url Shorter")
master.geometry("300x150")

label_direction =tk.Label(master, text="Enter Long Url")
label_direction.pack()
enter_url = tk.Entry(master)
enter_url.pack()
check_button= tk.Button(master, text="Shorten Url", command=check_answer)
check_button.pack()
label_direction2 =tk.Label(master, text="Short Url Result")
label_direction2.pack()
enter_url2 = tk.Entry(master)
enter_url2.pack()

master.mainloop()
