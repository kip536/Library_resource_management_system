from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image, ImageDraw
from ttkthemes import themed_tk as tk
from datetime import *
import time
import random
from tkinter import messagebox
import psycopg2
import os


class admindashboard:
    def __init__ (self, window):
        self.window = window
        self.window.geometry("1366x720+0+0")
        self.window.title("ADNIN DASHBOARD")
        self.window.iconbitmap('images\\logo.ico')
        self.window.resizable(False, False)
        self.admin_dashboard_frame = PhotoImage(file="images/admin_frame.png")
        self.image_panel = Label(self.window, image=self.admin_dashboard_frame)
        self.image_panel.pack(fill='both', expand='yes')


        self.txt = "Welcome to Admin Dashboard"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.window, text=self.txt, font=('yu gothic ui', 30, "bold"), bg="white",
                                fg='black',
                                bd=5,
                                relief=FLAT)
        self.heading.place(x=350, y=26, width=550)


        # ========================================================================
        # ============================Date and time==============================
        # ========================================================================
        self.clock_image = PhotoImage(file="images/time.png")
        self.date_time_image = Label(self.window, image=self.clock_image, bg="white")
        self.date_time_image.place(x=35, y=45)

        self.date_time = Label(self.window)
        self.date_time.place(x=65, y=35)
        self.time_running()
        

        # ========================================================================
        # ============================Current user================================
        # ========================================================================
        self.current_user_image = PhotoImage(file="images/current_user.png")
        self.current_user_label = Label(self.window, image=self.current_user_image, bg="white")
        self.current_user_label.place(x=1000, y=47)

        self.current_user = Label(self.window, bg="white",
                                    font=("yu gothic ui", 10, "bold"),fg="green")
        self.current_user.place(x=1030, y=48)

        # ========================================================================
        # ============================Home button====================================
        # ========================================================================
        self.home = PhotoImage(file="images/home.png")
        self.home_button = Button(self.window, image=self.home,
                                    font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2", command=self.click_home)

        self.home_button.place(x=43, y=113)
        

        # ========================================================================
        # ============================Manage button===============================
        # ========================================================================
        self.manage = PhotoImage(file="images/manage.png")
        self.manage_button = Button(self.window, image=self.manage,
                                    font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2", command=self.library)

        self.manage_button.place(x=41, y=233)

        # ========================================================================
        # ============================View button===============================
        # ========================================================================
        self.view = PhotoImage(file="images/view.png")
        self.view_button = Button(self.window, image=self.view,
                                    font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2", command=self.click_view)
        self.view_button.place(x=41, y=353)

        # ========================================================================
        # ============================Settings button===============================
        # ========================================================================
        self.setting = PhotoImage(file="images/setting.png")
        self.setting_button = Button(self.window, image=self.setting,
                                        font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                        , borderwidth=0, background="white", cursor="hand2")
        self.setting_button.place(x=41, y=473)

        # ========================================================================
        # ============================Exit button===============================
        # ========================================================================
        self.exit = PhotoImage(file="images/exit_button.png")
        self.exit_button = Button(self.window, image=self.exit,
                                    font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2", command=self.click_exit)
        self.exit_button.place(x=41, y=593)

        # ========================================================================
        # ============================Logout button===============================
        # ========================================================================
        self.logout = PhotoImage(file="images/logout.png")
        self.logout_button = Button(self.window, image=self.logout,
                                    font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2", command= self.signout)
        self.logout_button.place(x=1241, y=50)
        
        
    def signout(self):
        ask = messagebox.askyesnocancel("Confirm Logout", "Are you sure you want to Logout\n University library Management System?")
        if ask is True:
            self.window.withdraw()
            os.system('main.py')
    


    def click_home(self):
        """set to default home tab where details like no. of students, employees, department shows """
        home_frame = Frame(self.window)
        home_frame.place(x=145, y=105, height=576, width=1181)

        self.home_dashboard_frame = ImageTk.PhotoImage \
            (file='images\\home_frame1.png')
        self.home_panel = Label(home_frame, image=self.home_dashboard_frame, bg="white")
        self.home_panel.pack(fill='both', expand='yes')

        try:
            con = psycopg2.connect(user="postgres",
                        password="1911",
                        host="localhost",
                        database="unimanagement")
            cur = con.cursor()
            print("PostgreSQL server information")
            print(con.get_dsn_parameters(), "\n")

            query = "SELECT COUNT(*) FROM studenttable;"
            cur.execute(query)
            data = cur.fetchall()
            global no_students
            for value in data:
                no_students = value[0]

            total_students = Label(home_frame, text=f" TOTAL STUDENTS\n {no_students}\n",
                                   font=("yu gothic ui", 30, "bold"),
                                   background="white", fg='#e67c0b')
            total_students.place(x=175, y=90)

        
            con = psycopg2.connect(user="postgres",
                        password="1911",
                        host="localhost",
                        database="booktable")
            cur = con.cursor()
            print("PostgreSQL server information")
            print(con.get_dsn_parameters(), "\n")

            query = "SELECT COUNT(*) FROM booktable;"
            cur.execute(query)
            data = cur.fetchall()
            global no_books
            for value in data:
                no_books = value[0]

            total_students = Label(home_frame, text=f" TOTAL BOOKS\n {no_books}\n",
                                   font=("yu gothic ui", 30, "bold"),
                                   background="white", fg='#e67c0b')
            total_students.place(x=700, y=90)



            con = psycopg2.connect(user="postgres",
                        password="1911",
                        host="localhost",
                        database="booktable")
            cur = con.cursor()
            print("PostgreSQL server information")
            print(con.get_dsn_parameters(), "\n")

            query = "SELECT COUNT(*) FROM booktable WHERE status = 'Available';"
            cur.execute(query)
            data = cur.fetchall()
            #global no_books
            for value in data:
                books_available = value[0]

            total_students = Label(home_frame, text=f" BOOKS AVAILABLE\n {books_available}\n",
                                   font=("yu gothic ui", 30, "bold"),
                                   background="white", fg='#e67c0b')
            total_students.place(x=170, y=340)


            con = psycopg2.connect(user="postgres",
                        password="1911",
                        host="localhost",
                        database="booktable")
            cur = con.cursor()
            print("PostgreSQL server information")
            print(con.get_dsn_parameters(), "\n")

            query = "SELECT COUNT(*) FROM books_issued;"
            cur.execute(query)
            data = cur.fetchall()
            #global no_books
            for value in data:
                books_available = value[0]

            total_students = Label(home_frame, text=f" BOOKS ISSUED\n {books_available}\n",
                                   font=("yu gothic ui", 30, "bold"),
                                   background="white", fg='#e67c0b')
            total_students.place(x=700, y=340)

            

        except BaseException as msg:
            print(msg)


    def library(self):
            os.system('library.py')


    def click_view(self):
        """ Displays partial data into tree view of students, employees, departments, courses when clicked view tab
        on interface """
        view_frame = Frame(self.window, bg="white")
        view_frame.place(x=145, y=105, height=576, width=1181)

        self.view_dashboard_frame = ImageTk.PhotoImage \
            (file='images\\view_frame.png')
        self.view_panel = Label(view_frame, image=self.view_dashboard_frame, bg="white")
        self.view_panel.pack(fill='both', expand='yes')

        self.student_view_label = Label(view_frame, text=" Students Information ", bg="white", fg="#4f4e4d",
                                        font=("yu gothic ui", 13, "bold"))
        self.student_view_label.place(x=170, y=6)

        self.view_student_frame = Frame(view_frame, bg="white")
        self.view_student_frame.place(x=10, y=40, height=250, width=575)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=('yu gothic ui', 10, "bold"), foreground="red")
        style.configure("Treeview", font=('yu gothic ui', 9, "bold"), foreground="#f29b0f")

        scroll_y = Scrollbar(self.view_student_frame, orient=VERTICAL)
        scroll_x = Scrollbar(self.view_student_frame, orient=HORIZONTAL)
        self.view_student_tree = ttk.Treeview(self.view_student_frame,
                                              columns=(
                                                  "f_name", "l_name", "email", "contact_no"),
                                              xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.view_student_tree.xview)
        scroll_y.config(command=self.view_student_tree.yview)

        # ==========================TreeView Heading====================
        self.view_student_tree.heading("f_name", text="FIRST NAME")
        self.view_student_tree.heading("l_name", text="LAST NAME")
        self.view_student_tree.heading("email", text="EMAIL")
        self.view_student_tree.heading("contact_no", text="PHONE NO.")
        self.view_student_tree["show"] = "headings"

        # ==========================TreeView Column====================
        self.view_student_tree.column("f_name", width=150)
        self.view_student_tree.column("l_name", width=150)
        self.view_student_tree.column("email", width=150)
        self.view_student_tree.column("contact_no", width=100)
        self.view_student_tree.pack(fill=BOTH, expand=1)

        self.view_student_information()




        self.student_view_label = Label(view_frame, text=" Books Information ", bg="white", fg="#4f4e4d",
                                        font=("yu gothic ui", 13, "bold"))
        self.student_view_label.place(x=800, y=6)

        self.view_student_frame = Frame(view_frame, bg="white")
        self.view_student_frame.place(x=600, y=40, height=250, width=575)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=('yu gothic ui', 10, "bold"), foreground="red")
        style.configure("Treeview", font=('yu gothic ui', 9, "bold"), foreground="#f29b0f")

        scroll_y = Scrollbar(self.view_student_frame, orient=VERTICAL)
        scroll_x = Scrollbar(self.view_student_frame, orient=HORIZONTAL)
        self.view_student_tree = ttk.Treeview(self.view_student_frame,
                                              columns=(
                                                  "bid", "title", "author", "status"),
                                              xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.view_student_tree.xview)
        scroll_y.config(command=self.view_student_tree.yview)

        # ==========================TreeView Heading====================
        self.view_student_tree.heading("bid", text="BOOK ID")
        self.view_student_tree.heading("title", text="BOOK TITLE")
        self.view_student_tree.heading("author", text="AUTHOR")
        self.view_student_tree.heading("status", text="STATUS")
        self.view_student_tree["show"] = "headings"

        # ==========================TreeView Column====================
        self.view_student_tree.column("bid", width=150)
        self.view_student_tree.column("title", width=150)
        self.view_student_tree.column("author", width=150)
        self.view_student_tree.column("status", width=100)
        self.view_student_tree.pack(fill=BOTH, expand=1)

        self.view_book_information()




    def view_book_information(self):
        """fetched data of students from database and inserted required index to student tree view"""
        try:
            con = psycopg2.connect(user="postgres",
                            password="1911",
                            host="localhost",
                            database="booktable")
            cur = con.cursor()
            print("PostgreSQL server information")
            print(con.get_dsn_parameters(), "\n")

            query = "SELECT * from booktable"
            cur.execute(query)
            data = cur.fetchall()
            self.a = Label(self.window)
            data_list = data
            print(data)
            self.view_student_tree.delete(*self.view_student_tree.get_children())
            for values in data:
                data_list = [values[0], values[1], values[2], values[3]]
                print(data_list)
                self.view_student_tree.insert('', END, values=data_list)



        except BaseException as msg:
            print(msg)






    def view_student_information(self):
        """fetched data of students from database and inserted required index to student tree view"""
        try:
            con = psycopg2.connect(user="postgres",
                            password="1911",
                            host="localhost",
                            database="unimanagement")
            cur = con.cursor()
            print("PostgreSQL server information")
            print(con.get_dsn_parameters(), "\n")

            query = "SELECT * from studenttable"
            cur.execute(query)
            data = cur.fetchall()
            self.a = Label(self.window)
            data_list = data
            print(data)
            self.view_student_tree.delete(*self.view_student_tree.get_children())
            for values in data:
                data_list = [values[3], values[4], values[1], values[8]]
                print(data_list)
                self.view_student_tree.insert('', END, values=data_list)



        except BaseException as msg:
            print(msg)

    def click_exit(self):
        """:returns True to terminates the program if chosen yes"""
        ask = messagebox.askyesnocancel("Confirm Exit", "Are you sure you want to Exit\n College Management System?")
        if ask is True:
            self.window.quit()




    def time_running(self):
        """ displays the current date and time which is shown at top left corner of admin dashboard"""
        self.time = time.strftime("%H:%M:%S")
        self.date = time.strftime('%Y/%m/%d')
        concated_text = f"  {self.time} \n {self.date}"
        self.date_time.configure(text=concated_text, font=("yu gothic ui", 13, "bold"), relief=FLAT
                                , borderwidth=0, background="white", foreground="black")
        self.date_time.after(100, self.time_running)


def win():
    window = tk.ThemedTk()
    window.get_themes()
    window.set_theme("arc")
    img = ImageTk.PhotoImage(Image.open("images\\admin_frame.png"))

    clock = ImageTk.PhotoImage(Image.open("images/time.png"))

    c_user = ImageTk.PhotoImage(Image.open("images/current_user.png"))

    home = ImageTk.PhotoImage(Image.open("images\\home.png"))

    manage = ImageTk.PhotoImage(Image.open("images\\manage.png"))

    view = ImageTk.PhotoImage(Image.open("images\\view.png"))

    settings = ImageTk.PhotoImage(Image.open("images\\setting.png"))

    exit = ImageTk.PhotoImage(Image.open("images\\exit_button.png"))

    logout = ImageTk.PhotoImage(Image.open("images\\logout.png"))

    admindashboard(window)
    window.mainloop()


if __name__ == '__main__':
    win()
