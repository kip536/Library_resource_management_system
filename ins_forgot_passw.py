from tkinter import *
from PIL import ImageTk
from ttkthemes import themed_tk as tk
from datetime import *
import time
import smtplib
import random
from tkinter import messagebox
import psycopg2
#from student_login import *
import os



class forgotPassword:
    """Allows user to forgot password from GUI, Let user choose new password, and
     update those password to the database searching from email address that the user
     used in the verification process, after successful password changes, an email
     notification about recent password changed is sent to email address of that user
     with time and date when the password was changed."""

    def __init__(self, window):
        self.window = window
        self.window.geometry("1366x720+0+0")
        self.window.title("Choose New Password Form")
        self.window.iconbitmap('images\\logo.ico')
        self.window.resizable(False, False)

    

        self.login_frame = PhotoImage(file='images\\forgot_password_frame.png')
        self.image_panel = Label(self.window, image=self.login_frame)
        # self.image_panel = Label(self.window, image=ph)
        # self.image_panel.image = ph
        self.image_panel.pack(fill='both', expand='yes')

        self.txt = "Choose New Password"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.window, text=self.txt, font=('yu gothic ui', 30, "bold"), bg="white",
                             fg='black',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=470, y=70, width=450)


        # ========================================================================
        # ============================Email========================================
        # ========================================================================

        #self.change_img = ImageTk.PhotoImage \
            #(file='images\\change_password.png')

        self.email_label = Label(self.window, bg="white", fg="#4f4e4d",
                                 font=("yu gothic ui", 13, "bold"))
        self.email_label.place(x=485, y=160, width=430, height=100)

        self.email_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                 font=("yu gothic ui semibold", 12))
        self.email_entry.place(x=530, y=210, width=380)  # trebuchet ms

        # ========================================================================
        # ============================Password====================================
        # ========================================================================

        self.password_label = Label(self.window, text="New Password ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=495, y=295)

        self.password_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12), show="*")
        self.password_entry.place(x=530, y=325, width=350)  # trebuchet ms

        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_button = Button(self.window, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=890, y=330)

        # ========================================================================
        # ============================Confirm Password============================
        # ========================================================================

        self.c_password_label = Label(self.window, text="Confirm Password ", bg="white", fg="#4f4e4d",
                                      font=("yu gothic ui", 13, "bold"))
        self.c_password_label.place(x=495, y=410)

        self.c_password_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                      font=("yu gothic ui semibold", 12), show="*")
        self.c_password_entry.place(x=530, y=440, width=380)  # trebuchet ms

        # ========================================================================
        # ============================Submit button================================
        # ========================================================================

        self.submit = ImageTk.PhotoImage \
            (file='images\\submit.png')

        self.submit_button = Button(self.window, image=self.submit,
                                    font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2", command=self.validation)
        self.submit_button.place(x=500, y=520)

        # ========================================================================
        # ============================Login button================================
        # ========================================================================

        self.login = ImageTk.PhotoImage \
            (file='images\\login.png')

        self.login_button = Button(self.window, image=self.login,
                                   font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                   , borderwidth=0, background="white", cursor="hand2")
        self.login_button.place(x=640, y=523)

        # ========================================================================
        # ============================Exit button================================
        # ========================================================================

        self.exit_img = ImageTk.PhotoImage \
            (file='images\\exit.png')
        self.exit_button = Button(self.window, image=self.exit_img,
                                  font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2", command=self.click_exit)
        self.exit_button.place(x=783, y=523)

        # ========================================================================
        # ========================Forgot password instruction=====================
        # ========================================================================

        self.forgot_ins_label = Label(self.window, text="* Please enter new password\n and confirm your email ",
                                      bg="white", fg="#4f4e4d",
                                      font=("yu gothic ui", 13, "bold"))
        self.forgot_ins_label.place(x=575, y=593)



    def show(self):
        """allow user to show the password in password field"""
        self.hide_button = Button(self.window, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=890, y=330)
        self.password_entry.config(show='')

    def hide(self):
        """allow user to hide the password in password field"""
        self.show_button = Button(self.window, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=890, y=330)
        self.password_entry.config(show='*')



    def validation(self):
        """Validates the entry fields that they should not be empty and new password and confirm password should match,
         if it is not empty and both the password match then it allows user to change their password"""
        try:
            con = psycopg2.connect(user="postgres",
                            password="1911",
                            host="localhost",
                            database="unimanagement")
            cur = con.cursor()
            print("PostgreSQL server information")
            print(con.get_dsn_parameters(), "\n")

        except BaseException as msg:
            print(msg)

        if self.email_entry.get() == "":
            messagebox.showerror("Error", "Email can not be empty")

        elif self.password_entry.get() == "":
            messagebox.showerror("Error", "New Password can not be empty")

        elif self.c_password_entry.get() == "":
            messagebox.showerror("Error", "You must confirm Password")
        elif self.password_entry.get() != self.c_password_entry.get():
            messagebox.showerror("Error", "Confirm Password Does not matched")

        else:
            self.update_password()

    def update_password(self):
        """ this will updates the new password to the database where email address is that it was fetched while
        confirming the password. after successful password change, an email notification about password change
        is sent to the user email with password changed time and date"""
        email = self.email_entry.get()
        passwrd = self.password_entry.get()
        try:
            con = psycopg2.connect(user="postgres",
                            password="1911",
                            host="localhost",
                            database="unimanagement")
            cur = con.cursor()
            print("PostgreSQL server information")
            print(con.get_dsn_parameters(), "\n")

            query = "UPDATE employeetable SET passwrd = '"+passwrd+"' WHERE email = '"+email+"'"
            cur.execute(query)
            con.commit()
            # print(values)
            messagebox.showinfo("Success", "Password Updated Successfully")

            # print("i am pass")
            

            c_time = time.strftime('%H:%M:%S')
            c_date = time.strftime('%Y/%m/%d')
            print(c_time)
            print(c_date)

            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

            server.login("duncankipkorir99@gmail.com", "ewdxvnwvxxcfuizj")

            server.sendmail("duncankipkorir99@gmail.com", f"{self.email_entry.get()}", f"Subject: Password reset "
                                                                                 f"Password changed \n\n "
                                                                                 f"Your "
                                                                                 f" Password for University library Management was "
                                                                                 f"Changed Recently "
                                                                                 f" at Time  {c_time}"
                                                                                 f" at Date  {c_date}")
            server.quit()
            # print(values)
            self.clear_update_password()
            self.click_login()

        except BaseException as msg:
            print(msg)
            messagebox.showerror("Error", "There is some error Submitting Credentials ")



    def clear_update_password(self):
        """it clears the entry fields whenever called"""
        self.email_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.c_password_entry.delete(0, END)

    def click_login(self):
        self.window.withdraw()
        """:returns login form when clicked"""
        os.system('instructor_login.py')


    def click_exit(self):
        """:returns True to terminates the program if chosen yes"""
        ask = messagebox.askyesnocancel("Confirm Exit", "Are you sure you want to Exit\n College Management System?")
        if ask is True:
            self.window.quit()




def win():
    window = tk.ThemedTk()
    window.get_themes()
    window.set_theme("arc")
    forgotPassword(window)
    window.mainloop()


if __name__ == '__main__':
    win()
