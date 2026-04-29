import random
import string
import re

def check_strength(password):
    if len(password) < 8:
        return "Weak (Too short)"
    if not re.search("[A-Z]", password):
        return "Weak (No uppercase)"
    if not re.search("[0-9]", password):
        return "Weak (No number)"
    if not re.search("[@#$%^&*!]", password):
        return "Weak (No symbol)"
    return "Strong Password"

def generate_password():
    chars = string.ascii_letters + string.digits + "@#$%^&*!"
    return ''.join(random.choice(chars) for _ in range(10))

# main
pwd = input("Enter password: ")
print("Strength:", check_strength(pwd))

choice = input("Generate strong password? (y/n): ")
if choice == 'y':
    print("Generated:", generate_password())