import getpass
import base64

print("----------MENU----------")
print("1. Add Password")
print("2. Show Password")
print("3. Delete Password")
print("99. QUIT")
print("------------------------")

choice = 0
password = ""

while choice < 1 or choice > 3 or choice == 99:
    choice = int(input("Enter your Choice: "))

def add_password():
    org = input("Enter the name of organization: ")
    password = getpass.getpass()
    password.encode("ascii")

def show_password():
    input("Enter the name of the Organization: ")

if choice == 1:
    add_password()

elif choice == 2:
    show_password()