import smtplib
import os


EMAIL_ADDRESS = "nikolaa.kostcI4@gmail.com"
EMAIL_PASSWORD = "sD&4b=%5Ge38jM@Y"


with smtplib.SMTP('smtp.gmail.com', 28) as smtp:
    
    subject = "Test1"
    body = "Test2"

    msg = f"Subject : {subject}\n\n{body}"

    smtp.sendmail(EMAIL_ADDRESS, "nikosta350@gmail.com", msg)