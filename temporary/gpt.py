import pandas as pd
import random
import string
import re

# Initialize an empty DataFrame to store passwords
data = {'Password': []}
df = pd.DataFrame(data)


def generate_password():
    special_characters = '!@#$%^&*()_-+=<>?'
    capital_letters = string.ascii_uppercase
    numbers = string.digits

    password = (
            random.sample(special_characters, 3) +
            random.sample(capital_letters, 4) +
            random.sample(numbers, 4) +
            random.sample(string.ascii_letters + string.digits, 5)
    )
    random.shuffle(password)
    return ''.join(password)


def save_to_file(password):
    with open('../pg_chk_fls/passwords.txt', 'a') as file:
        file.write(password + '\n')


def display_passwords():
    print(df)


def delete_password(index):
    df.drop(index, inplace=True)
    df.reset_index(drop=True, inplace=True)


def check_password_constraints(password):
    if len(password) != 16:
        return False

    if len(re.findall(r'[!@#$%^&*()_+=<>?]', password)) < 3:
        return False

    if len(re.findall(r'[A-Z]', password)) < 4:
        return False

    if len(re.findall(r'\d', password)) < 4:
        return False

    return True


while True:
    print("1. Generate Password")
    print("2. Check Password")
    print("3. Display Passwords")
    print("4. Delete Password")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        new_password = generate_password()
        print("Generated Password:", new_password)
        if check_password_constraints(new_password):
            save_to_file(new_password)
            df = df._append({'Password': new_password}, ignore_index=True)
            print("Password saved successfully.")
        else:
            print("Generated password does not meet constraints.")

    elif choice == '2':
        user_password = input("Enter the password to check: ")
        if check_password_constraints(user_password):
            print("Password meets constraints.")
        else:
            print("Password does not meet constraints.")

    elif choice == '3':
        display_passwords()

    elif choice == '4':
        display_passwords()
        index = int(input("Enter the index of the password to delete: "))
        delete_password(index)
        print("Password deleted successfully.")

    elif choice == '5':
        break
