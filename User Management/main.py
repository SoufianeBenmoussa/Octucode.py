import os
import time  # Import the time module

def cln():
    os.system("cls" if os.name == "nt" else "clear")

def delay(seconds):
    """Pause the program for the specified number of seconds."""
    time.sleep(seconds)

class User:
    def __init__(self, first_name, last_name, email, password, status = 'inactive'):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.status = status

    def display_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")
        print(f"Status: {self.status}")

def creat_user():
    while True:
        cln()
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        email = input("Enter Email: ")
        password = input("Enter Password: ")
        return User(first_name, last_name, email, password)

user_management = []

        
