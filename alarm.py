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

    img = ImageTk.PhotoImage(Image.open(r"C:\\Users\\Nikola Kostic\\Downloads\\digital_assistant_software_1.0-main\\templates\\alarm_template.png"))
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
    Hours.place(x=186, y=330)

    Minutes = Entry(root, font=("Century Gothic", 15), width=4)
    Minutes.place(x=300, y=330)

    Hours_Label = Label(root, text="Hrs : ", font=("Century Gothic", 20), fg="#fff", bg="#414141")
    Hours_Label.place(x=237, y=322)

    Minutes_Label = Label(root, text="Min", font=("Century Gothic", 20), fg="#fff", bg="#414141")
    Minutes_Label.place(x=352, y=322)

    def activate_alarm():
        Hours_Info = int(Hours.get())
        Minutes_Info = int(Minutes.get())
        while True:
            if Hours_Info == datetime.datetime.now().hour and Minutes_Info == datetime.datetime.now().minute:
                playsound("C:\\Users\\Nikola Kostic\\Downloads\\digital_assistant_software_1.0-main\\alarm.mp3")
                break

    #Add event

    add_event_path = r"C:\\Users\\Nikola Kostic\\Downloads\\digital_assistant_software_1.0-main\\buttons\\set_alarm.png"

    add_event_icon = ImageTk.PhotoImage(Image.open(add_event_path))
    add_event_button = tk.Button(root, image=add_event_icon, relief=FLAT, text="optional text", command=activate_alarm, bd=0)
    add_event_button.place(x=160, y=440)


    root.mainloop()
