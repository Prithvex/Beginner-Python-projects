import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "your_email@gmail.com"
sender_password = "your_app_password"

recipients = [
    "person1@example.com",
    "person2@example.com",
    "person3@example.com"
]

# Create message
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = ", ".join(recipients)
msg["Subject"] = "Test Email"

body = "Hello everyone, this is a test message!"
msg.attach(MIMEText(body, "plain"))

# Send email
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipients, msg.as_string())

print("Emails sent successfully!")
