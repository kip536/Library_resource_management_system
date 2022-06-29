from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import *
from PIL import ImageTk, Image, ImageDraw
from ttkthemes import themed_tk as tk
from datetime import *
import time
from math import *
import random
from tkinter import messagebox
from student_login import *
from instructor_login import *
from admin_login import *
from student_register import *
from instructor_register import *






class welcome():
    def __init__ (self, window):
        self.window = window
        self.window.geometry("1366x720+0+0")
        self.window.title("WELCOME TO LAIKIPIA LIBRARY MANAGEMENT SYSTEM")
        self.window.iconbitmap('images\\logo.ico')
        self.window.resizable(False, False)
        self.background_img = PhotoImage(file="images/welcome_frame.png")
        self.image_panel = Label(self.window, image=self.background_img)
        self.image_panel.pack(fill='both', expand='yes')



        self.student = PhotoImage(file="images/student.png")
        self.student_button = Button(self.window, image=self.student, relief=FLAT, borderwidth=0,
                                        activebackground="white", bg="white",cursor="hand2",command=self.student_login)
        self.student_button.place(x=244, y=210)

        self.instructor = PhotoImage(file="images/instructor.png")
        self.instructor_button = Button(self.window, image=self.instructor, relief=FLAT, borderwidth=0,
                                        activebackground="white", bg="white",cursor="hand2", command=self.instructor_login)
        self.instructor_button.place(x=609, y=210)

        self.admin = PhotoImage(file="images/admin.png")
        self.admin_button = Button(self.window, image=self.admin, relief=FLAT, borderwidth=0,
                                        activebackground="white", bg="white",cursor="hand2", command=self.admin_login)
        self.admin_button.place(x=969, y=210)

        self.reg_student_button = Button(self.window, image=self.student, relief=FLAT, borderwidth=0,
                                        activebackground="white", bg="white",cursor="hand2", command=self.student_register)
        self.reg_student_button.place(x=419, y=545)

        self.reg_instructor_button = Button(self.window, image=self.instructor, relief=FLAT, borderwidth=0,
                                            activebackground="white", bg="white",cursor="hand2", command=self.instructor_register)
        self.reg_instructor_button.place(x=794, y=545)


    
    def student_login(self):
        self.window.withdraw()
        global page2
        newwindow = Toplevel()
        page2 = signin(newwindow)   
        
        

    def instructor_login(self):
        self.window.withdraw()
        global page2
        newwindow = Toplevel()
        page2 = instructorlogin(newwindow)

    def admin_login(self):
        self.window.withdraw()
        global page2
        newwindow = Toplevel()
        page2 = admin_signin(newwindow)

    def student_register(self):
        self.window.withdraw()
        global page2
        newwindow = Toplevel()
        page2 = RegisterForm(newwindow)
        page2 = Clock(newwindow)

    def instructor_register(self):
        self.window.withdraw()
        global page2
        newwindow = Toplevel()
        page2 = instructorregister(newwindow)
        page2 = Clock(newwindow)





def win():
    window = tk.ThemedTk()
    window.get_themes()
    window.set_theme("arc")
    
    #img = ImageTk.PhotoImage(Image.open("images\\welcome_frame.png"))

    #instructor = ImageTk.PhotoImage(Image.open("images\\instructor.png"))

    #student = ImageTk.PhotoImage(Image.open("images\\student.png"))

    #admin = ImageTk.PhotoImage(Image.open("images\\admin.png"))

    welcome(window)
    
    window.mainloop()


if __name__ == '__main__':
    win()