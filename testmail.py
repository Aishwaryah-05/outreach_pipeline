import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))

msg = EmailMessage()
msg["Subject"] = "SMTP Test"
msg["From"] = EMAIL
msg["To"] = "aishwaryah825@gmail.com"   # replace with your gmail
msg.set_content("Testing outreach email setup")

server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()
server.login(EMAIL, PASSWORD)
server.send_message(msg)

print("Mail Sent Successfully")

server.quit()