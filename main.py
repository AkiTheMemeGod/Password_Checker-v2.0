import Functions as fn
# import pandas as pd
while True:
    choice = input("Password Generator/Checker : \n\n"
                   "Generate | Check | Manage | Exit : ? ")
    choice.lower()
    if choice.startswith("generate"):

        length = input("Enter your passwords length : ")
        gen_pass = fn.gen(length)
        print(gen_pass)
        fn.save(gen_pass)

    elif choice.startswith("check"):
        while True:

            # pwd = input("Enter the password to check (len = 16 or more) : ") + "\n"
            sec,pwd = fn.checker()
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
                print("enter something dumbass .. ")
    elif choice.startswith("manage"):
        userchoice = input("Show / Edit / Delete / Clearall :")
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
                fn.saving()
                exit("Bummer !")
            else:
                fn.saving()
                exit("invalid choice !")
    elif choice.startswith("exit"):
        fn.saving()
        exit("BYE BYE .. !")
    else:
        print("invalid choice try again .. ! ")


# https://thecleverprogrammer.com/2021/04/14/otp-verification-using-python/