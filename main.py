import os
import time
import requests
from pathlib import Path
import smtplib
from email.mime.text import MIMEText


def getenv_required(key: str) -> str:
    val = os.getenv(key)
    if val is None:
        raise ValueError(f"Environment variable {key} is required!")
    return val


EMAIL_SENDER = getenv_required("EMAIL_SENDER")
EMAIL_PASSWORD = getenv_required("EMAIL_PASSWORD")
EMAIL_RECIPENTS = [s.strip() for s in getenv_required("EMAIL_RECIPENTS").split(";")]
SLEEP_TIME_MINS = float(os.getenv("SLEEP_TIME_MINS", "30"))


prev_ip_file = Path(__file__).parent / "_prev_ip"


while True:
    curr_ip = requests.get('https://checkip.amazonaws.com').text.strip()
    
    if not prev_ip_file.exists():
        with open(prev_ip_file, "w") as f:
            f.write(curr_ip)
    else:
        with open(prev_ip_file, "r") as f:
            prev_ip = f.readline().strip()
        
        if prev_ip != curr_ip:
            body = f"Your public IP has changed!\n\nOld: {prev_ip}\nNew: {curr_ip}"
            print(body)
            msg = MIMEText(body)
            msg["Subject"] = "Your public IP has changed!"
            msg["From"] = EMAIL_SENDER
            msg["To"] = ', '.join(EMAIL_RECIPENTS)
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
                smtp_server.login(EMAIL_SENDER, EMAIL_PASSWORD)
                smtp_server.sendmail(EMAIL_SENDER, EMAIL_RECIPENTS, msg.as_string())

            print("Email sent.")

        with open(prev_ip_file, "w") as f:
            f.write(curr_ip)

    print(f"Sleeping for {SLEEP_TIME_MINS} minutes...")
    time.sleep(60*SLEEP_TIME_MINS)
