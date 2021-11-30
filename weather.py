import requests, json
import tkinter
from tkinter import *
from PIL import ImageTk, Image
import pyglet
import os

general_path = os.getcwd().replace("\\", r"\\")


def weather_app():
    #Set up the Program

    root = tkinter.Toplevel()
    root.title("Weather")
    root.geometry("1152x700")
    root.resizable(width=False, height=False)
    root.configure(bg="#323999")


    #Template (background image)

    img = ImageTk.PhotoImage(Image.open(general_path + r"\\Downloads\\digital_assistant_software_1.0-main\\templates\\weather_template.png"))
    panel = Label(root, image = img)
    panel.place(x=0, y=0)


    #Insert the font

    pyglet.font.add_file(general_path + r"\\Downloads\\digital_assistant_software_1.0-main\\Poppins-Regular.ttf")


    #OpenWeather API

    def check():
        
        #API base URL
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

        #City name input
        CITY = Text_Entry.get()

        #API key
        API_KEY = "63b6494c53ed8a38142f66dfd26eb59f"

        #Updating the URL
        URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

        #Sending the HTTP request
        response = requests.get(URL)

        #Checking the status code of the request
        if response.status_code == 200:

            data = response.json()
            main = data['main']
            temperature = main['temp']
            temp_feel_like = main['feels_like']  
            humidity = main['humidity']
            pressure = main['pressure']
            weather_report = data['weather']
            wind_report = data['wind']
            
            City_Label = Label(root, text=(f"City : {CITY}") , font=("Poppins", 20), fg="#fff", bg="#A5A8B0")
            City_Label.place(x=210, y=180)

            Temperature_Label = Label(root, text=(f"Temperature : {int(temperature-273)}")+"°C", font=("Poppins", 20), fg="#fff", bg="#A5A8B0")
            Temperature_Label.place(x=210, y=230)

            Feels_Like_Label = Label(root, text=(f"Feels like : {int(temp_feel_like-273)}")+"°C", font=("Poppins", 20), fg="#fff", bg="#A5A8B0")
            Feels_Like_Label.place(x=210, y=280)

            Humidity_Label = Label(root, text=(f"Humidity : {humidity}")+"%", font=("Poppins", 20), fg="#fff", bg="#A5A8B0")
            Humidity_Label.place(x=210, y=330)

            Pressure_Label = Label(root, text=(f"Pressure : {pressure}")+"hPa", font=("Poppins", 20), fg="#fff", bg="#A5A8B0")
            Pressure_Label.place(x=520, y=180)

            Weather_Report_Label = Label(root, text=(f"Weather Report : {weather_report[0]['description']}"), font=("Poppins", 20), fg="#fff", bg="#A5A8B0")
            Weather_Report_Label.place(x=520, y=230)

            Wind_Speed_Label = Label(root, text=(f"Wind Speed : {wind_report['speed']}")+"m/s", font=("Poppins", 20), fg="#fff", bg="#A5A8B0")
            Wind_Speed_Label.place(x=520, y=280)
        else:
            #Error message
            print("Error in the HTTP request")


    #City Question Label

    City_Question_Label = Label(root, text="Enter the name of the city : " , font=("Poppins", 20), fg="#fff", bg="#A5A8B0")
    City_Question_Label.place(x=225, y=420)


    #Text Entry

    Text_Entry = Entry(root, font=("Century Gothic", 15), width=30)
    Text_Entry.place(x=230, y=490)


    #Enter Button

    Enter_Button = Button(root, text="Enter", font=("Century Gothic", 15), fg="#fff", bg="#7b7b7b", width=10, command=check, relief=FLAT)
    Enter_Button.place(x=590, y=485)


    #Root Mainloop

    root.mainloop()
