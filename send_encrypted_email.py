###--- IMPORTS ---###
import smtplib  # https://docs.python.org/3/library/smtplib.html
import ssl
import settings

###--- FUNCTIONS ---###


def send_encrypted_email():
    # Simple Mail Transfer Protocol ("SMTP") session for gmail
    # An SMTP instance encapsulates an SMTP connection.
    session = smtplib.SMTP('smtp.gmail.com', 587)

    # Put the SMTP connection in TLS (Transport Layer Security) mode.
    # All SMTP commands that follow will be encrypted.
    session.starttls()

    # auth gmail
    session.login(f"{settings.sending_from}", f"{settings.hahaha}")

    # body of email/message that will be sent
    message_body = ""

    encrypt_message_body = input("\nEnter the message to encrypt:\n>>")

    for i in range(len(encrypt_message_body)):
        message_body = "Subject: Hi there\n" + \
            message_body + chr(ord(encrypt_message_body[i]))

    # send encrypted message in an email
    session.sendmail(f"{settings.sending_from}",
                     f"{settings.to}", message_body)

    session.quit()


###--- DRIVER CODE ---###
if __name__ == "__main__":
    send_encrypted_email()
