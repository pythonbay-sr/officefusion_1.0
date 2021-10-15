from tkcalendar import Calendar, DateEntry
import tkinter as tk
from tkinter import ttk
import datetime


def calendar_app():

    #Set up the program
    root = tk.Tk()
    root.title("Calendar")
    root.geometry("1200x700")
    root.resizable(width=False, height=False)

    today = datetime.date.today()
    mindate = datetime.date(year=2018, month=1, day=21)
    maxdate = today + datetime.timedelta(days=5)
    print(mindate, maxdate)

    cal = Calendar(root, font="Arial 14", selectmode='day', locale='en_US',
                    mindate=mindate, maxdate=maxdate, disabledforeground='red',
                    cursor="hand1", year=2018, month=2, day=5)
    cal.pack(fill="both", expand=True)


    #Root Mainloop

    root.mainloop()
