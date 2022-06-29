def click_enter_login(self, events):
    self.validation()

def validattion(self):
    username = username.get()
    password = password.get()

    try:
        con = psycopg2.connect(user="postgres",
                        password="1911",
                        host="localhost",
                        database="unimanagement")
        cur = con.cursor()
        print("PostgreSQL server information")
        print(con.get_dsn_parameters(), "\n")

    
        find_user = "SELECT * FROM studenttable WHERE username = ? and passwrd = ?"
        cur.execute(find_user, [username, password])
        results = cur.fetchall()
        if results:
            messagebox.showinfo("Login Page", "The login is successful")

        else:
            messagebox.showerror("Error", "Incorrect username or password.")

    except BaseException as msg:
            print(msg)