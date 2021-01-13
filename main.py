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

    # opens file, reads data inside, encrypts data and writes new, encrypted data
    with open('lorem.txt', 'rb') as unencrypted_file:
        file_data = unencrypted_file.read()
        encrypted_data = fernet.encrypt(file_data)

    with open('encrypted_lorem.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)


###--- DRIVER CODE ---###
if __name__ == "__main__":
    # write_key()
    encrypt()
