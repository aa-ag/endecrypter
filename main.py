from cryptography.fernet import Fernet
import config

key = Fernet.generate_key()

f = Fernet(key)

token = f.encrypt(config.MY_KEY.encode('utf-8'))
print(token.decode())

# print(f.decrypt(token).decode())