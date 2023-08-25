import Functions as fn
import os

key = fn.gen_key()

try:
    email = ""
    session = 0
    admin = input("Enter Your Nickname sir : ")
    admin = admin.lower()
    if admin == "akash":
        print("You have admin privileges ! ")
        if os.path.exists('.idea\mykey.key'):
            fn.decrypt(key)
        email = "k.akashkumar@gmail.com"
    else:
        exit("You dont have access to this code yet : ")

    while True:
        choice = input(f"\n\n\t\t\t\tPassword Generator/Checker v2.0\n\t\t\t\t\tLogged on user : {admin}\n\n"
                       "Generate | Check | Manage | Exit ? : ")
        choice.lower()
        if choice.startswith("generate"):

            length = input("Enter your passwords length : ")
            gen_pass = fn.gen(length)
            print(gen_pass)
            fn.save(gen_pass)

        elif choice.startswith("check"):
            while True:

                # pwd = input("Enter the password to check (len = 16 or more) : ") + "\n"
                sec, pwd = fn.checker()
                if sec == 4:
                    print("\nStrong password !")
                    fn.save(pwd)

                    break
                elif sec == 3:
                    print("\nMediocre password !")
                    fn.save(pwd)
                    break
                elif sec == 2 or 1:
                    print("\nWEAK PASSWORD Try again \n")
                    choice = input("Want to try auto generation ? y/n : ")
                    choice.lower()
                    if choice.startswith("y"):
                        gen_pass = fn.gen(16)
                        print(gen_pass)
                        fn.save(gen_pass)
                        break
                    else:
                        print("Alright .. !")
                else:
                    print("enter something  .. ")
        elif choice.startswith("manage"):
            if fn.verify_otp(email, session):
                while True:
                    userchoice = input("\n\nShow / Edit / Delete / Clearall / MainMenu ? : ")
                    userchoice.lower()
                    if userchoice.startswith("show"):
                        fn.show()
                    elif userchoice.startswith("edit"):
                        fn.edit()
                    elif userchoice.startswith("delete"):
                        fn.delete()
                    elif userchoice.startswith("clearall"):
                        r = input("Are you sure do you want to clear all ? y/n : ")
                        r.lower()
                        if r == 'y':
                            fn.clear()
                        elif r == 'n':
                            continue
                        else:
                            continue
                    elif userchoice.startswith("mainmenu"):
                        session = 1
                        break

        elif choice.startswith("exit"):
            exit("BYE BYE .. !")
        else:
            print("invalid choice try again .. ! ")

except KeyboardInterrupt:
    fn.saving()
    fn.encrypt(key)
    raise
# have to implement the encryption cycle
finally:
    fn.saving()
    fn.encrypt(key)
    raise
