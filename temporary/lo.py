import tkinter as tk
from tkinter import messagebox
import Functions as fn
import os

class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")

        self.key = fn.gen_key()
        self.email = ""
        self.session = 0

        admin_label = tk.Label(root, text="Enter Your Nickname:")
        admin_label.pack()
        self.admin_entry = tk.Entry(root)
        self.admin_entry.pack()

        admin_button = tk.Button(root, text="Login", command=self.login)
        admin_button.pack()

        self.logged_in = False
        self.admin_privileges = False

    def login(self):
        admin_name = self.admin_entry.get().lower()
        if admin_name == "akash":
            self.logged_in = True
            self.admin_privileges = True
            self.email = "k.akashkumar@gmail.com"  # You might need to implement email input
            self.show_menu()
        else:
            messagebox.showerror("Access Denied", "You don't have access to this code yet.")

    def show_menu(self):
        menu_label = tk.Label(self.root, text="Password Generator/Checker v2.0\nLogged on user: Admin")
        menu_label.pack()

        generate_button = tk.Button(self.root, text="Generate", command=self.generate_password)
        generate_button.pack()

        check_button = tk.Button(self.root, text="Check", command=self.check_password)
        check_button.pack()

        manage_button = tk.Button(self.root, text="Manage", command=self.manage_passwords)
        manage_button.pack()

        exit_button = tk.Button(self.root, text="Exit", command=self.exit_app)
        exit_button.pack()

    def generate_password(self):
        if not self.logged_in:
            return

        length = tk.simpledialog.askinteger("Password Length", "Enter password length:")
        if length is not None:
            gen_pass = fn.gen(length)
            messagebox.showinfo("Generated Password", gen_pass)
            fn.save(gen_pass)

    def check_password(self):
        if not self.logged_in:
            return

        sec, pwd = fn.checker()
        if sec == 4:
            messagebox.showinfo("Password Strength", "Strong password!")
            fn.save(pwd)
        elif sec == 3:
            messagebox.showinfo("Password Strength", "Mediocre password!")
            fn.save(pwd)
        else:
            messagebox.showinfo("Password Strength", "Weak password! Please try again.")

    def manage_passwords(self):
        if not self.logged_in:
            return

        if not fn.verify_otp(self.email, self.session):
            return

        # Implement the password management logic using tkinter dialogs

    def exit_app(self):
        if self.logged_in:
            fn.saving()
            fn.encrypt(self.key)
            os.remove("passwords.txt")
            os.remove("usernames.txt")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.mainloop()
