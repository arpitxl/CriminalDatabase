from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
import sqlite3

dis = Tk()
dis.title('Criminal Database Management')
dis.geometry('1000x700')
dis.resizable(0, 0)


def sogs():
    f2 = Frame(bg='#aaaaff')
    f2.place(x=0, y=0, width=1000, height=700)

    n = StringVar()
    a = StringVar()
    e = StringVar()
    p = StringVar()

    account = Label(f2, text='Create your account here!', bg='#aaaaff')
    account.config(font=('eras medium itc', 25))
    account.place(x=300, y=100)
    name = Label(f2, text='Enter Name', bg='#aaaaff')
    name.config(font=('eras medium itc', 20))
    age = Label(f2, text='Enter Age', bg='#aaaaff')
    age.config(font=('eras medium itc', 20))
    age2 = Label(f2, text='(18 - 70)', bg='#aaaaff')
    age2.config(font=('eras medium itc', 15))
    email = Label(f2, text='Enter Email', bg='#aaaaff')
    email.config(font=('eras medium itc', 20))
    passw = Label(f2, text='Create Password', bg='#aaaaff')
    passw.config(font=('eras medium itc', 20))

    nametext = Entry(f2, font=('eras medium itc', 12), borderwidth=2, textvariable=n)
    agetext = Entry(f2, font=('eras medium itc', 12), borderwidth=2, textvariable=a)
    emailtext = Entry(f2, font=('eras medium itc', 12), borderwidth=2, textvariable=e)
    passwtext = Entry(f2, font=('eras medium itc', 12), borderwidth=2, textvariable=p, show='*')

    name.place(x=280, y=200)
    age.place(x=280, y=250)
    age2.place(x=715, y=252)
    email.place(x=280, y=300)
    passw.place(x=280, y=350)

    nametext.place(x=520, y=205)
    agetext.place(x=520, y=255)
    emailtext.place(x=520, y=305)
    passwtext.place(x=520, y=355)

    home_btn = Button(f2, text='Home', command=home, width=15, height=2)
    home_btn.place(x=50, y=50)

    def finish():

        if n.get() == '' or p.get() == '':
            messagebox.showerror('Error', 'Information cannot be empty')

        else:
            try:
                conn = sqlite3.connect('myfile.db')
                c = conn.cursor()
                c.execute("INSERT INTO Accounts (name, age, email, passw) VALUES ('" + n.get() + "','" + a.get() + "','" + e.get() + "','" + p.get() + "')")
                conn.commit()
                conn.close()
                messagebox.showinfo('Action Completed', 'User Registered Successfully')
                n.set('')
                a.set('')
                e.set('')
                p.set('')

            except:
                messagebox.showerror('Aborted', 'Invalid Information Provided')

    sogs_btn = Button(f2, text='Create Account', command=finish, height=2, width=15)
    sogs_btn.place(x=450, y=450)


def branch():
    f3 = Frame(bg='#aaaaff')
    f3.place(x=0, y=0, width=1000, height=700)

    lab = Label(f3, text='Select Police Station Branch!', bg='#aaaaff')
    lab.config(font=('eras medium itc', 25))
    lab.place(x=300, y=100)

    clicked = StringVar()
    clicked.set('Select Branch')
    branches = []
    conn = sqlite3.connect('myfile.db')
    c = conn.cursor()
    branch = c.execute("SELECT branch_name from Branch")
    for branche in branch:
        branches.append(branche)
    drop = OptionMenu(f3, clicked, *branches)
    drop.place(x=430, y=250, width=150, height=30)

    conn.commit()
    conn.close()

    btn = Button(f3, text='Confirm', command=menu, height=2, width=15)
    btn.place(x=450, y=300)

    home_btn = Button(f3, text='Home', command=home, width=15, height=2)
    home_btn.place(x=50, y=50)


def menu():
    n = ttk.Notebook()
    n.place(x=0, y=0, width=1000, height=700)

    def demo(a):
        if n.index("current") == 6:
            home()

    n.bind("<<NotebookTabChanged>>", demo)
    insert(n)
    show(n)
    search(n)
    update(n)
    delete(n)
    victim(n)
    out(n)


def insert(n):
    f4 = Frame(bg='#aaaaff')
    n.add(f4, text="Insert")

    s1 = StringVar()
    s2 = StringVar()
    s3 = StringVar()
    s4 = StringVar()
    s5 = StringVar()

    u0 = Label(f4, text='Enter Criminal Information', bg='#aaaaff')
    u0.config(font=('eras medium itc', 25))
    u0.place(x=300, y=100)

    u2 = Label(f4, font=('eras medium itc', 20), bg='#aaaaff', text="Enter Name")
    u2.place(x=300, y=200)
    e2 = Entry(f4, font=('eras medium itc', 12), textvariable=s1)
    e2.place(x=500, y=210)

    u3 = Label(f4, font=('eras medium itc', 20), bg='#aaaaff', text="Enter Age")
    u3.place(x=300, y=250)
    e3 = Entry(f4, font=('eras medium itc', 12), textvariable=s2)
    e3.place(x=500, y=260)

    u5 = Label(f4, font=('eras medium itc', 20), bg='#aaaaff', text="Enter Date")
    u5.place(x=300, y=300)
    e5 = DateEntry(f4, font=('eras medium itc', 12), textvariable=s4)
    e5.place(x=500, y=310)

    u4 = Label(f4, font=('eras medium itc', 20), bg='#aaaaff', text="Crime")
    u4.place(x=300, y=350)
    e4 = Entry(f4, font=('eras medium itc', 12), textvariable=s3)
    e4.place(x=500, y=360)

    u6 = Label(f4, font=('eras medium itc', 20), bg='#aaaaff', text="Victim Name")
    u6.place(x=300, y=400)
    e6 = Entry(f4, font=('eras medium itc', 12), textvariable=s5)
    e6.place(x=500, y=410)

    def insert1():
        db = sqlite3.connect('myfile.db')
        cr = db.cursor()
        cr.execute("INSERT INTO CriminalInfo (name, age, crime, date, victim) VALUES ('" + s1.get() + "','" + s2.get() + "','" + s3.get() + "','" + s4.get() + "','" + s5.get() + "')")
        db.commit()
        db.close()
        messagebox.showinfo("Action completed", "Insertion Executed")
        s1.set("")
        s2.set("")
        s3.set("")
        s4.set("")
        s5.set("")

        show1(f55)

    b1 = Button(f4, text="Insert", command=insert1, height=2, width=15)
    b1.place(x=450, y=500)


def show(n):
    f5 = Frame(bg='#aaaaff')
    n.add(f5, text="Show All")
    global f55
    f55 = f5
    show1(f5)

def show1(f5):
    for w in f5.winfo_children():
        w.destroy()

    u1 = Label(f5, text="ID", font=('eras medium itc', 12), bg="#000000", fg="white")
    u1.place(x=0, y=10, width=100)

    u2 = Label(f5, text="Name", font=('eras medium itc', 12), bg="#000000", fg="white")
    u2.place(x=100, y=10, width=220)

    u3 = Label(f5, text="Age", font=('eras medium itc', 12), bg="#000000", fg="white")
    u3.place(x=320, y=10, width=100)

    u4 = Label(f5, text="Crime", font=('eras medium itc', 12), bg="#000000", fg="white")
    u4.place(x=420, y=10, width=220)

    u5 = Label(f5, text="Date", font=('eras medium itc', 12), bg="#000000", fg="white")
    u5.place(x=640, y=10, width=150)

    u6 = Label(f5, text="Victim", font=('eras medium itc', 12), bg="#000000", fg="white")
    u6.place(x=790, y=10, width=210)


    db = sqlite3.connect('myfile.db')
    cr = db.cursor()
    r = cr.execute("SELECT * FROM CriminalInfo")
    x = 0
    y = 50
    for r1 in r:
        Label(f5, text=r1[0], font=('eras medium itc', 12), bg="#000000", fg="white").place(x=x, y=y, width=100)
        x = x + 100
        Label(f5, text=r1[1], font=('eras medium itc', 12), bg="#000000", fg="white").place(x=x, y=y, width=220)
        x = x + 220
        Label(f5, text=r1[2], font=('eras medium itc', 12), bg="#000000", fg="white").place(x=x, y=y, width=100)
        x = x + 100
        Label(f5, text=r1[3], font=('eras medium itc', 12), bg="#000000", fg="white").place(x=x, y=y, width=220)
        x = x + 220
        Label(f5, text=r1[4], font=('eras medium itc', 12), bg="#000000", fg="white").place(x=x, y=y, width=150)
        x = x + 150
        Label(f5, text=r1[5], font=('eras medium itc', 12), bg="#000000", fg="white").place(x=x, y=y, width=210)

        y = y + 30
        x = 0

    db.commit()
    db.close()

def search(n):
    f6 = Frame(bg='#aaaaff')
    n.add(f6, text="Search")
    s1 = StringVar()

    u0 = Label(f6, font=('eras medium itc', 20), bg='#aaaaff', text="Enter Criminal Name")
    u0.place(x=200, y=50)
    e0 = Entry(f6, font=('eras medium itc', 20), textvariable=s1)
    e0.place(x=500, y=50)

    def search1():

        u1 = Label(f6, text="ID", font=('eras medium itc', 12), bg="#000000", fg="white")
        u1.place(x=0, y=200, width=100)

        u2 = Label(f6, text="Name", font=('eras medium itc', 12), bg="#000000", fg="white")
        u2.place(x=100, y=200, width=220)

        u3 = Label(f6, text="Age", font=('eras medium itc', 12), bg="#000000", fg="white")
        u3.place(x=320, y=200, width=100)

        u4 = Label(f6, text="Crime", font=('eras medium itc', 12), bg="#000000", fg="white")
        u4.place(x=420, y=200, width=220)

        u5 = Label(f6, text="Date", font=('eras medium itc', 12), bg="#000000", fg="white")
        u5.place(x=640, y=200, width=150)

        u6 = Label(f6, text="Victim", font=('eras medium itc', 12), bg="#000000", fg="white")
        u6.place(x=790, y=200, width=210)

        db = sqlite3.connect('myfile.db')
        cr = db.cursor()
        r = cr.execute("SELECT * FROM CriminalInfo WHERE name='" + s1.get() + "'")
        x = 0
        y = 250
        for r1 in r:
            Label(f6, text=r1[0], font=('eras medium itc', 12), bg="#000000", fg="white").place(x=x, y=y, width=100)
            x = x + 100
            Label(f6, text=r1[1], font=('eras medium itc', 12), bg="#000000", fg="white").place(x=x, y=y, width=220)
            x = x + 220
            Label(f6, text=r1[2], font=('eras medium itc', 12), bg="#000000", fg="white").place(x=x, y=y, width=100)
            x = x + 100
            Label(f6, text=r1[3], font=('eras medium itc', 12), bg="#000000", fg="white").place(x=x, y=y, width=220)
            x = x + 220
            Label(f6, text=r1[4], font=('eras medium itc', 12), bg="#000000", fg="white").place(x=x, y=y, width=150)
            x = x + 150
            Label(f6, text=r1[5], font=('eras medium itc', 12), bg="#000000", fg="white").place(x=x, y=y, width=210)

            break

        else:
            messagebox.showerror('Action Failed', 'Invalid Name')

        db.commit()
        db.close()

    b1 = Button(f6, text='Search', command=search1, height=2, width=15)
    b1.place(x=400, y=100)

def update(n):
    f7 = Frame(bg='#aaaaff')
    n.add(f7, text="Update")

    s1 = StringVar()

    u0 = Label(f7, font=('eras medium itc', 20), bg='#aaaaff', text="Enter Criminal ID")
    u0.place(x=200, y=50)
    e0 = Entry(f7, font=('eras medium itc', 20), textvariable=s1)
    e0.place(x=500, y=50)

    def update1():

        db = sqlite3.connect('myfile.db')
        cr = db.cursor()
        r = cr.execute("SELECT * FROM CriminalInfo WHERE criminalID='" + s1.get() + "'")

        for r1 in r:

            s2 = StringVar()
            s3 = StringVar()
            s4 = StringVar()
            s5 = StringVar()
            s6 = StringVar()

            u2 = Label(f7, font=('eras medium itc', 20), bg='#aaaaff', text="Enter Name")
            u2.place(x=300, y=250)
            e2 = Entry(f7, font=('eras medium itc', 12), textvariable=s2)
            e2.place(x=500, y=260)
            e2.insert(0, r1[1])

            u3 = Label(f7, font=('eras medium itc', 20), bg='#aaaaff', text="Enter Age")
            u3.place(x=300, y=300)
            e3 = Entry(f7, font=('eras medium itc', 12), textvariable=s3)
            e3.place(x=500, y=310)
            e3.insert(0, r1[2])

            u5 = Label(f7, font=('eras medium itc', 20), bg='#aaaaff', text="Enter Date")
            u5.place(x=300, y=350)
            e5 = DateEntry(f7, font=('eras medium itc', 12), textvariable=s5)
            e5.place(x=500, y=360)

            u4 = Label(f7, font=('eras medium itc', 20), bg='#aaaaff', text="Crime")
            u4.place(x=300, y=400)
            e4 = Entry(f7, font=('eras medium itc', 12), textvariable=s4)
            e4.place(x=500, y=410)
            e4.insert(0, r1[3])

            u6 = Label(f7, font=('eras medium itc', 20), bg='#aaaaff', text="Victim Name")
            u6.place(x=300, y=450)
            e6 = Entry(f7, font=('eras medium itc', 12), textvariable=s6)
            e6.place(x=500, y=460)
            e6.insert(0, r1[5])

            def update2():
                db = sqlite3.connect('myfile.db')
                cr = db.cursor()
                cr.execute("UPDATE CriminalInfo SET name ='" + s2.get() + "', age ='" + s3.get() + "', crime ='" + s4.get() + "', date ='" + s5.get() + "', victim ='" + s6.get() + "' where CriminalID ='" + s1.get() + "'")
                db.commit()
                db.close()
                show1(f55)
                messagebox.showinfo('Action Completed', 'Criminal Information Updated')

            b11 = Button(f7, text="Update", command=update2, height=2, width=15)
            b11.place(x=450, y=550)

            break

        else:
            messagebox.showerror('Action Failed', 'Invalid Criminal ID')

        db.commit()
        db.close()

    b1 = Button(f7, text='Fetch', command=update1, height=2, width=15)
    b1.place(x=400, y=100)


def delete(n):
    f8 = Frame(bg='#aaaaff')
    n.add(f8, text="Delete")
    s1 = StringVar()

    u0 = Label(f8, font=('eras medium itc', 20), bg='#aaaaff', text="Enter Criminal ID")
    u0.place(x=200, y=50)
    e0 = Entry(f8, font=('eras medium itc', 20), textvariable=s1)
    e0.place(x=500, y=50)

    def delete1():

        u1 = Label(f8, text="ID", font=('eras medium itc', 12), bg="#000000", fg="white")
        u1.place(x=0, y=200, width=100)

        u2 = Label(f8, text="Name", font=('eras medium itc', 12), bg="#000000", fg="white")
        u2.place(x=100, y=200, width=220)

        u3 = Label(f8, text="Age", font=('eras medium itc', 12), bg="#000000", fg="white")
        u3.place(x=320, y=200, width=100)

        u4 = Label(f8, text="Crime", font=('eras medium itc', 12), bg="#000000", fg="white")
        u4.place(x=420, y=200, width=220)

        u5 = Label(f8, text="Date", font=('eras medium itc', 12), bg="#000000", fg="white")
        u5.place(x=640, y=200, width=150)

        u6 = Label(f8, text="Victim", font=('eras medium itc', 12), bg="#000000", fg="white")
        u6.place(x=790, y=200, width=210)

        db = sqlite3.connect('myfile.db')
        cr = db.cursor()
        r = cr.execute("SELECT * FROM CriminalInfo WHERE criminalID='" + s1.get() + "'")
        x = 0
        y = 250
        for r1 in r:
            Label(f8, text=r1[0], font=('eras medium itc', 12), bg="#000000", fg="white").place(x=x, y=y, width=100)
            x = x + 100
            Label(f8, text=r1[1], font=('eras medium itc', 12), bg="#000000", fg="white").place(x=x, y=y, width=220)
            x = x + 220
            Label(f8, text=r1[2], font=('eras medium itc', 12), bg="#000000", fg="white").place(x=x, y=y, width=100)
            x = x + 100
            Label(f8, text=r1[3], font=('eras medium itc', 12), bg="#000000", fg="white").place(x=x, y=y, width=220)
            x = x + 220
            Label(f8, text=r1[4], font=('eras medium itc', 12), bg="#000000", fg="white").place(x=x, y=y, width=150)
            x = x + 150
            Label(f8, text=r1[5], font=('eras medium itc', 12), bg="#000000", fg="white").place(x=x, y=y, width=210)

            break

        else:
            messagebox.showerror('Action Failed', 'Invalid Criminal ID')

        db.commit()
        db.close()

        def delete2():
            db = sqlite3.connect('myfile.db')
            cr = db.cursor()
            cr.execute(" DELETE FROM CriminalInfo WHERE criminalID='" + s1.get() + "'")
            db.commit()
            db.close()
            show1(f55)
            messagebox.showinfo('Action Completed', 'Data Deleted')
            s1.set("")

        btn = Button(f8, text='Confirm', command=delete2, height=2, width=15)
        btn.place(x=400, y=500)

    b1 = Button(f8, text='Fetch', command=delete1, height=2, width=15)
    b1.place(x=400, y=100)

def victim(n):
    f9 = Frame(bg='#aaaaff')
    n.add(f9, text="Victims")

    u0 = Label(f9, text="List of all Victims", font=('eras medium itc', 20), bg='#aaaaff')
    u0.place(x=400, y=30)

    u1 = Label(f9, text="ID", font=('eras medium itc', 12), bg="#000000", fg="white")
    u1.place(x=0, y=100, width=100)

    u2 = Label(f9, text="Name", font=('eras medium itc', 12), bg="#000000", fg="white")
    u2.place(x=100, y=100, width=300)

    u3 = Label(f9, text="Age", font=('eras medium itc', 12), bg="#000000", fg="white")
    u3.place(x=400, y=100, width=200)

    u4 = Label(f9, text="Address", font=('eras medium itc', 12), bg="#000000", fg="white")
    u4.place(x=600, y=100, width=400)

    db = sqlite3.connect('myfile.db')
    cr = db.cursor()
    r = cr.execute("SELECT * FROM victims")
    x = 0
    y = 150

    for r1 in r:
        Label(f9, text=r1[0], font=('eras medium itc', 12), bg="#000000", fg="white").place(x=x, y=y, width=100)
        x = x + 100
        Label(f9, text=r1[1], font=('eras medium itc', 12), bg="#000000", fg="white").place(x=x, y=y, width=300)
        x = x + 300
        Label(f9, text=r1[2], font=('eras medium itc', 12), bg="#000000", fg="white").place(x=x, y=y, width=200)

        y = y + 30
        x = 0

    r2 = cr.execute("SELECT victim_address from Address")
    x = 600
    y = 150

    for r3 in r2:
        Label(f9, text=r3[0], font=('eras medium itc', 12), bg="#000000", fg="white").place(x=x, y=y, width=400)
        y = y + 30

    db.commit()
    db.close()

def out(n):
    f10 = Frame(bg='#aaaaff')
    n.add(f10, text="Log Out")

def home():

    f1 = Frame(bg='#aaaaff')
    f1.place(x=0, y=0, width=1000, height=700)

    g1 = StringVar()
    g2 = StringVar()

    mainable = Label(f1, text='Criminal Database Management', bg='#aaaaff')
    mainable.config(font=('eras medium itc', 27))
    mainable.place(x=250, y=85)

    mainLabel = Label(f1, text='Enter Your Login Credentials!', bg='#aaaaff')
    mainLabel.config(font=('eras medium itc', 25))
    mainLabel.place(x=300, y=200)

    policeID = Label(f1, text='Name', bg='#aaaaff')
    policeID.config(font=('eras medium itc', 20))
    policeID.place(x=350, y=330)
    password = Label(f1, text='Password', bg='#aaaaff')
    password.config(font=('eras medium itc', 20))
    password.place(x=350, y=380)

    textID = Entry(f1, font=('eras medium itc', 12), borderwidth=2, textvariable=g1)
    textID.place(x=500, y=335)
    textword = Entry(f1, font=('eras medium itc', 12), borderwidth=2, show='*', textvariable=g2)
    textword.place(x=500, y=385)

    def logs():
        conn = sqlite3.connect('myfile.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Accounts WHERE name='" + g1.get() + "' and passw='" + g2.get() + "'")
        for c1 in c:
            branch()
            break

        else:
            messagebox.showerror('Invalid', 'Incorrect Login Info')

        conn.commit()
        conn.close()
        g1.set('')
        g2.set('')


    login = Button(f1, text='Login!', command=logs, height=2, width=15)
    signup = Button(f1, text='Sign up!', command=sogs, height=2, width=15)

    login.place(x=400, y=500)
    signup.place(x=530, y=500)


home()
dis.mainloop()