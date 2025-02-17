import smtplib
from email.mime.text import MIMEText
from config import SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_EMAIL

def send_email(process_name, process_pid, cpu_usage):
    """ Sends an email alert when a system process exceeds CPU usage threshold. """
    subject = "High CPU Usage Alert: System Process"
    body = f"System process '{process_name}' (PID: {process_pid}) is consuming {cpu_usage:.2f}% CPU."

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        print(f"Email sent regarding system process '{process_name}' consuming high CPU.")
    except Exception as e:
        print(f"Failed to send email: {e}")
