from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import psycopg2







def bookRegister():
    
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
    status = status.lower()
    
    insertBooks = "INSERT INTO "+bookTable+" VALUES('"+bid+"','"+title+"','"+author+"','"+status+"')"
    try:
        con = psycopg2.connect(user="postgres",
                            password="1911",
                            host="localhost",
                            database="booktable")
        cur = con.cursor()
        print("PostgreSQL server information")
        print(con.get_dsn_parameters(), "\n")
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success',"Book added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    print(bid)
    print(title)
    print(author)
    print(status)

    root.destroy()
    
def addBook(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code

    


    # Enter Table Names here
    bookTable = "booktable" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Title
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # Book Author
    lb3 = Label(labelFrame,text="Author : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    # Book Status
    lb4 = Label(labelFrame,text="Status(Avail/issued) : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=confirm)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)



def confirm():
    bid = bookInfo1.get()
    try:
        con = psycopg2.connect(user="postgres",
                            password="1911",
                            host="localhost",
                            database="booktable")
        cur = con.cursor()
        print("PostgreSQL server information")
        print(con.get_dsn_parameters(), "\n")

        query = "SELECT * from booktable"
        cur.execute(query, [bid])
        data = cur.fetchall()
        print(data)
        bid_list = data
        email_list = data
        for values in data:
            print(values)
            bid_data_list = values[0]
            bid_list.append(bid_data_list)
            email_data_list = values[1]
            email_list.append(email_data_list)
    except BaseException as msg:
        print(msg)

    

    if bookInfo1.get() in bid_list:
        messagebox.showerror("Already Exists", f"{bookInfo1.get()} Book ID Already Exists")
        bookInfo1.delete(0, END)

    elif bookInfo1.get() == "" or bookInfo2.get() == "" or bookInfo3.get() == "" \
            or bookInfo4.get() == "":
        messagebox.showwarning("Warning", "All Fields are Required\n Please fill all required fields")


    else:
        bookRegister()

    
    root.mainloop()