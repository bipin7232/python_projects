import hashlib


text = input("Enter message: ")

encod = hashlib.sha256(text.encode())
print(encod.hexdigest())

