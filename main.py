import getpass
import base64
import sqlite3

conn = sqlite3.connect('passwords.db')

c = conn.cursor()

# c.execute("""CREATE TABLE passwords (
#     org text,
#     password text
# )""")

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
    base64.b64encode(bytes(password, 'utf-8'))
    c.execute("INSERT INTO passwords VALUES (?, ?)", (org, password))

def show_password():
    org = input("Enter the name of the Organization: ")
    c.execute("SELECT * FROM passwords WHERE org=?", (org,))
    my_pass = c.fetchone()

    if my_pass == None:
        print("This site has not been added!")

    else:
        print(my_pass)

if choice == 1:
    add_password()

elif choice == 2:
    show_password()