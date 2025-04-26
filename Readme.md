# 🛡️ Python Keylogger with Email Reporting
![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-Educational-important)

## 🛡️ Python Keylogger with Email Reporting
KeySentry is a lightweight and efficient Python-based keylogger designed for educational purposes in cybersecurity and ethical hacking. It captures user keystrokes in real-time, securely logs the data, and automatically sends the collected logs to a designated email address at regular intervals. This project demonstrates core concepts like event-driven programming, background threading, secure SMTP communication, and basic cybersecurity monitoring techniques. It provides an excellent foundation for students and security researchers to understand the behavior of monitoring software, how data exfiltration works in ethical testing, and how defense mechanisms can be built against such tools. Built with simplicity and modularity in mind, KeySentry ensures easy customization for research, testing, or learning environments.

## ✨ Features
Real-time keystroke logging

Auto-emailing of log files every 5 minutes

Lightweight and runs in the background

External configuration for secure email handling

Clean and modular code structure

## 🛠️ Technologies Used
Python

pynput (for capturing keystrokes)

smtplib (for sending emails)

threading (for background tasks)

## ⚙️ How It Works
Logs each key pressed by the user.

Writes the keystrokes into a text file with timestamps.

Sends the logs to your email automatically every 5 minutes.

Clears the log after sending to avoid duplicates.

## 🔒 Legal Disclaimer
This project is intended only for authorized testing and educational purposes.
Unauthorized usage on systems you do not own or have permission to monitor is illegal.
The creator is not responsible for any misuse of this tool.

## 📈 Future Enhancements
Hide console window (stealth mode)

Encrypt logs before transmission

Add a GUI dashboard to view logs in real-time

## 📜 License
This project is licensed for educational and personal research use.
