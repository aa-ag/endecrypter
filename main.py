###--- IMPORTS ---###
from cryptography.fernet import Fernet
import base64
import config


###--- FUNCTIONS ---###

def write_key():
    '''
     Generates a key, and saves it to a config.py file
    '''
    key = Fernet.generate_key()
    with open("config.py", "wb") as kf:
        kf.write(key)


def encrypt():
    '''
     Encrypts message using Fernet class
    '''
    # generate key
    key = Fernet.generate_key()

    # initialize Fernet class
    fernet = Fernet(key)

    # convert message to bytes by encoding it
    message = "Hello, World!".encode()

    # encrypt message
    token = fernet.encrypt(message)

    print(token)


def decrypt():
    pass


###--- DRIVER CODE ---###
if __name__ == "__main__":
    # write_key()
    encrypt()
    # pass
