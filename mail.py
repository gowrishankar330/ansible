import shutil
import smtplib
from email.message import EmailMessage

def check_disk(threshold_percent=80):
    total, used, free = shutil.disk_usage("/")
    percent_used = (used / total) * 100
    
    if percent_used > threshold_percent:
        send_alert_email(percent_used)

def send_alert_email(usage):
    msg = EmailMessage()
    msg.set_content(f"Warning! Disk usage is at {usage:.2f}%.")
    msg["Subject"] = "Disk Space Alert"
    msg["From"] = "you@example.com"
    msg["To"] = "admin@example.com"
    
    with smtplib.SMTP("localhost") as server:
        server.send_message(msg)

check_disk()