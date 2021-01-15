###--- IMPORTS ---###
from cryptography.fernet import Fernet
import settings


###--- GLOBAL VARIABLES ---###
key = settings.MY_KEY
fernet = Fernet(key)

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
     Encrypts file using Fernet class
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


def decrypt():
    '''
     Decrypts file using key
    '''
    global key, fernet

    # opens, reads, decrypts encrypted file and writes new uncrypted file
    with open('encrypted_lorem.txt', 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open('lorem.txt', 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)


def encrypt_image():
    try:
        path_to_image = '/Users/aaronaguerrevere/Documents/portfolio/endecrypter/thisisfine.jpeg'
        key = 15

        fin = open(path_to_image, 'rb')

        image = fin.read()
        fin.close()

        # Return a new array of bytes
        image = bytearray(image)

        for index, value in enumerate(image):
            image[index] = value ^ key
            # The ^ operator yields the bitwise XOR (exclusive OR) of its arguments,
            # which must be integers.

        fin = open(path_to_image, 'wb')

        fin.write(image)
        fin.close()
        print("Image encrypted.")

    except Exception:
        print("Error: ", Exception.__name__)


def decrypt_image():
    try:
        path_to_image = '/Users/aaronaguerrevere/Documents/portfolio/endecrypter/thisisfine.jpeg'
        key = 15

        fin = open(path_to_image, 'rb')

        image = fin.read()
        fin.close()

        # Return a new array of bytes
        image = bytearray(image)

        for index, value in enumerate(image):
            image[index] = value ^ key
            # The ^ operator yields the bitwise XOR (exclusive OR) of its arguments,
            # which must be integers.

        fin = open(path_to_image, 'wb')

        fin.write(image)
        fin.close()
        print("Image decrypted.")

    except Exception:
        print("Error: ", Exception.__name__)


###--- DRIVER CODE ---###
if __name__ == "__main__":
    # write_key()
    # encrypt()
    # decrypt()
    # encrypt_image()
    decrypt_image()
