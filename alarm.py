import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import tkinter as tk
from datetime import datetime
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import datetime
import time
import webbrowser
from playsound import playsound
import math
from weather import weather_app
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf
import threading



def alarm_app():
    root = tkinter.Toplevel()
    root.title("Alarm")
    root.geometry("1152x700")
    root.resizable(width=False, height=False)
    root.configure(bg="#323999")


    #Template (background image)

    img = ImageTk.PhotoImage(Image.open(r"C:\\Users\\Nikola Kostic\\Downloads\\digital_assistant_software_1.0-main\\alarm_template.png"))
    panel = Label(root, image = img)
    panel.place(x=0, y=0)




    Clock = Label(root, font=('Century Gothic', 40), bg='#414141', fg="white")
    Clock.place(x=770, y=330)

    def tick():
        global time1
        time1 = ''
        time2 = time.strftime('%H:%M:%S')
        if time2 != time1:
            time1 = time2
            Clock.config(text=time2)
        Clock.after(200, tick)
    tick()

        
    Hours = Entry(root, font=("Century Gothic", 15), width=4)
    Hours.place(x=150, y=350)

    Minutes = Entry(root, font=("Century Gothic", 15), width=4)
    Minutes.place(x=300, y=350)

    Hours_Label = Label(root, text="Hrs", font=("Century Gothic", 20), fg="#fff", bg="#414141")
    Hours_Label.place(x=200, y=350)

    Minutes_Label = Label(root, text="Min", font=("Century Gothic", 20), fg="#fff", bg="#414141")
    Minutes_Label.place(x=350, y=350)

    def activate_alarm():
        xx = Hours_Info = int(Hours.get())
        yy = Minutes_Info = int(Minutes.get())
        while True:
            if Hours_Info == datetime.datetime.now().hour and Minutes_Info == datetime.datetime.now().minute:
                playsound("C:\\Users\\Nikola Kostic\\Downloads\\digital_assistant_software_1.0-main\\alarm.mp3")
                break

    Enter_Buttonn = Button(root, text="Enter", font=("Century Gothic", 15),
    fg="#fff", bg="#3841c7", width=10, command = activate_alarm, relief=FLAT)
    Enter_Buttonn.place(x=135, y=500)


    root.mainloop()
