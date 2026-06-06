import requests
from config import BREVO_API_KEY

def send_brevo_email(to_email, subject, content):

    url = "https://api.brevo.com/v3/smtp/email"

    headers = {
        "accept": "application/json",
        "api-key": BREVO_API_KEY,
        "content-type": "application/json"
    }

    data = {
        "sender": {
            "name": "Aishwarya",
            "email": "aishwarya@outreachdemo.online"
        },
        "to": [
            {
                "email": to_email
            }
        ],
        "subject": subject,
        "htmlContent": f"<html><body><p>{content}</p></body></html>"
    }

    response = requests.post(
        url,
        json=data,
        headers=headers
    )

    print(response.text)