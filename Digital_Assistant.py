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
from alarm import alarm_app
from calendarr import calendar


#Set up the Program

root = tkinter.Tk()
root.title("Digital Assistant")
root.geometry("1300x800")
root.resizable(width=False, height=False)
root.configure(bg="#323999")


img1 = ImageTk.PhotoImage(Image.open(r"C:\\Users\\Nikola Kostic\\Downloads\\digital_assistant_software_1.0-main\\ls.jpg"))
panel = Label(root, image = img1)
panel.place(x=0, y=0)


#Clock

Clock_Label = Label(root, text="Clock", font=("Century Gothic", 20), fg="#fff", bg="#323999")
Clock_Label.place(x=930, y=70)


Clock = Label(root, font=('Century Gothic', 30), bg='#323999', fg="white")
Clock.place(x=890, y=110)

def tick():
    global time1
    time1 = ''
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        Clock.config(text=time2)
    Clock.after(200, tick)
tick()



def tasks_app():
    notes = tkinter.Toplevel()
    notes.title("Tasks")
    notes.geometry("1152x643")
    notes.resizable(width=False, height=False)
    notes.configure(bg="#323999")

    img = ImageTk.PhotoImage(Image.open(r"C:\\Users\\Nikola Kostic\\Downloads\\digital_assistant_software_1.0-main\\124.png"))
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
        #path = r"C:\\Users\\Nikola Kostic\\Downloads\\digital_assistant_software_1.0-main\\file.txt"
        path = filedialog.asksaveasfilename(filetypes = (("Text Files", "*.txt"), ("All Files", "*.*")))
        title = Title_Entry.get()
        text = Text_Entry.get()
        current_time = time.strftime('%H:%M:%S')
        with open(path, 'w') as f:
            f.write("Title of the task : ")
            f.write(title)
            f.write("\n")
            f.write("Description of the task : ")
            f.write(text)
            f.write("\n")
            f.write("Task created on : ")
            f.write(current_time)

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

    img = ImageTk.PhotoImage(Image.open(r"C:\\Users\\Nikola Kostic\\Downloads\\digital_assistant_software_1.0-main\\templates\\pdf_viewer_template.png"))
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
menubar.add_command(label="Calendar", command=calendar)
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


#Labels

Digital_Assistant_Label = Label(root, text="Office Fusion", font=("Century Gothic", 20), fg="#fff", bg="#3841c7", width=300)
Digital_Assistant_Label.pack(side='top')

Digital_Assistant_Label_2 = Label(root, text="Digital Assistant", font=("Century Gothic", 20), fg="#fff", bg="#3841c7")
Digital_Assistant_Label_2.place(x=250, y=80)

Help_Label = Label(root, text="How can I help you?", font=("Century Gothic", 20), fg="#000", bg="#fff")
Help_Label.place(x=250, y=120)

Answer_Label = Label(root, text="Answer : ", font=("Century Gothic", 20), fg="#fff", bg="#323999")
Answer_Label.place(x=45, y=260)


#Entry Fields

Text_Entry = Entry(root, font=("Century Gothic", 15), width=30)
Text_Entry.place(x=50, y=710)


#Show the answer

def show_answer():
    question = Text_Entry.get()
    if "time" in question:
        Time = Label(root, font=("Century Gothic", 20), fg="#fff", bg="#323999", text=time)
        Time.place(x=165, y=260)
    if "google" in question:
        webbrowser.open("www.google.com")
    if "netflix" in question:
        webbrowser.open("www.netflix.com")
    if "spotify" in question:
        webbrowser.open("www.spotify.com")
    if "apple" in question:
        webbrowser.open("www.apple.com")


def delete_answer():
    Text_Entry.delete(0, 'end')


#User Picture

img = ImageTk.PhotoImage(Image.open(r"C:\\Users\\Nikola Kostic\\Downloads\\digital_assistant_software_1.0-main\\logo.png"))
panel = Label(root, image = img, relief=FLAT)
panel.place(x=50, y=60)


#Buttons

Enter_Button = Button(root, text="Enter", font=("Century Gothic", 15),
                     fg="#fff", bg="#3841c7", width=10, command=show_answer, relief=FLAT)
Enter_Button.place(x=400, y=700)

Reset_Button = Button(root, text="Reset", font=("Century Gothic", 15),
                      fg="#fff", bg="#3841c7", width=10, command=delete_answer, relief=FLAT)
Reset_Button.place(x=550, y=700)









Calculator = Label(root, text="Calculator", font=('Century Gothic', 30), bg='#323999', fg="white")
Calculator.place(x=870, y=330)



# globally declare the expression variable
global expression
expression = "" 
    
    
# Function to update expressiom 
# in the text entry box 
def press(num): 
    # point out the global expression variable 
    global expression 
    
    # concatenation of string 
    expression = expression + str(num) 
    
    # update the expression by using set method 
    equation.set(expression)
        
    
def equalpress(): 
    try: 
    
        global expression 
        total = str(eval(expression)) 
        equation.set(total) 
        expression = "" 
    
    # if error is generate then handle 
    # by the except block 
    except: 
    
        equation.set(" error ") 
        expression = "" 
    

def clear(): 
    global expression 
    expression = "" 
    equation.set("") 


equation = StringVar()
expression_field = Entry(root, textvariable=equation, width=32, font=("Century Gothic", 15))
expression_field.place(x=800, y=408)
equation.set('0')


#Buttons

button1 = Button(root, text=' 1 ', fg='#3841c7', bg='#fff', font=("Century Gothic", 20), command=lambda: press(1), height=1, width=5) 
button1.place(x=800, y=610)

button2 = Button(root, text=' 2 ', fg='#3841c7', bg='#fff', font=("Century Gothic", 20), command=lambda: press(2), height=1, width=5) 
button2.place(x=890, y=610)

button3 = Button(root, text=' 3 ', fg='#3841c7', bg='#fff', font=("Century Gothic", 20), command=lambda: press(3), height=1, width=5) 
button3.place(x=980, y=610)

button4 = Button(root, text=' 4 ', fg='#3841c7', bg='#fff', font=("Century Gothic", 20), command=lambda: press(4), height=1, width=5) 
button4.place(x=800, y=552)

button5 = Button(root, text=' 5 ', fg='#3841c7', bg='#fff', font=("Century Gothic", 20), command=lambda: press(5), height=1, width=5) 
button5.place(x=890, y=552)

button6 = Button(root, text=' 6 ', fg='#3841c7', bg='#fff', font=("Century Gothic", 20), command=lambda: press(6), height=1, width=5) 
button6.place(x=980, y=552)

button7 = Button(root, text=' 7 ', fg='#3841c7', bg='#fff', font=("Century Gothic", 20), command=lambda: press(7), height=1, width=5) 
button7.place(x=800, y=494)

button8 = Button(root, text=' 8 ', fg='#3841c7', bg='#fff', font=("Century Gothic", 20), command=lambda: press(8), height=1, width=5) 
button8.place(x=890, y=494)

button9 = Button(root, text=' 9 ', fg='#3841c7', bg='#fff', font=("Century Gothic", 20), command=lambda: press(9), height=1, width=5) 
button9.place(x=980, y=494)

button0 = Button(root, text=' 0 ', fg='#3841c7', bg='#fff', font=("Century Gothic", 20),command=lambda: press(0), height=1, width=5) 
button0.place(x=890, y=668)


button_dot = Button(root, text=' . ', fg='#fff', bg='#3841c7', font=("Century Gothic", 20),
                    command=lambda: press(1), height=1, width=5) 
button_dot.place(x=980, y=436)


button_equal = Button(root, text=' = ', fg='#fff', bg='#3841c7', font=("Century Gothic", 20),
                    command=equalpress, height=1, width=5) 
button_equal.place(x=890, y=436)


button_plus = Button(root, text=' + ', fg='#fff', bg='#3841c7', font=("Century Gothic", 20),
                    command=lambda: press("+"), height=1, width=5) 
button_plus.place(x=1070, y=436)


button_minus = Button(root, text=' - ', fg='#fff', bg='#3841c7', font=("Century Gothic", 20),
                    command=lambda: press("-"), height=1, width=5) 
button_minus.place(x=1070, y=494)


button_multiply = Button(root, text=' * ', fg='#fff', bg='#3841c7', font=("Century Gothic", 20),
                    command=lambda: press("*"), height=1, width=5) 
button_multiply.place(x=1070, y=552)


button_divide = Button(root, text=' / ', fg='#fff', bg='#3841c7', font=("Century Gothic", 20),
                    command=lambda: press("/"), height=1, width=5) 
button_divide.place(x=1070, y=610)


button_CE = Button(root, text=' CE ', fg='#fff', bg='#3841c7', font=("Century Gothic", 20),
                    command=clear, height=1, width=5) 
button_CE.place(x=800, y=436)


#Root Mainloop

root.mainloop()
