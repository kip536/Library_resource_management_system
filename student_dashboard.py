from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image, ImageDraw
from ttkthemes import themed_tk as tk
from datetime import *
import time
from math import *
import random
from tkinter import messagebox
import psycopg2
import os






class dashboard:
    def __init__ (self, window):
        self.window = window
        self.window.geometry("1366x720+0+0")
        self.window.title("STUDENT DASHBOARD")
        self.window.iconbitmap('images\\logo.ico')
        self.window.resizable(False, False)
        self.admin_dashboard_frame = PhotoImage(file="images/student_frame.png")
        self.image_panel = Label(self.window, image=self.admin_dashboard_frame)
        self.image_panel.pack(fill='both', expand='yes')


        self.exit = PhotoImage(file="images/exit_button.png")
        self.txt = "Welcome to student Dashboard"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.window, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="white",
                                fg='black',
                                bd=5,
                                relief=FLAT)
        self.heading.place(x=350, y=35, width=550)


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
        # ============================View all===============================
        # ========================================================================
        self.viewall = PhotoImage(file="images/view_all1.png")
        self.viewall_button = Button(self.window, image=self.viewall,
                                    font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2", command=self.view_all)
        self.viewall_button.place(x=90, y=200)


        # ========================================================================
        # ============================Exit button===============================
        # ========================================================================
        
        self.exit_button = Button(self.window, image=self.exit,
                                    font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2", command=self.click_exit)
        self.exit_button.place(x=45, y=593)


        # ========================================================================
        # ============================Logout button===============================
        # ========================================================================
        self.logout = PhotoImage(file="images/logout.png")
        self.logout_button = Button(self.window, image=self.logout,
                                    font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2", command= self.signout)
        self.logout_button.place(x=250, y=620)
        
        
    def signout(self):
        ask = messagebox.askyesnocancel("Confirm Logout", "Are you sure you want to Logout\n University library Management System?")
        if ask is True:
            self.window.withdraw()
            os.system('main.py')




    def view_all(self):
        self.student_view_label = Label(self.window, text=" Books Information ", bg="white", fg="#4f4e4d",
                                        font=("yu gothic ui", 18, "bold"))
        self.student_view_label.place(x=750, y=105)

        self.view_student_frame = Frame(self.window, bg="white")
        self.view_student_frame.place(x=405, y=140, height=520, width=900)

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







    def click_exit(self):
        """ Allows user to terminates the program when chosen yes"""
        self.window.deiconify()
        ask = messagebox.askyesnocancel("Confirm Exit", "Are you sure you want to Exit\n Student Registration Form?")
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



class Clock:
    """this creates an working clock using different module, and displayed those function onto
    a clock image which is static"""
    def __init__(self, win_):
        self.window = win_

        # ==========Clock image=============
        self.clock_label = Label(self.window, bg="white")  # ,bd=10, relief=RAISED)
        self.clock_label.place(x=90, y=340, height=220, width=220)
        # self.clock_image()
        self.clock_usable()

    def clock_image(self, h_, min_, sec_):
        """this will draw a new image having hight, width and it takes parameter for hour, minutes and seconds"""
        clock_img = Image.new("RGB", (300, 300), (255, 255, 255))
        draw_img = ImageDraw.Draw(clock_img)
        bg = Image.open("images\\clockNew.jpg")
        bg = bg.resize((200, 200), Image.ANTIALIAS)
        clock_img.paste(bg, (50, 50))

        center = 150, 150
        # ============= Clock hour Line===========
        draw_img.line((center, 150 + 30 * sin(radians(h_)), 150 - 30 * cos(radians(h_))), fill="green", width=4)

        # ============= Clock Minutes Line===========
        draw_img.line((center, 150 + 50 * sin(radians(min_)), 150 - 50 * cos(radians(min_))), fill="blue", width=3)

        # ============= Clock Seconds Line===========
        draw_img.line((center, 150 + 60 * sin(radians(sec_)), 150 - 60 * cos(radians(sec_))), fill="red", width=2)

        # ============= Clock Eclipse===========
        draw_img.ellipse((147, 147, 153, 153), fill="black")
        clock_img.save(
            "images\\clock_new_image.png")

    def clock_usable(self):
        """this make clock to movable by calling it recursively after every 200 ms """
        hour = datetime.now().time().hour
        minutes = datetime.now().time().minute
        seconds = datetime.now().time().second
        # print(hour, minutes, seconds)
        h_ = (hour / 12) * 360
        min_ = (minutes / 60) * 360
        sec_ = (seconds / 60) * 360
        # print(h_, min_, sec_)
        self.clock_image(h_, min_, sec_)
        try:
            self.show_img = ImageTk.PhotoImage(file="images\\clock_new_image.png")
        except:
            pass
        self.clock_label.config(image=self.show_img)
        self.clock_label.after(200, self.clock_usable)



def win():
    window = tk.ThemedTk()
    window.get_themes()
    window.set_theme("arc")
    img = ImageTk.PhotoImage(Image.open("images\\student_frame.png"))

    clock = ImageTk.PhotoImage(Image.open("images/time.png"))

    c_user = ImageTk.PhotoImage(Image.open("images/current_user.png"))

    home = ImageTk.PhotoImage(Image.open("images\\home.png"))

    manage = ImageTk.PhotoImage(Image.open("images\\manage.png"))

    view = ImageTk.PhotoImage(Image.open("images\\view.png"))

    settings = ImageTk.PhotoImage(Image.open("images\\setting.png"))

    exit = ImageTk.PhotoImage(Image.open("images\\exit_button.png"))

    logout = ImageTk.PhotoImage(Image.open("images\\logout.png"))

    dashboard(window)
    Clock(window)
    window.mainloop()


if __name__ == '__main__':
    win()