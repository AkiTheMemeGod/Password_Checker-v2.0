from logo import *
from Auth import Authentication
from Database import Database


db = Database()
auth = Authentication()

global enc_key

while True:
    print_logo()

    if input("New Here? type help : ").lower() == "help":
        break
    else:
        print("Invalid input try again")

while True:

    cmd = input("\n\n1. New here ? Type Register\n2. Already a User? Type Login\nEnter your Option here : ")

    if cmd == "1" or cmd.lower() == "register":
        print_logo()
        username = input("Please Enter the username : ")
        password = input("Please Enter the Password : ")
        status = auth.register(username, password)
        if status["Success"]:
            print(status["Message"])
            print("Proceed to Login !")

        else:
            print(status["Message"])

    elif cmd == "2" or cmd.lower() == "login":
        print_logo()
        username = input("Please Enter the username : ")
        password = input("Please Enter the Password : ")
        status = auth.login(username, password)
        if status["Success"]:
            enc_key = status["Key"]
            print(status["Message"])
            # print(enc_key)
            break
        else:
            print(print(status["Message"]))

    else:
        print("\n\nEnter a valid option , for eg : Type 1 or 'register' ")
        print_logo()

while True:
    cmd = input("\n\n1. Generate a password\n2. Check a password\n3. Manage all your passwords\nEnter your Option here (0 - 9) : ")
    if cmd == "1":
        pass