import flet as ft

def main(page: ft.Page):
    page.title = "Page 2 - OTP Verification"
    page.window.width = 600
    page.window.height = 600

    otp_input = ft.TextField(label="Enter OTP")

    
    with open("otp.txt", "r") as f:
        correct_otp = f.read().replace("\n", "")

    status_text = ft.Text("")

    def verify_clicked(e):
        if otp_input.value == correct_otp:
            status_text.value = "Verified!"
            status_text.color = "green"
        else:
            status_text.value = "Incorrect OTP"
            status_text.color = "red"
        page.update()

    verify_button = ft.ElevatedButton("Verify OTP", on_click=verify_clicked)

    page.add(
        ft.Text("Please Enter the OTP"),
        otp_input,
        verify_button,
        status_text
    )

ft.app(target=main)