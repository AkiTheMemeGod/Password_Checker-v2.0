import pandas as pd
import smtplib as sm
import time as tm
import random as rd
from cryptography.fernet import Fernet as fn
import os


def account():
    while True:
        if os.path.exists(".idea/acc_us.txt"):
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if username == open(".idea/acc_us.txt").read() and password == open(".idea/acc_pd.txt").read():
                print("Successful login")
                emails = open(".idea/acc_email.txt").read()
                return True, emails, username
            else:
                print('Incorrect')
                return False
        else:
            filename = ".idea/acc_us.txt"
            with open(filename, "w") as f:
                f.write(input("Enter a username: "))

            filename = ".idea/acc_pd.txt"
            with open(filename, "w") as f:
                f.write(input("Enter a password: "))

            filename = ".idea/acc_email.txt"
            with open(filename, "w") as f:
                f.write(input("Enter a email: "))



def gen_key():
    if os.path.exists('.idea\mykey.key'):
        with open('.idea\mykey.key', 'rb') as keys:
            key = keys.read()
        return key
    else:
        key = fn.generate_key()
        with open('.idea\mykey.key', 'wb') as keys:
            keys.write(key)
        return key


def encrypt(key):
    f = fn(key)

    with open('passwords.txt', 'rb') as passes:
        passes = passes.read()

    enc_pass = f.encrypt(passes)

    with open('enc_passwords.txt', 'wb') as enc_passes:
        enc_passes.write(enc_pass)

    with open('usernames.txt', 'rb') as usernames:
        users = usernames.read()

    enc_user = f.encrypt(users)

    with open('enc_usernames.txt', 'wb') as enc_users:
        enc_users.write(enc_user)

    with open('login_credentials.xlsx', 'rb') as logs:
        log = logs.read()

    enc_log = f.encrypt(log)

    with open('enc_login_credentials.xlsx', 'wb') as enc_logs:
        enc_logs.write(enc_log)

    os.remove("passwords.txt")
    os.remove("usernames.txt")
    os.remove("login_credentials.xlsx")


def decrypt(key):
    f = fn(key)

    with open('enc_passwords.txt', 'rb') as enc_passes:
        passes = enc_passes.read()

    dec_pass = f.decrypt(passes)

    with open('passwords.txt', 'wb') as passes:
        passes.write(dec_pass)

    with open('enc_usernames.txt', 'rb') as enc_users:
        users = enc_users.read()

    dec_users = f.decrypt(users)

    with open('usernames.txt', 'wb') as usernames:
        usernames.write(dec_users)

    with open('enc_login_credentials.xlsx', 'rb') as enc_logs:
        log = enc_logs.read()

    dec_logs = f.decrypt(log)

    with open('login_credentials.xlsx', 'wb') as logs:
        logs.write(dec_logs)

    os.remove("enc_passwords.txt")
    os.remove("enc_usernames.txt")
    os.remove("enc_login_credentials.xlsx")


def gen(length):
    small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v',
             'w', 'x', 'y', 'z']
    caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
    spec = ['!', '@', '#', '$', '%', '&', '=']
    i = 0
    pwd = ""

    def small_gen():
        x = rd.choice(small)
        return x

    def caps_gen():
        y = rd.choice(caps)
        return y

    def num_gen():
        z = rd.randint(0, 9)
        return str(z)

    def spec_gen():
        s = rd.choice(spec)
        return s

    args = [small_gen, caps_gen, num_gen, spec_gen]

    while i < int(length):
        func = rd.choice(args)
        pwd = f"{pwd}{func()}"
        i += 1

    # print(pwd)
    pwd = pwd + "\n"
    return pwd


def get_pd():
    with open("passwords.txt", 'r') as file:
        passwords = file.readlines()
    return passwords


def put_pd(pwd):
    with open("passwords.txt", 'w') as file:
        file.writelines(pwd)


def get_usr():
    with open("usernames.txt", 'r') as file:
        usernames = file.readlines()
    return usernames


def put_usr(usrn):
    with open("usernames.txt", 'w') as file:
        file.writelines(usrn)


def get_time():
    with open("timestamp.txt", 'r') as file:
        times = file.readlines()
    return times


def put_time(tim):
    with open("timestamp.txt", 'w') as file:
        file.writelines(tim)


def checker():
    vuln = []
    spec = ['!', '@', '#', '$', '%', '&', '=']
    cap = 0
    spc = 0
    num = 0
    smll = 0
    while True:
        pwd = input("Enter the password to check (len = 16 or more) : ") + "\n"

        if len(pwd) >= 16:
            for p in pwd:
                if p.isdigit():
                    num += 1

            for p in pwd:
                if p.islower():
                    smll += 1

            for p in pwd:
                if p.isupper():
                    cap += 1

            for p in pwd:
                if p in spec:
                    spc += 1

            break

        else:
            print("character length is below 16 try again : \n")

    if spc >= 3:
        em4 = "✅"
        vuln.append(True)
    else:
        em4 = "❌"
    if cap >= 3:
        em3 = "✅"
        vuln.append(True)
    else:
        em3 = "❌"
    if smll >= 6:
        em2 = "✅"
        vuln.append(True)
    else:
        em2 = "❌"
    if num >= 4:
        em1 = "✅"
        vuln.append(True)
    else:
        em1 = "❌"

    print(smll, "/6 small letters - ", em2)
    print(cap, "/3 capital letters - ", em3)
    print(num, "/4 numbers - ", em1)
    print(spc, "/3 special characters - ", em4)
    x = 0
    for i in vuln:
        if i:
            x += 1

    return x, pwd


def save(pwd):
    pds = []
    usrn = []
    time = []
    yorn = input("Do you want to save this password Y/N ? : ")
    yorn.lower()
    if yorn.startswith('y'):
        usr = input("Enter the user name : ") + '\n'

        usrn = get_usr()
        usrn.append(usr)
        put_usr(usrn)

        pds = get_pd()
        pds.append(pwd)
        put_pd(pds)

        time = get_time()
        time.append(tm.asctime() + '\n')
        put_time(time)

    else:
        saving()


def show():
    usrn = []
    pds = []
    time = []
    time = get_time()
    # time.append(tm.asctime())

    usrn = get_usr()
    pds = get_pd()

    usrn = [i.strip('\n') for i in usrn]
    pds = [i.strip('\n') for i in pds]
    time = [i.strip('\n') for i in time]
    data = {
        "Date/Time": time,
        "USERNAMES": usrn,
        "PASSWORDS": pds
    }
    df = pd.DataFrame(data)
    print(df)
    usrn = [i + "\n" for i in usrn]
    pds = [i + "\n" for i in pds]
    time = [i + "\n" for i in time]
    put_usr(usrn)
    put_pd(pds)
    put_time(time)


def delete():
    usrn = []
    pds = []
    time = []
    time = get_time()
    # time.append(tm.asctime())

    usrn = get_usr()
    pds = get_pd()

    usrn = [i.strip('\n') for i in usrn]
    pds = [i.strip('\n') for i in pds]
    time = [i.strip('\n') for i in time]
    data = {
        "Date/Time": time,
        "USERNAMES": usrn,
        "PASSWORDS": pds
    }
    df = pd.DataFrame(data)
    print(df)
    delete = int(input("\nMention the row.no you want to be deleted : "))
    df.drop(delete, inplace=True)
    print(df)
    usrn.remove(usrn[delete])
    pds.remove(pds[delete])
    time.remove(time[delete])
    usrn = [i + "\n" for i in usrn]
    pds = [i + "\n" for i in pds]
    time = [i + "\n" for i in time]
    put_usr(usrn)
    put_pd(pds)
    put_time(time)


def edit():
    usrn = []
    pds = []
    time = []

    time = get_time()
    # time.append(tm.asctime())

    usrn = get_usr()
    pds = get_pd()

    usrn = [i.strip('\n') for i in usrn]
    pds = [i.strip('\n') for i in pds]
    time = [i.strip('\n') for i in time]

    data = {
        "Date/Time": time,
        "USERNAMES": usrn,
        "PASSWORDS": pds
    }
    df = pd.DataFrame(data)
    print(df)
    row = int(input("\nMention the row.no you want to edit : "))

    while True:
        editor = input("\nenter U to edit Username : "
                       "\nenter P to edit Password : ")
        editor.lower()
        if editor == 'u':
            usrn[row] = input("Enter the new username : ")  # + "\n"
            break
        elif editor == 'p':
            pds[row] = input("Enter the new password : ")  # + "\n"
            break
        else:
            print("wrong selection try again .. ")

    data = {
        "Date/Time": time,
        "USERNAMES": usrn,
        "PASSWORDS": pds
    }
    df = pd.DataFrame(data)
    print(df)

    usrn = [i + "\n" for i in usrn]
    pds = [i + "\n" for i in pds]
    time = [i + "\n" for i in time]
    put_usr(usrn)
    put_pd(pds)
    put_time(time)


def clear():
    usrn = []
    pds = []
    time = []

    time = get_time()
    time.clear()
    put_time(time)

    usrn = get_usr()
    usrn.clear()
    put_usr(usrn)

    pds = get_pd()
    pds.clear()
    put_pd(pds)


def saving():
    usrn = []
    pds = []
    time = []
    time = get_time()
    # time.append(tm.asctime())

    usrn = get_usr()
    pds = get_pd()

    usrn = [i.strip('\n') for i in usrn]
    pds = [i.strip('\n') for i in pds]
    time = [i.strip('\n') for i in time]
    data = {
        "Date/Time": time,
        "USERNAMES": usrn,
        "PASSWORDS": pds
    }
    df = pd.DataFrame(data)
    df.to_excel("login_credentials.xlsx")

    usrn = [i + "\n" for i in usrn]
    pds = [i + "\n" for i in pds]
    time = [i + "\n" for i in time]

    put_usr(usrn)
    put_pd(pds)
    put_time(time)


def otp_gen():
    otp = ""
    for i in range(0, 6):
        z = str(rd.randint(0, 9))
        otp += z
    return otp


def verify_otp(email, session):
    i = 0
    while session == 0:
        print("INITIALIZING GENERAL 2-FACT AUTHENTICATION\n"
              f"A 6 digit OTP has been sent to the email {email} \n")
        OTP = otp_gen()
        s = sm.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("akis.pwdchecker@gmail.com", "tjjqhaifdobuluhg")
        s.sendmail('akis.pwdchecker@gmail.com', email, OTP)
        while i < 5:
            a = input("Enter Your OTP >>: ")
            if a == OTP:
                print("Verified !\n")
                break
            else:
                i += 1
                print(f"Wrong OTP , you have {5 - i} - no of attempts left")
                if i == 5:
                    exit("\t\t\t\n\nTOO MANY ATTEMPTS TRY AGAIN LATER !")
        break
    return True
