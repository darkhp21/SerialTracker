from cryptography.fernet import Fernet
import requests
orgput = input("Enter Command: ")
def key():
    keys = Fernet.generate_key()
    print(keys)
def get_requests():
    put = input("Enter URL: ")
    req = requests.get(put)
    print(req)
if orgput == "-key":
    print(key())
elif orgput == "-get":
    print(get_requests())
else:
    pass