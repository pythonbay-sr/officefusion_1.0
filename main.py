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
from playsound import playsound
from weather import weather_app
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf
import threading
from alarm import alarm_app
from datepicker import calendar_app
import os

general_path = os.getcwd().replace("\\", r"\\")


#Set up the Program

root = tkinter.Tk()
root.title("Office Fusion")
root.geometry("1440x900")
root.resizable(width=False, height=False)
root.configure(bg="#323999")


img1 = ImageTk.PhotoImage(Image.open(general_path + r"\\Downloads\\digital_assistant_software_1.0-main\\templates\\main_template.png"))
panel = Label(root, image = img1)
panel.place(x=0, y=0)



def tasks_app():
    notes = tkinter.Toplevel()
    notes.title("Tasks")
    notes.geometry("1152x643")
    notes.resizable(width=False, height=False)
    notes.configure(bg="#323999")

    img = ImageTk.PhotoImage(Image.open(general_path + r"\\Downloads\\digital_assistant_software_1.0-main\\templates\\tasks_template.png"))
    panel = Label(notes, image = img)
    panel.place(x=0, y=0)

    Title_Label = Label(notes, text="Title : ", font=("Century Gothic", 20), fg="#fff", bg="#323999")
    Title_Label.place(x=350, y=280)

    Text_Label = Label(notes, text="Text : ", font=("Century Gothic", 20), fg="#fff", bg="#323999")
    Text_Label.place(x=350, y=350)

    Title_Entry = Entry(notes, font=("Century Gothic", 15), width=30)
    Title_Entry.place(x=450, y=280)

    Text_Entry = Entry(notes, font=("Century Gothic", 15), width=30)
    Text_Entry.place(x=450, y=350)


    def add_task():
        title = Title_Entry.get()
        text = Text_Entry.get()
        current_time = time.strftime('%H:%M:%S')

        location = general_path + r"\\Downloads\\digital_assistant_software_1.0-main\\tasks\\"
        path = (location + title + ".txt")

        with open(path, 'w') as f:
            f.write("Title : " + title + "\n")
            f.write("Description : " + text)
            f.write("Time : " + current_time + "\n")

    Add_Note_Button = Button(notes, text="Add a Task", font=("Century Gothic", 15),
                     fg="#fff", bg="#3841c7", width=10, command=add_task, relief=FLAT)
    Add_Note_Button.place(x=500, y=500)

    notes.mainloop()


#PDF Viewer

def pdf_viewer():
    top = Toplevel(root)
    top.title("PDF Viewer")
    top.geometry("1230x860")
    top.resizable(width=False, height=False)
    top.configure(bg="#323999")
      

    #PDF Viewer Template

    img = ImageTk.PhotoImage(Image.open(general_path + r"\\Downloads\\digital_assistant_software_1.0-main\\templates\\pdf_viewer_template.png"))
    panel = Label(top, image = img)
    panel.place(x=0, y=0)


    #Ask for a .pdf file, and then display it

    fileName = filedialog.askopenfilename(filetypes = (("png files", "*.png"), ("All Files", "*.*")))
    v1 = pdf.ShowPdf()
    v2 = v1.pdf_view(top, pdf_location = fileName, width = 80, height = 40)
    v2.place(x=303, y=190)

    #top Mainloop

    top.mainloop()



#Menu Bar

menubar = Menu(root)
menubar.add_command(label="File")
menubar.add_command(label="Alarm", command=alarm_app)
menubar.add_command(label="Calendar", command=calendar_app)
menubar.add_command(label="Weather", command=weather_app)
menubar.add_command(label="Tasks", command=tasks_app)
menubar.add_command(label="PDF Viewer", command=pdf_viewer)
#command=threading.Thread(target=pdf_viewer).start()

root.config(menu=menubar)


#Close the window

def close_window():
    response = messagebox.askquestion("Exit the Program", "Do you really want to exit the program?")
    if response == 'yes':
        root.destroy()
    else:
        pass


today = datetime.date.today()

mindate = datetime.date(year=1900, month=1, day=1)
maxdate = datetime.date(year=2100, month=1, day=1)


#Entry Fields

Title_Entry = Entry(root, font=("Century Gothic", 15), width=30)
Title_Entry.place(x=755, y=280)

Description_Entry = Text(root, font=("Century Gothic", 12), width=37, height=6)
Description_Entry.place(x=755, y=395)

People_Entry = Entry(root, font=("Century Gothic", 15), width=30)
People_Entry.place(x=755, y=613)


Calendar_Interface_Label = Calendar(root, font=("Century Gothic", 15), selectmode='day', locale='en_US',
mindate=mindate, maxdate=maxdate, disabledforeground='red', cursor="hand1", year=2021, month=9, day=21, fg="ffffff")
Calendar_Interface_Label.place(x=300, y=340)


def add_event():
    global date
    date = Calendar_Interface_Label.get_date()

    title = Title_Entry.get()
    description = Description_Entry.get(1.0, END)
    people = People_Entry.get()

    location = general_path + r"\\Downloads\\digital_assistant_software_1.0-main\\projects\\"
    path = (location + title + ".txt")

    with open(path, 'w') as f:
        f.write("Title : " + title + "\n")
        f.write("Description : " + description)
        f.write("People : " + people + "\n")


def open_events():
    path = general_path + r"\\Downloads\\digital_assistant_software_1.0-main\\projects" + "\\events.txt"
    os.startfile(path)


#Add event

add_event_path = general_path + r"\\Downloads\\digital_assistant_software_1.0-main\\buttons\\add_event.png"

add_event_icon = ImageTk.PhotoImage(Image.open(add_event_path))
add_event_button = tk.Button(root, image=add_event_icon, relief=FLAT, text="optional text", command=add_event, bd=0)
add_event_button.place(x=750, y=670)


#Open a event

open_event_path = general_path + r"\\Downloads\\digital_assistant_software_1.0-main\\buttons\\open_event.png"

open_event_icon = ImageTk.PhotoImage(Image.open(open_event_path))
open_event_button = tk.Button(root, image=open_event_icon, relief=FLAT, text="optional text", command=open_events, bd=0)
open_event_button.place(x=315, y=670)


#Root Mainloop

root.mainloop()
