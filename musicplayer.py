from pygame import mixer
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import filedialog

#Main Screen
master = Tk()
master.title("Music Player")

#Labels
Label(master,text="Custom Music Player",font=("Calibri",15),fg="red").grid(sticky="N",row=0,padx=120)
Label(master,text="Please Select Music Track",font=("Calibri",12),fg="blue").grid(sticky="N",row=1)

master.mainloop()