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
from admin_dashboard import *


class admin_signin:
    def __init__ (self, window):
        self.window = window
        self.window.geometry("1366x720+0+0")
        self.window.title("Admin Login Form")
        self.window.iconbitmap('images\\logo.ico')
        self.window.resizable(False, False)
        self.login_frame = PhotoImage(file="images/login_frame.png")
        self.image_panel = Label(self.window, image=self.login_frame)
        self.image_panel.pack(fill='both', expand='yes')


        self.log = PhotoImage(file="images/login.png")
        self.txt = "Admin Login"
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
                                    , borderwidth=0, background="white", cursor="hand2", command=self.click_login)
        self.login_button.place(x=640, y=450)

        # ========================================================================
        # ============================Forgot password=============================
        # ========================================================================


        self.forgot_button = Button(self.window, text="Forgot Password ?",
                                    font=("yu gothic ui", 13, "bold underline"), fg="red", relief=FLAT,
                                    activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2")
        self.forgot_button.place(x=640, y=500)



    def click_login(self):
        u = self.username.get()
        p = self.password.get()

        if u == str('dun') and p == str(1911):
            
            messagebox.showinfo("Login Page", "The login is successful")
            self.window.withdraw()
            global page2
            newwindow = Toplevel()
            page2 = admindashboard(newwindow)
            
        else:
            messagebox.showerror("Error", "Incorrect username or password.")
        self.username.delete(0, END)
        self.password.delete(0, END)






def win():
    window = tk.ThemedTk()
    window.get_themes()
    window.set_theme("arc")
    img = ImageTk.PhotoImage(Image.open("images\\login_frame.png"))

    login = ImageTk.PhotoImage(Image.open("images\\login.png"))

    #database_img = ImageTk.PhotoImage(Image.open("images\\connect_database.png"))

    admin_signin(window)
    window.mainloop()


if __name__ == '__main__':
    win()
