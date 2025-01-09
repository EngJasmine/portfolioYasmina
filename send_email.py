import smtplib
import ssl
import os


def send_email(message):
    # SMTP server configuration
    host = "smtp.gmail.com"
    port = 465
    username = "reema5khamassi@gmail.com"
    password = os.getenv("PASSWORD")  # Use an App Password if you have 2FA enabled
    print(password)
    # Recipient email
    receiver = 'reema5khamassi@gmail.com'

    # Create a secure SSL context
    context = ssl.create_default_context()
    try:
        # Connect to the server and send email
        with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)
            print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


