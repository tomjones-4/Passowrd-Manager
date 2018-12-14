from tkinter import *
import time
import sys
import tkinter.messagebox as tm

import subprocess
from subprocess import PIPE, Popen

class LoginFrame(Frame):

    def launch_master_password_program(self):
        cmd = 'master_password.py'
        P = Popen(["python", "-u", cmd], stdin=PIPE, stdout=PIPE, bufsize=1)
        return P

    def toplevel_launch(self, msg):
        top = Toplevel()

        label = Message(top, text=msg)
        label.pack()

        button = Button(top, text="Dismiss", command=top.destroy)
        button.pack()


    def _generate_password_btn_clicked(self):

        username = self.entry_username.get()
        url = self.entry_url.get()
        masterPassword = self.entry_password.get()

        P = self.launch_master_password_program()

        text = P.stdout.readline() # Master password has already been created. Type 'a' to add a password or 'g' to get a password.

        P.stdin.write(b'a\n') # enter 'a'
        P.stdin.flush()

        text = P.stdout.readline()  # Enter master password.

        out = masterPassword + '\n'
        b = out.encode('utf-8')
        P.stdin.write(b)
        P.stdin.flush()

        masterPassword = None

        text = P.stdout.readline() # Adding new password:
        text = text.strip()

        if text != b'Adding new password:':
            self.toplevel_launch(text)
            P.kill()
            return

        text = P.stdout.readline() # Enter 'e' to add a password for an existing account. Enter 'n' to generate a password for a new account.

        P.stdin.write(b'n\n') # enter 'n'
        P.stdin.flush()

        text = P.stdout.readline() # Enter username

        out = username + '\n'
        b = out.encode('utf-8')
        P.stdin.write(b)
        P.stdin.flush()

        text = P.stdout.readline() # Enter url

        out = url + '\n'
        b = out.encode('utf-8')
        P.stdin.write(b)
        P.stdin.flush()

        text = P.stdout.readline() # Password generated.
        self.toplevel_launch(text)

        P.kill()

    def _input_password_btn_clicked(self):

        username = self.entry_username.get()
        url = self.entry_url.get()
        masterPassword = self.entry_password.get()
        inputPassword = self.entry_input.get()

        P = self.launch_master_password_program()

        text = P.stdout.readline() # Master password has already been created. Type 'a' to add a password or 'g' to get a password.

        P.stdin.write(b'a\n') # enter 'a'
        P.stdin.flush()

        text = P.stdout.readline()  # Enter master password.

        out = masterPassword + '\n'
        b = out.encode('utf-8')
        P.stdin.write(b)
        P.stdin.flush()

        masterPassword = None

        text = P.stdout.readline() # Adding new password:
        text = text.strip()

        if text == b'Incorrect master password entered. Try again.':
            self.toplevel_launch(text)
            P.kill()
            return

        text = P.stdout.readline() # Enter 'e' to add a password for an existing account. Enter 'n' to generate a password for a new account.

        P.stdin.write(b'e\n') # enter 'e'
        P.stdin.flush()

        text = P.stdout.readline() # Enter password to be encrypted

        out = inputPassword + '\n'
        b = out.encode('utf-8')
        P.stdin.write(b)
        P.stdin.flush()

        text = P.stdout.readline() # Enter username

        out = username + '\n'
        b = out.encode('utf-8')
        P.stdin.write(b)
        P.stdin.flush()

        text = P.stdout.readline() # Enter url

        out = url + '\n'
        b = out.encode('utf-8')
        P.stdin.write(b)
        P.stdin.flush()

        text = P.stdout.readline() # Password generated.
        self.toplevel_launch(text)

        P.kill()

    def _retrieve_password_btn_clicked(self):

        username = self.entry_username.get()
        url = self.entry_url.get()
        masterPassword = self.entry_password.get()

        P = self.launch_master_password_program()

        text = P.stdout.readline() # Master password has already been created. Type 'a' to add a password or 'g' to get a password.

        P.stdin.write(b'g\n') # enter 'g'
        P.stdin.flush()

        text = P.stdout.readline()  # Enter master password.

        out = masterPassword + '\n'
        b = out.encode('utf-8')
        P.stdin.write(b)
        P.stdin.flush()

        masterPassword = None

        text = text.strip()
        text = P.stdout.readline() #Enter 'url' to look up accounts by URL. Enter 'user' to look up accounts by username.
        if text == b'Incorrect master password entered. Try again.':
            self.toplevel_launch(text)
            P.kill()
            return

        P.stdin.write(b'user\n') # enter 'user'
        P.stdin.flush()

        text = P.stdout.readline() #Enter username associated with password

        out = username + '\n'
        b = out.encode('utf-8')
        P.stdin.write(b)
        P.stdin.flush()

        text = P.stdout.readline() # url list
        print(text)
        text = P.stdout.readline() # Enter one of the above URLs to get its password
        print(text)

        out = url + '\n'
        b = out.encode('utf-8')
        P.stdin.write(b)
        P.stdin.flush()

        text = P.stdout.readline() # Password has been copied to the clipboard

        if text == b'':
            text = "This username/url combination does not exist in the database, try again!"

        self.toplevel_launch(text)
        P.kill()

    def _create_master_btn_clicked(self):

        masterPassword = self.entry_new.get()

        P = self.launch_master_password_program()

        text = P.stdout.readline() # Create master password by entering it now.
        text = text.strip()

        if text != b'Create master password by entering it now.':
            text = "Sorry MR. HackerMan!! A Master Password already exists! To create a new one you must erase all encrypted data by deleting the infofile and start fresh."
            self.toplevel_launch(text)
            masterPassword = None
            P.kill()
            return

        text = P.stdout.readline() # Master password must be at least 8 chars long, contain an upper case letter, a lower case letter, and a digit

        out = masterPassword + '\n'
        b = out.encode('utf-8')
        P.stdin.write(b)
        P.stdin.flush()

        masterPassword = None

        text = P.stdout.readline() # Master password created
        self.toplevel_launch(text)

        time.sleep(1);

        P.kill()

    def __init__(self, master):
        super().__init__(master)

        # main UI work #
        self.password_prompt = Label(self, text="Generate or Retrieve a Password?")
        self.password_prompt.grid(row=0, columnspan = 3)

        self.password_instruct = Label(self, text="Fill all fields and choose your option. Only fill input password if using encrypt input button.")
        self.password_instruct.grid(row=1, columnspan = 3)

        self.label_username = Label(self, text="Username")
        self.label_url = Label(self, text="URL")
        self.label_password = Label(self, text="Master Password")

        self.entry_username = Entry(self)
        self.entry_url = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_username.grid(row=2, sticky=E)
        self.label_url.grid(row=3, sticky=E)
        self.label_password.grid(row=4, sticky=E)
        self.entry_username.grid(row=2, column=1)
        self.entry_url.grid(row=3, column=1)
        self.entry_password.grid(row=4, column=1)

        self.input_password = Label(self, text="Input Your Own Password (optional)")
        self.input_password.grid(row=5, sticky=E)

        self.entry_input = Entry(self, show="*")
        self.entry_input.grid(row=5, column=1)

        self.generate_password_btn = Button(self, text="Generate Random Password", command=self._generate_password_btn_clicked)
        self.generate_password_btn.grid(row=6, column=0)

        self.input_password_btn = Button(self, text="Encrypt Input Password", command=self._input_password_btn_clicked)
        self.input_password_btn.grid(row=6, column=1)

        self.retrieve_password_btn = Button(self, text="Retrieve Password", command=self._retrieve_password_btn_clicked)
        self.retrieve_password_btn.grid(row=6, column=2)

        self.new_master_prompt = Label(self, text="First Time Here? Create a New Master Password!")
        self.new_master_prompt.grid(row=7, columnspan = 3)

        self.label_instructions = Label(self, text="Master password must be at least 8 chars long,")
        self.label_instructions.grid(row=8, columnspan=3)

        self.label_instructions2 = Label(self, text="contain an upper case letter, a lower case letter, and a digit")
        self.label_instructions2.grid(row=9, columnspan=3)

        self.label_new = Label(self, text="New Master Password")
        self.label_new.grid(row=10, sticky=E)

        self.entry_new = Entry(self, show="*")
        self.entry_new.grid(row=10, column=1)

        self.submit_button = Button(self, text="Submit", command=self._create_master_btn_clicked) ## PASS newMaster here
        self.submit_button.grid(row=11, columnspan=3)

        self.pack()

root = Tk()
lf = LoginFrame(root)
root.mainloop()
