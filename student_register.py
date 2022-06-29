from tkinter import *
from tkinter import ttk
from tkcalendar import *
from PIL import ImageTk, Image, ImageDraw
from ttkthemes import themed_tk as tk
from tkinter import messagebox
from datetime import *
import time
from math import *
import random
import psycopg2
import os

from student_login import signin

class RegisterForm:
    def __init__ (self, wind):
        self.window = wind
        self.window.title('LAIKIPIA LIBRARY MANAGEMENT SYSTEM')
        self.window.geometry('1366x786+0+0')
        self.window.config(bg="#f29844")
        self.window.iconbitmap('images\\logo.ico')
        self.window.resizable(False, False)
        self.manage_student_frame = ImageTk.PhotoImage \
            (file='images\\student_frame.png')

        # # win= Toplevel()
        # a= Frontend.manage_student.ManageStudent.list_of_tree
        # print(a)

        # ======================Backend connection=============

        # ======================Variables======================

        self.reg_frame = Frame(self.window, bg="#ffffff", width=1300, height=680)
        self.reg_frame.place(x=30, y=30)

        self.txt = "Student Registration Form"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]

        self.heading = Label(self.reg_frame, text=self.txt, font=('yu gothic ui', 30, "bold"), bg="white",
                                fg='black',
                                bd=5,
                                relief=FLAT)
        self.heading.place(x=350, y=0, width=600)
        

        self.cred_frame = LabelFrame(self.reg_frame, text="Account Details", bg="white", fg="#4f4e4d", height=140,
                                        width=800, borderwidth=2.4,
                                        font=("yu gothic ui", 13, "bold"))
        self.cred_frame.config(highlightbackground="red")
        self.cred_frame.place(x=100, y=100)

        # ========================================================================
        # ============================Key Bindings====================================
        # ========================================================================

        

        # ========================================================================
        # ============================Username====================================
        # ========================================================================

        self.username_label = Label(self.cred_frame, text="Username ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=10, y=10)

        self.username = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12))
        self.username.place(x=230, y=167, width=260)  # trebuchet ms

        self.username_line = Canvas(self.window, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=230, y=189)

        # ========================================================================
        # ============================Email=======================================
        # ========================================================================

        self.email_label = Label(self.cred_frame, text="Email ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.email_label.place(x=370, y=10)

        self.email = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12))
        self.email.place(x=555, y=167, width=350)  # trebuchet ms

        self.email_line = Canvas(self.window, width=350, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.email_line.place(x=555, y=189)

        # ========================================================================
        # ============================Password====================================
        # ========================================================================

        self.password_label = Label(self.cred_frame, text="Password ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=10, y=50)

        self.password = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12), show="*")
        self.password.place(x=230, y=207, width=260)  # trebuchet ms

        self.password_line = Canvas(self.window, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=230, y=230)

        # ========================================================================
        # ============================Confirm password============================
        # ========================================================================

        self.c_password_label = Label(self.cred_frame, text="Confirm Password ", bg="white", fg="#4f4e4d",
                                        font=("yu gothic ui", 13, "bold"))
        self.c_password_label.place(x=370, y=50)

        self.c_password = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                        font=("yu gothic ui semibold", 12), show="*")
        self.c_password.place(x=650, y=207, width=255)  # trebuchet ms

        self.c_password_line = Canvas(self.window, width=255, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.c_password_line.place(x=650, y=230)

        # =======================================================================
        # ========================frame for personal credentials ================
        # =======================================================================

        self.personal_frame = LabelFrame(self.reg_frame, text="Personal Details", bg="white", fg="#4f4e4d", height=265,
                                            width=800, borderwidth=2.4,
                                            font=("yu gothic ui", 13, "bold"))
        self.personal_frame.config(highlightbackground="red")
        self.personal_frame.place(x=100, y=260)

        # =======================================================================
        # ========================frame for information==========================
        # =======================================================================

        self.info_frame = LabelFrame(self.reg_frame, text="                                        "
                                                            "                         ",
                                        bg="white", fg="#4f4e4d", height=560,
                                        width=340, borderwidth=2.4,
                                        font=("yu gothic ui", 13, "bold"))
        self.info_frame.config(highlightbackground="red")
        self.info_frame.place(x=930, y=80)

        # ======================================
        self.logo_img = ImageTk.PhotoImage \
            (file='images\\cms_logo.png')

        self.logo = ttk.Label(self.info_frame, image=self.logo_img,
                                font=("yu gothic ui", 13, "bold"), background="white")
        self.logo.place(x=70, y=20)
        # ========================================
        self.author = ttk.Label(self.info_frame, text="Developed by:       Duncan    Kipkorir\n             Reg No: "
                                                        "N11/3/0536/018",
                                font=("yu gothic ui", 13, "bold"), background="white")
        self.author.place(x=20, y=470)

        # ========================================================================
        # ============================First name==================================
        # ========================================================================
        self.f_name_label = Label(self.personal_frame, text="First Name ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.f_name_label.place(x=10, y=10)

        self.f_name = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12))
        self.f_name.place(x=235, y=327, width=260)  # trebuchet ms

        self.f_name_line = Canvas(self.window, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.f_name_line.place(x=235, y=349)

        # ========================================================================
        # ============================Last name===================================
        # ========================================================================

        self.l_name_label = Label(self.personal_frame, text="Last Name ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.l_name_label.place(x=370, y=10)

        self.l_name = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12))
        self.l_name.place(x=595, y=327, width=315)  # trebuchet ms

        self.l_name_line = Canvas(self.window, width=315, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.l_name_line.place(x=595, y=349)

        # ========================================================================
        # ============================DOB=========================================
        # ========================================================================

        self.dob_label = Label(self.personal_frame, text="DOB ", bg="white", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
        self.dob_label.place(x=10, y=50)

        self.dob = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                font=("yu gothic ui semibold", 12))
        self.dob.insert(0, "mm/dd/yyyy")
        self.dob.place(x=190, y=367, width=305)
        self.dob.bind("<1>", self.pick_date)
        

        self.dob_line = Canvas(self.window, width=305, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.dob_line.place(x=190, y=389)

        # ========================================================================
        # ===========================Gender=======================================
        # ========================================================================
        style = ttk.Style()

        # style.map('TCombobox', selectbackground=[('readonly', 'grey')])
        self.window.option_add("*TCombobox*Listbox*Foreground", '#f29844')

        self.gender_label = Label(self.personal_frame, text="Gender ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.gender_label.place(x=370, y=50)

        self.gender = ttk.Combobox(self.window, font=('yu gothic ui semibold', 12, 'bold'), state='readonly',
                                            width=35)

        gender_list = ['Male', 'Female', 'Rather not say']
        self.gender['values'] = gender_list
        # self.gender_combo.current(0)
        self.gender.place(x=570, y=367)

        # self.gender_line = Canvas(self.window, width=315, height=1.5, bg="#bdb9b1", highlightthickness=0)
        # self.gender_line.place(x=595, y=369)

        # ========================================================================
        # ============================Address====================================
        # ========================================================================

        self.address_label = Label(self.personal_frame, text="Address ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.address_label.place(x=10, y=90)

        self.address = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12))
        self.address.place(x=215, y=407, width=280)  # trebuchet ms

        self.address_line = Canvas(self.window, width=280, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.address_line.place(x=215, y=429)

        # ========================================================================
        # ============================Contact no====================================
        # ========================================================================

        self.contact_label = Label(self.personal_frame, text="Contact No. ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.contact_label.place(x=370, y=90)

        self.contact = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12))
        self.contact.place(x=605, y=407, width=305)  # trebuchet ms

        self.contact_line = Canvas(self.window, width=305, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.contact_line.place(x=605, y=429)

        # ========================================================================
        # ============================Shift No====================================
        # ========================================================================

        self.department_label = Label(self.personal_frame, text="Department ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.department_label.place(x=10, y=130)

        self.department = ttk.Combobox(self.window, font=('yu gothic ui semibold', 11, 'bold'), state='readonly',
                                            width=26)
        department_list = ["Computing and Informatics", "Mathematics", "Chemistry and Biochemistry", "Biological and Biomedical Sciences Technology", "Commerce", "Economics", "Psychology, Councelling and Educational Foundations", "Curriculum and Educational Management"]
        self.department['values'] = department_list
        self.department.current(0)
        self.department.place(x=240, y=447)

        # ========================================================================
        # ============================Course enrolled=============================
        # ========================================================================

        self.register_as_label = Label(self.personal_frame, text="Course enrolled ", bg="white", fg="#4f4e4d",
                                        font=("yu gothic ui", 13, "bold"))
        self.register_as_label.place(x=370, y=130)

        self.register_as = ttk.Combobox(self.window, font=('yu gothic ui semibold', 12, 'bold'), state='readonly',
                                                width=31)

        register_as_list = ["Bachelor of Science(Computer science)", "Bachelor of Science(BICT)", "Statistics", "Business and Commerce", "Bachelor of Science(Mathematics and Economics)", "Bachelor of Science(Chemistry)"]
        self.register_as['values'] = register_as_list
        self.register_as.current(2)
        self.register_as.place(x=605, y=447)

        

        # ========================================================================
        # ============================Register options=====================================
        # ========================================================================

        self.options_frame = LabelFrame(self.reg_frame, text="Register Options", bg="white", fg="#4f4e4d", height=95,
                                        width=800, borderwidth=2.4,
                                        font=("yu gothic ui", 13, "bold"))
        self.options_frame.config(highlightbackground="red")
        self.options_frame.place(x=100, y=545)

        # ========================================================================
        # ============================Register options=====================================
        # ========================================================================
        self.submit_img = ImageTk.PhotoImage \
            (file='images\\submit.png')

        self.submit = Button(self.options_frame, image=self.submit_img,
                                font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                , borderwidth=0, background="white", cursor="hand2", command=self.validation)
        self.submit.place(x=90, y=10)

        self.clear_img = ImageTk.PhotoImage \
            (file='images\\clear.png')
        self.clear_button = Button(self.options_frame, image=self.clear_img,
                                    font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2", command=self.click_clear_button)
        self.clear_button.place(x=250, y=13)

        self.back_img = ImageTk.PhotoImage \
            (file='images\\back.png')
        self.back_button = Button(self.options_frame, image=self.back_img,
                                    font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2", command=self.back)
        self.back_button.place(x=410, y=13)

        self.exit_img = ImageTk.PhotoImage \
            (file='images\\exit.png')
        self.exit_button = Button(self.options_frame, image=self.exit_img,
                                    font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2", command=self.exit)
        self.exit_button.place(x=570, y=13)


        # ========================================================================
        # ========================username entry instruction=====================
        # ========================================================================

        self.forgot_ins_label = Label(self.window, text="* Please use your Registration Number as your username. ",
                                      bg="white", fg="red",
                                      font=("yu gothic ui", 13, "bold"))
        self.forgot_ins_label.place(x=240, y=100)
        
        
    def back(self):
        ask = messagebox.askyesnocancel("Confirm exit", "Are you sure you want to Exit\n University library Management System?")
        if ask is True:
            self.window.withdraw()
            os.system('main.py')


    def click_clear_button(self):
        """this will clear entire field to default when click on clear button"""
        self.username.delete(0, END)
        self.f_name.delete(0, END)
        self.l_name.delete(0, END)
        self.email.delete(0, END)
        self.password.delete(0, END)
        self.c_password.delete(0, END)
        self.dob.delete(0, END)
        self.gender.current(0)
        self.address.delete(0, END)
        self.contact.delete(0, END)
        self.shift_combo.current(0)
        self.batch_combo.current(0)
        self.course_combo.current(0)
        self.batch_combo.current(0)
        self.section_combo.current(0)


    def pick_date(self, event):
        """left click event is being handled when trying to add DOB"""
        self.date_win = tk.ThemedTk()
        self.date_win.get_themes()
        self.date_win.set_theme("arc")
        self.date_win.grab_set()
        self.date_win.title('Choose Date of Birth')
        self.date_win.geometry('250x220+500+370')
        self.cal = Calendar(self.date_win, selectmode="day", date_pattern="mm/dd/y")
        self.cal.place(x=0, y=0)

        self.okay_btn = ttk.Button(self.date_win, text="Okay", command=self.grab_date)
        self.okay_btn.place(x=80, y=180)

    def grab_date(self):
        """Grabs the date that being handled in pick_date() methods"""
        self.dob.delete(0, END)
        self.dob.config(fg="#6b6a69")
        self.dob.insert(0, self.cal.get_date())
        self.date_win.destroy()

    def exit(self):
        ask = messagebox.askyesnocancel("Confirm Exit", "Are you sure you want to Exit\n Student Registration Form?")
        if (ask == True):
            self.window.destroy()







    def click_enter_submit(self,events):
        """events for return or enter key is handled and validation method is called"""
        self.validation()

    def validation(self):
        """this will validate if the username and email of entry fields are already in database table named student or
        not if return True, error message is thrown displaying email/username already exists"""
        username = self.username.get()
        email = self.email.get()


        try:
            con = psycopg2.connect(user="postgres",
                        password="1911",
                        host="localhost",
                        database="unimanagement")
            cur = con.cursor()
            print("PostgreSQL server information")
            print(con.get_dsn_parameters(), "\n")

            query = "SELECT * from studenttable"
            cur.execute(query, [username, email])
            data = cur.fetchall()
            print(data)
            self.username_list = data
            self.email_list = data
            for values in data:
                print(values)
                user_data_list = values[0]
                self.username_list.append(user_data_list)
                email_data_list = values[1]
                self.email_list.append(email_data_list)
                #print(self.final_list)
                #print(self.data_list)
        except BaseException as msg:
            print(msg)

        if self.username.get() == "" or self.email.get() == "" or self.password.get() == "" \
                or self.f_name.get() == "" or self.l_name.get() == "" or self.dob.get() == "" \
                or self.address.get() == "" or self.contact.get() == "":
            messagebox.showwarning("Warning", "All Fields are Required\n Please fill all required fields")

        elif self.username.get() in self.username_list:
            messagebox.showerror("Already Exists", f"{self.username.get()} username Already Exists")
            self.username.delete(0, END)


        elif self.email.get() in self.email_list:
            messagebox.showerror("Already Exists", f"{self.email.get()} Email ID Already Exists")
            self.email.delete(0, END)


        elif self.password.get() != self.c_password.get():
            messagebox.showerror("Not Matched", "Password Does not Match")
            self.password.delete(0, END)
            self.c_password.delete(0, END)


        elif len(self.password.get()) < 8:
            messagebox.showerror("Password too short", "password should be atleast 6 characters")
            self.password.delete(0, END)
            self.c_password.delete(0, END)


        elif len(self.password.get()) > 12:
            messagebox.showerror("Password too long", "password should be atmost 12 characters")
            self.password.delete(0, END)
            self.c_password.delete(0, END)

        elif not any(char.isdigit() for char in self.password.get()):
            messagebox.showerror("Password too weak", "password should have atleast one number")
            self.password.delete(0, END)
            self.c_password.delete(0, END)


        elif not any(char.isupper() for char in self.password.get()):
            messagebox.showerror("Password too weak", "password should have atleast one Uppercase letter")
            self.password.delete(0, END)
            self.c_password.delete(0, END)


        elif not any(char.islower() for char in self.password.get()):
            messagebox.showerror("Password too weak", "password should have atleast one lowercase letter")
            self.password.delete(0, END)
            self.c_password.delete(0, END)


        


        else:
            self.click_submit()


    def ins_login(self):
        global page2
        newwindow = Toplevel()
        page2 = signin(newwindow)

        
        
        
        



    def click_submit(self):
        username = self.username.get()
        email = self.email.get()
        passwrd = self.password.get()
        c_password = self.c_password.get()
        first_name = self.f_name.get()
        last_name = self.l_name.get()
        d_o_b = self.dob.get()
        gender = self.gender.get()
        hom_address = self.address.get()
        contact_no = self.contact.get()

        
        insertstudent = "INSERT INTO "+studentTable+" VALUES('"+username+"','"+email+"','"+passwrd+"','"+first_name+"','"+last_name+"','"+d_o_b+"','"+gender+"', '"+hom_address+"', '"+contact_no+"')"
        #try:
        cur.execute(insertstudent)
        con.commit()
        messagebox.showinfo('Success',"student added successfully")
        #except:
        #messagebox.showinfo("Error","Can't add data into Database")
        self.window.withdraw()
        self.ins_login()
        
        
        print(username)
        print(email)
        print(passwrd)
        print(first_name)
        print(last_name)
        print(d_o_b)
        print(gender)
        print(hom_address)
        print(contact_no)

con = psycopg2.connect(user="postgres",
                        password="1911",
                        host="localhost",
                        database="unimanagement")
cur = con.cursor()
print("PostgreSQL server information")
print(con.get_dsn_parameters(), "\n")

studentTable = "studenttable"

#createtable= '''CREATE TABLE studenttable(
    #username VARCHAR,
    #email VARCHAR,
    #passwrd VARCHAR,
    #first_name VARCHAR,
    #last_name VARCHAR,
    #d_o_b VARCHAR,
    #gender VARCHAR,
    #hom_address VARCHAR,
    #contact_no Varchar);'''
#cur.execute(createtable)
#con.commit()

    







class Clock:
    """this creates an working clock using different module, and displayed those function onto
    a clock image which is static"""
    def __init__(self, win_):
        self.window = win_

        # ==========Clock image=============
        self.clock_label = Label(self.window, bg="white")  # ,bd=10, relief=RAISED)
        self.clock_label.place(x=1020, y=340, height=220, width=220)
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
        draw_img.line((center, 150 + 30 * sin(radians(h_)), 150 - 30 * cos(radians(h_))), fill="white", width=4)

        # ============= Clock Minutes Line===========
        draw_img.line((center, 150 + 50 * sin(radians(min_)), 150 - 50 * cos(radians(min_))), fill="white", width=3)

        # ============= Clock Seconds Line===========
        draw_img.line((center, 150 + 60 * sin(radians(sec_)), 150 - 60 * cos(radians(sec_))), fill="white", width=2)

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
    RegisterForm(window)
    Clock(window)
    window.mainloop()


if __name__ == '__main__':
    win()