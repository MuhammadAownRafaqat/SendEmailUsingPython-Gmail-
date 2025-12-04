import flet as ft
import random
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


RECIPIENT_EMAIL = ""


def send_email(otp_code):
    try:
        subject = "Your OTP"
        body = f"Your OTP is: {otp_code}"

        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = RECIPIENT_EMAIL
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, RECIPIENT_EMAIL, msg.as_string())

        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", e)


def main(page: ft.Page):

    page.title = "Page 1 - User Details"
    page.window.width = 600
    page.window.height = 600
    name = ft.TextField(label="Name")
    password = ft.TextField(label="Password", password=True)
    email = ft.TextField(label="Email")

    datatable = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Field")),
            ft.DataColumn(ft.Text("Value")),
        ],
        rows=[]
    )

    def update_table(e):
        datatable.rows = [
            ft.DataRow(cells=[ft.DataCell(ft.Text("Name")), ft.DataCell(ft.Text(name.value))]),
            ft.DataRow(cells=[ft.DataCell(ft.Text("Password")), ft.DataCell(ft.Text(password.value))]),
            ft.DataRow(cells=[ft.DataCell(ft.Text("Email")), ft.DataCell(ft.Text(email.value))]),
        ]
        page.update()

    name.on_change = update_table
    password.on_change = update_table
    email.on_change  = update_table

    def next_step_clicked(e):

        
        if name.value == "" or password.value == "" or email.value == "":
            page.snack_bar = ft.SnackBar(ft.Text("Please fill all fields"))
            page.snack_bar.open = True
            page.update()
            return   

        
        otp_code = str(random.randint(100000, 999999))

        
        with open("otp.txt", "w") as f:
            f.write(otp_code)

        
        send_email(otp_code)

        
        os.system("python page2.py")

    next_button = ft.ElevatedButton("Next Step", on_click=next_step_clicked)

    page.add(
        ft.Text("Enter User Details"),
        name,
        password,
        email,
        next_button
    )


ft.app(target=main)