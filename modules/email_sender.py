import smtplib
from email.message import EmailMessage
from config import EMAIL, PASSWORD, SMTP_SERVER, SMTP_PORT

def send_email(to_email, subject, body):

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = to_email
    msg.set_content(body)

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL, PASSWORD)

    server.send_message(msg)

    server.quit()

    print("Email Sent")