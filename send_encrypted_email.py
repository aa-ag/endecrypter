###--- IMPORTS ---###
import smtplib  # https://docs.python.org/3/library/smtplib.html
import ssl
import settings
import mimetypes
from email.message import EmailMessage


###--- FUNCTIONS ---###


def send_encrypted_email():

    # Create a SSLContext object with default settings.
    context = ssl.create_default_context()

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls(context=context)
        smtp.ehlo()
        smtp.login(settings.sending_from, settings.hahaha)
        smtp.sendmail(settings.sending_from, settings.to, 'Hello World')


###--- DRIVER CODE ---###
if __name__ == "__main__":
    send_encrypted_email()
