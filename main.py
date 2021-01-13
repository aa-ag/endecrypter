###--- IMPORTS ---###
from cryptography.fernet import Fernet
import config


###--- GLOBAL VARIABLES ---###
key = config.MY_KEY
fernet = Fernet(key)

###--- FUNCTIONS ---###


def write_key():
    '''
     Generates a key, and saves it to a config.py file
    '''
    key = Fernet.generate_key()
    with open("config.py", "wb") as kf:
        kf.write(key)


def decrypt(token):
    '''
     decrypts string using key
    '''
    global key, fernet

    decrypted_message = fernet.decrypt(token)

    print(decrypted_message.decode())


def encrypt():
    '''
     Encrypts message using Fernet class
    '''
    # import/generate key
    # key = Fernet.generate_key()
    global key, fernet

    # convert message to bytes by encoding it
    message = "Hello, World!".encode()

    # encrypt message
    token = fernet.encrypt(message)

    print(token)
    decrypt(token)


###--- DRIVER CODE ---###
if __name__ == "__main__":
    # write_key()
    encrypt()
