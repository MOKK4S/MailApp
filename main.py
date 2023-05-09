import tkinter as tk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os
from tkinter import ttk  # for better looking widgets

# funkcja wysyłająca maile
def send_email():
    # odczytanie danych z pól formularza
    email = email_entry.get()
    subject = subject_entry.get()
    body = body_entry.get()
    count = int(count_entry.get())

    # odczytanie danych do logowania z pliku mails.txt
    with open('mails.txt') as f:
        lines = f.readlines()
        email_login, password = lines[0].split(":") 
    # email_login = lines[0].strip()
    # password = lines[1].strip()

    # połączenie z serwerem SMTP Google
    smtp_connection = smtplib.SMTP('smtp.eu.mailgun.org', 587)
    smtp_connection.ehlo()
    smtp_connection.starttls()
    smtp_connection.login(email_login, password)

    # wysłanie maili
    for i in range(count):
        # stworzenie obiektu MIMEMultipart
        message = MIMEMultipart()
        message['Subject'] = subject
        message['From'] = email_login
        message['To'] = email
        message.attach(MIMEText(body, 'plain'))

        # załączenie obrazka do maila
        if os.path.exists('image.jpg'):
            with open('image.jpg', 'rb') as f:
                img_data = f.read()
            image = MIMEImage(img_data, name="image.jpg")
            message.attach(image)

        # wysłanie maila
        smtp_connection.send_message(message)

        # wyświetl informację o postępie
        status_label.config(text=f"Wysłano {i+1}/{count} maili")

    # zamknij połączenie SMTP
    smtp_connection.quit()

    # wyświetl komunikat o zakończeniu wysyłania maili
    status_label.config(text="Wysłano maile")

# tworzenie interfejsu użytkownika
root = tk.Tk()
root.title("Wysyłanie maili")
root.geometry("600x400")
root.configure(bg="gray30")

# Create a main frame
main_frame = ttk.Frame(root)
main_frame.pack(pady=100)

# pole Email
email_label = ttk.Label(main_frame, text="Email:")
email_label.grid(row=0, column=0, padx=5, pady=5, sticky="W")
email_entry = ttk.Entry(main_frame, width=50)
email_entry.grid(row=0, column=1, padx=5, pady=5)

# pole Temat
subject_label = ttk.Label(main_frame, text="Temat:")
subject_label.grid(row=1, column=0, padx=5, pady=5, sticky="W")
subject_entry = ttk.Entry(main_frame, width=50)
subject_entry.grid(row=1, column=1, padx=5, pady=5)

# pole Treść
body_label = ttk.Label(main_frame, text="Treść:")
body_label.grid(row=2, column=0, padx=5, pady=5, sticky="W")
body_entry = ttk.Entry(main_frame, width=50)
body_entry.grid(row=2, column=1, padx=5, pady=5)

# pole Ilość
count_label = ttk.Label(main_frame, text="Ilość:")
count_label.grid(row=3, column=0, padx=5, pady=5, sticky="W")
count_entry = ttk.Entry(main_frame, width=50)
count_entry.grid(row=3, column=1, padx=5, pady=5)

#przycisk Wyślij
send_button = ttk.Button(main_frame, text="Wyślij", command=send_email)
send_button.grid(row=4, column=0, columnspan=2)

#pole statusu
status_label = ttk.Label(main_frame, text="")
status_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="W")

#wyświetlenie interfejsu użytkownika
root.mainloop()



x = 4
obliczenie = x ^ 5