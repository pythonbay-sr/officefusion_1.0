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
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf
import threading





#Calendar

def calendar():
    calendar = Toplevel()
    calendar.title("Calendar")
    calendar.geometry("1150x700")
    calendar.resizable(width=False, height=False)
    calendar.configure(bg="#323999")


    today = datetime.date.today()

    img = ImageTk.PhotoImage(Image.open(r"C:\\Users\\Nikola Kostic\\Downloads\\digital_assistant_software_1.0-main\\templates\\calendar_template.png"))
    panel = Label(calendar, image = img)
    panel.place(x=0, y=0)


    mindate = datetime.date(year=1900, month=1, day=1)
    maxdate = datetime.date(year=2100, month=1, day=1)


    #Entry Fields

    Title_Entry = Entry(calendar, font=("Century Gothic", 15), width=30)
    Title_Entry.place(x=620, y=250)

    Description_Entry = Text(calendar, font=("Century Gothic", 12), width=37, height=6)
    Description_Entry.place(x=619, y=360)


    Calendar_Interface_Label = Calendar(calendar, font=("Century Gothic", 15), selectmode='day', locale='en_US',
    mindate=mindate, maxdate=maxdate, disabledforeground='red', cursor="hand1", year=2021, month=9, day=21, fg="ffffff")
    Calendar_Interface_Label.place(x=180, y=220)


    def add_event():
        global date
        date = Calendar_Interface_Label.get_date()
        print(date)


        title = Title_Entry.get()
        location = r"C:\\Users\\Nikola Kostic\\Downloads\\digital_assistant_software_1.0-main\\tasks\\"
        path = (location + title + ".txt")
        description = Description_Entry.get(1.0, END)
        with open(path, 'w') as f:
            f.write(title)
            f.write(description)

    def do():
        x=0


    #Add event

    add_event_path = r"C:\\Users\\Nikola Kostic\\Downloads\\digital_assistant_software_1.0-main\\128.png"

    add_event_icon = ImageTk.PhotoImage(Image.open(add_event_path))
    add_event_button = tk.Button(calendar, image=add_event_icon, relief=FLAT, text="optional text", command=add_event, bd=0)
    add_event_button.place(x=215, y=540)


    #Open a event

    open_event_path = r"C:\\Users\\Nikola Kostic\\Downloads\\digital_assistant_software_1.0-main\\129.png"

    open_event_icon = ImageTk.PhotoImage(Image.open(open_event_path))
    open_event_button = tk.Button(calendar, image=open_event_icon, relief=FLAT, text="optional text", command=do, bd=0)
    open_event_button.place(x=580, y=540)


    calendar.mainloop()