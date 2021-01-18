###--- IMPORTS ---###
import smtplib  # https://docs.python.org/3/library/smtplib.html
import ssl
import settings
import mimetypes
from email.message import EmailMessage


###--- FUNCTIONS ---###


def send_encrypted_email():

    msg = EmailMessage()

    msg['Subject'] = "This is an email..."
    msg['From'] = settings.sending_from
    msg['To'] = settings.to

    msg.set_content('Hello World')

    msg.add_alternative("""
    <p>
        <h1>This is an email?</h1>
        Hello <strong>World</strong>!
    </p>
    """, subtype='html')

    context = ssl.create_default_context()

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls(context=context)
        smtp.ehlo()
        smtp.login(settings.sending_from, settings.hahaha)
        smtp.send_message(msg)


###--- DRIVER CODE ---###
if __name__ == "__main__":
    send_encrypted_email()
