from tkinter import *
from tkinter import ttk
from tkcalendar import *
from PIL import ImageTk, Image, ImageDraw
from ttkthemes import themed_tk as tk
from datetime import *
import time
from math import *
import random
from tkinter import messagebox
import os
import psycopg2
from student_dashboard import *
from forgotpassword import *
from otp_verification import *


class signin:
    def __init__ (self, window):
        self.window = window
        self.window.geometry("1366x720+0+0")
        self.window.title("Student Login Form")
        self.window.iconbitmap('images\\logo.ico')
        self.window.resizable(False, False)
        self.login_frame = PhotoImage(file="images/login_frame.png")
        self.image_panel = Label(self.window, image=self.login_frame)
        self.image_panel.pack(fill='both', expand='yes')


        self.log = PhotoImage(file="images/login.png")
        self.txt = "Student Login"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.window, text=self.txt, font=('yu gothic ui', 30, "bold"), bg="white",
                                fg='black',
                                bd=5,
                                relief=FLAT)
        self.heading.place(x=580, y=70, width=250)
        
        



        # ========================================================================
        # ============================Username====================================
        # ========================================================================

        self.username_label = Label(self.window, text="Username ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=495, y=220)

        self.username = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12), show="")
        self.username.place(x=530, y=255, width=380)  # trebuchet ms

        # ========================================================================
        # ============================Password====================================
        # ========================================================================

        self.password_label = Label(self.window, text="Password ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=495, y=335)

        self.password = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12),show="*")
        self.password.place(x=530, y=370, width=380)  # trebuchet ms

        # ========================================================================
        # ============================Login button================================
        # ========================================================================

        
        self.login_button = Button(self.window, image=self.log,
                                    font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2", command=self.click_enter_login)
        self.login_button.place(x=640, y=450)
        

        # ========================================================================
        # ============================Forgot password=============================
        # ========================================================================


        self.forgot_button = Button(self.window, text="Forgot Password ?",
                                    font=("yu gothic ui", 13, "bold underline"), fg="red", relief=FLAT,
                                    activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2", command=self.forgotpass)
        self.forgot_button.place(x=640, y=500)




    def click_enter_login(self):
        self.validation()

    def validation(self):
        username = self.username.get()
        passwrd = self.password.get()

        try:
            con = psycopg2.connect(user="postgres",
                            password="1911",
                            host="localhost",
                            database="unimanagement")
            cur = con.cursor()
            print("PostgreSQL server information")
            print(con.get_dsn_parameters(), "\n")

        
            query = "SELECT passwrd from studenttable WHERE username = '"+username+"';"
            cur.execute(query)
            con.commit()
            data = cur.fetchone()
            print(data)
            p = data[0]
            print(p)
            
        except BaseException as msg:
            print(msg)
        try:
            if self.username.get() == "":
                messagebox.showerror("Error", "Username can not be empty")
            elif self.password.get() == "":
                messagebox.showerror("Error", "Password can not be empty")
            elif self.password.get() != p:
                messagebox.showerror("Error", "Invalid Password")
                self.username.delete(0, END)
                self.password.delete(0, END)
            else:
                messagebox.showinfo("Success", "The login is successful")
                self.login_success()
                self.window.withdraw()
                #win.deiconify()
                
                

        except BaseException as msg:
            messagebox.showerror("Invalid", "Invalid Username or Password")


    def login_success(self):
        
        global page2
        newwindow = Toplevel()
        page2 = dashboard(newwindow)
        page2 = Clock(newwindow)


    def forgotpass(self):
        self.window.withdraw()
        global page2
        newwindow = Toplevel()
        page2 = OtpVerification(newwindow)





    def exit(self):
        self.window.deiconify()
        self.window.quit()

    


def win():
    window = tk.ThemedTk()
    window.get_themes()
    window.set_theme("arc")
    #img = ImageTk.PhotoImage(Image.open("images\\login_frame.png"))

    #login = ImageTk.PhotoImage(Image.open("images\\login.png"))

    #database_img = ImageTk.PhotoImage(Image.open("images\\connect_database.png"))

    signin(window)
    window.mainloop()


if __name__ == '__main__':
    win()
