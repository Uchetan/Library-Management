import datetime
from tkinter import *
import sqlite3
from tkinter import PhotoImage
from tkinter import messagebox
con=sqlite3.connect('library.db')
st_his={}         #for student's history
query ="select * from history"
cur=con.cursor()
a=cur.execute(query)
for i in a:
    st_his[i[0]]=[i[1],i[2],i[3],i[4],i[5]]

stud_roll={}        #for all student's
query ="select * from all_students"
cur=con.cursor()
a=cur.execute(query)
for i in a:
    stud_roll[i[0]]=[i[1],i[2],i[3],i[4]]

stud_book={}        #for all books
query ="select * from all_books"
cur=con.cursor()
a=cur.execute(query)
for i in a:
    stud_book[i[0]]=[i[1],i[2]]

issue_book={}        #for issued of books
query ="select * from issued_book"
cur=con.cursor()
a=cur.execute(query)
for i in a:
    issue_book[i[0]]=[i[1],i[2],i[3],i[4],i[5]]


def sleep():
    a = Label(panel_1, bd=2, height=560, width=990, bg="#4d4545")
    panel_1.add(a)
    a.place(x=0, y=0)


base=Tk()
base.geometry("1400x680+0+0")
base.title("Library Management")
base.iconbitmap(r"./Images/main.ico")
#images
tit=PhotoImage(file="./Images/title.png")
exit=PhotoImage(file="./Images/exit.png")
#upper style
pane=PanedWindow(orient=VERTICAL,width=850,height=600)
pane.pack(fill=BOTH,expand=1)
t=Label(pane,height=5,bg="#2ef77f")
pane.add(t)
f1=("Bauhaus 93",24)
f2=("Britannic Bold",12)

b=Label(pane,bg="#2ef77f",image=tit)
b.place(x=80,y=5)
b=Label(pane,text="Library Management",bg="#2ef77f",font=f1,fg="white")
b.place(x=200,y=30)
b=Label(pane,image=exit,bg="#2ef77f")
b.place(x=1220,y=30)
def meth(a):
    b=messagebox.askquestion("Sure","Do You Want To Exit")
    if b=="yes":
        base.destroy()
def meth1(a):
    b.configure( fg="black")
def meth2(a):
    b.configure( fg="red")
b=Label(pane,text="Log Out",bg="#2ef77f",font=("Britannic Bold",15),fg="red")
b.place(x=1250,y=30)
b.bind("<ButtonRelease>",meth)
b.bind("<Enter>",meth1)
b.bind("<Leave>",meth2)

def all_issue_books():
    sleep()
    ti = Label(panel_1, text="All Issued Books", font=f2,fg="white", bg="#4d4545")
    panel_1.add(ti)
    ti.place(x=450, y=25)
    d = ""
    for i in issue_book:
        d = d + f"\n\n{i}  |  {issue_book[i][0]}  |  {issue_book[i][1]}  |  {issue_book[i][2]}  |  {issue_book[i][3]}  |  {issue_book[i][4]}"

    c = Label(panel_1, text=f"{d}", font=f2, bg="#4d4545",fg="white")
    panel_1.add(c)
    c.place(x=150, y=50)


def all_info():
    sleep()
    ti = Label(panel_1, text="All Students Info", font=f2, bg="#4d4545",fg="white")
    panel_1.add(ti)
    ti.place(x=450, y=25)
    d=""
    for i in stud_roll:
        d=d+f"\n\n{i}  |  {stud_roll[i][0]}  |  {stud_roll[i][1]}  |  {stud_roll[i][2]}  |  {stud_roll[i][3]}"

    c = Label(panel_1, text=f"{d}",font=f2, bg="#4d4545",fg="white")
    panel_1.add(c)
    c.place(x=150, y=50)

def all_book():
    sleep()
    ti = Label(panel_1, text="All Books Info", font=f2, bg="#4d4545",fg="white")
    panel_1.add(ti)
    ti.place(x=450, y=25)
    d=""
    for i in stud_book:
        d=d+f"\n\n{i}  |  {stud_book[i][0]}  |  {stud_book[i][1]}"

    c = Label(panel_1, text=f"{d}",font=f2, bg="#4d4545",fg="white")
    panel_1.add(c)
    c.place(x=150, y=50)


def Issue():
    sleep()

    def issue_books():
        sleep()

        a=rol.get()
        b = bno.get()
        if a not in stud_roll:
            messagebox.showerror("Invalid", "Invalid Input!!!!")
            Issue()
        elif(b not in stud_book):
            messagebox.showerror("Invalid", "Invalid Input!!!!")
            Issue()
        else:
            c = datetime.date.today()
            bb = datetime.timedelta(days=7)
            dd = c + bb
            ret_date = str(dd)
            issue_book[a] = [stud_roll[a][0], stud_book[b][0], b, c, ret_date]

            a1 = Label(panel_1, text="Student Enrollment number : ", font=f2, bg="#4d4545",fg="white")
            panel_1.add(a1)
            a1.place(x=250, y=100)
            b1 = Label(panel_1,text=f"{a}", width=25, height=1, font=f2, bg="#4d4545",fg="white")
            panel_1.add(b1)
            b1.place(x=500, y=100)

            a1 = Label(panel_1, text="Student Name : ", font=f2, bg="#4d4545",fg="white")
            panel_1.add(a1)
            a1.place(x=250, y=150)
            b1 = Label(panel_1, text=f"{stud_roll[a][1]}", width=25, height=1, font=f2, bg="#4d4545",fg="white")
            panel_1.add(b1)
            b1.place(x=500, y=150)

            a1 = Label(panel_1, text="Book Name : ", font=f2, bg="#4d4545",fg="white")
            panel_1.add(a1)
            a1.place(x=250, y=200)
            b1 = Label(panel_1,text=f"{stud_book[b][0]}", width=25, height=1, font=f2, bg="#4d4545",fg="white")
            panel_1.add(b1)
            b1.place(x=500, y=200)

            a1 = Label(panel_1, text="Book No : ", font=f2, bg="#4d4545",fg="white")
            panel_1.add(a1)
            a1.place(x=250, y=250)
            b1 = Label(panel_1, text=f"{b}", width=25, height=1, font=f2, bg="#4d4545",fg="white")
            panel_1.add(b1)
            b1.place(x=500, y=250)

            a1 = Label(panel_1, text="Issue Date : ", font=f2, bg="#4d4545",fg="white")
            panel_1.add(a1)
            a1.place(x=250, y=300)
            b1 = Label(panel_1, text=f"{c}", width=25, height=1, font=f2, bg="#4d4545",fg="white")
            panel_1.add(b1)
            b1.place(x=500, y=300)

            a1 = Label(panel_1, text="Return Date : ", font=f2, bg="#4d4545",fg="white")
            panel_1.add(a1)
            a1.place(x=250, y=330)
            b1 = Label(panel_1, text=f"{ret_date}", width=25, height=1, font=f2, bg="#4d4545",fg="white")
            panel_1.add(b1)
            b1.place(x=500, y=330)

            query = f"insert into issued_book values('{a}','{stud_roll[a][0]}','{stud_book[b][0]}','{b}','{c}','{ret_date}')"
            con.execute(query)
            con.commit()
            messagebox.showinfo("Sucess","Book Issued Sucessfully!!")

    ti = Label(panel_1, text="Issue Books",font=f2, bg="#4d4545",fg="white")
    panel_1.add(ti)
    ti.place(x=450, y=25)
    a = Label(panel_1, text="Student Enrollment number : ",font=f2, bg="#4d4545",fg="white")
    panel_1.add(a)
    a.place(x=250, y=100)
    rol = Entry(panel_1, width=25,font=f2)
    panel_1.add(rol)
    rol.place(x=500, y=100)
    c = Label(panel_1, text="Book number : ",font=f2, bg="#4d4545",fg="white")
    panel_1.add(c)
    c.place(x=300, y=150)
    bno = Entry(panel_1, width=25,font=f2)
    panel_1.add(bno)
    bno.place(x=500, y=150)
    bt = Button(panel_1, text="Submit",font=f2,command=issue_books,fg="white",bg="#79827c")
    panel_1.add(bt)
    bt.place(x=450, y=200)
    d = Label(panel_1, text="Today's date is : ",width=25, height=1,font=f2, bg="#4d4545",fg="white")
    panel_1.add(d)
    d.place(x=150, y=350)
    e=datetime.date.today()
    d = Label(panel_1, text=f"{e}",width=25, height=1,font=f2, bg="#4d4545",fg="white")
    panel_1.add(d)
    d.place(x=450, y=350)
    d = Label(panel_1, text="Book should be returned in 7 Days", height=1,font=f2, bg="#4d4545",fg="white")
    panel_1.add(d)
    d.place(x=310, y=280)

def Return_book():
    sleep()

    def return_books():
        sleep()
        a = sro.get()
        b = sbr.get()
        c = sdt.get()
        if a not in issue_book:
            messagebox.showerror("Invalid", "Invalid Input!!!!")
            Return_book()
        elif(b not in issue_book[a]):
            messagebox.showerror("Invalid", "No such Book Issued")
            Return_book()
        else:
            d = c.split("-")
            q = d[1]
            if q[0] == "0":
                m = q[1:]
                q = m
            p = d[0]
            if p[0] == "0":
                m = p[1:]
                p = m
            r = d[2] # current p=date  q=month
            c = datetime.date(int(r), int(q), int(p))
            d = issue_book[a][-1]
            e = d.split("-")
            y = e[1]
            if y[0] == "0":
                m = y[1:]
                y = m
            x = e[2]
            if x[0] == "0":
                m = x[1:]
                x = m
            z = e[0]  # actual x=date  y=month
            d = datetime.date(int(z), int(y), int(x))
            w = c-d
            w = str(w)
            w=w.split(" ")
            w = w[0]
            w = int(w)
            cc=True
            if (w > 0):
                a2 = Label(panel_1, text=f"Date of returning was : {issue_book[a][-1]}", font=f2, bg="#4d4545",fg="white")
                panel_1.add(a2)
                a2.place(x=250, y=100)
                fine = w * 5
                a1 = Label(panel_1, text=f"Fine amount : {fine}", font=f2, bg="#4d4545",fg="white")
                panel_1.add(a1)
                a1.place(x=250, y=150)
                a1 = Label(panel_1, text=f"For : {w} Days", font=f2, bg="#4d4545",fg="white")
                panel_1.add(a1)
                a1.place(x=250, y=200)
                cc=False
            if cc ==True:
                fine=0
            query = f"insert into history values('{a}','{issue_book[a][0]}','{issue_book[a][1]}','{issue_book[a][2]}','{issue_book[a][3]}','{issue_book[a][4]}','{fine}')"
            con.execute(query)
            con.commit()

            query = f"delete from issued_book where roll_no='{a}'"
            con.execute(query)
            con.commit()
            issue_book.pop(a)
            ti = Label(panel_1, text="Return Books", font=f2, bg="#4d4545",fg="white")
            panel_1.add(ti)
            ti.place(x=450, y=25)
            messagebox.showinfo("Sucess", "Book Returned Sucessfully!!")

    ti = Label(panel_1, text="Return Books",font=f2, bg="#4d4545",fg="white")
    panel_1.add(ti)
    ti.place(x=450, y=25)
    a = Label(panel_1, text="Student Enrollment number : ",font=f2, bg="#4d4545",fg="white")
    panel_1.add(a)
    a.place(x=250, y=100)
    sro = Entry(panel_1, width=25,font=f2)
    panel_1.add(sro)
    sro.place(x=500, y=100)
    c = Label(panel_1, text="Book number : ",font=f2, bg="#4d4545",fg="white")
    panel_1.add(c)
    c.place(x=300, y=150)
    sbr = Entry(panel_1, width=25,font=f2)
    panel_1.add(sbr)
    sbr.place(x=500, y=150)
    e = Label(panel_1, text="Enter Date : ",font=f2, bg="#4d4545",fg="white")
    panel_1.add(e)
    e.place(x=300, y=200)
    sdt = Entry(panel_1, width=25,font=f2)
    panel_1.add(sdt)
    sdt.place(x=500, y=200)
    bt = Button(panel_1, text="Submit",font=f2,command=return_books,fg="white",bg="#79827c")
    panel_1.add(bt)
    bt.place(x=450, y=250)
    d = Label(panel_1, text="Today's date is : ",width=25, height=1,font=f2, bg="#4d4545",fg="white")
    panel_1.add(d)
    d.place(x=150, y=350)
    e=datetime.date.today()
    d = Label(panel_1, text=f"{e}",width=25, height=1,font=f2, bg="#4d4545",fg="white")
    panel_1.add(d)
    d.place(x=450, y=350)


def Add_stud():
    sleep()

    def add_student():
        sleep()
        a=sno.get()
        b=sna.get()
        c=sbr.get()
        d=smo.get()
        e=sem.get()
        stud_roll[a] = [b, c, d, e]

        query = f"insert into all_students values('{a}','{b}','{c}','{d}','{e}')"
        con.execute(query)
        con.commit()
        ti = Label(panel_1, text="Add Student", font=f2, bg="#4d4545",fg="white")
        panel_1.add(ti)
        ti.place(x=450, y=25)
        ti = Label(panel_1, text="Data added Sucessfully", font=f2, bg="#4d4545",fg="white")
        panel_1.add(ti)
        ti.place(x=450, y=75)
        messagebox.showinfo("Sucess", "Student Added Sucessfully!!")

    ti = Label(panel_1, text="Add Student",font=f2, bg="#4d4545",fg="white")
    panel_1.add(ti)
    ti.place(x=450, y=25)

    a = Label(panel_1, text="Enter Enrollment number : ",font=f2, bg="#4d4545",fg="white")
    panel_1.add(a)
    a.place(x=250, y=70)
    sno = Entry(panel_1, width=25,font=f2)
    panel_1.add(sno)
    sno.place(x=500, y=70)
    c = Label(panel_1, text="Enter Your Name : ",font=f2, bg="#4d4545",fg="white")
    panel_1.add(c)
    c.place(x=300, y=115)
    sna = Entry(panel_1, width=25,font=f2)
    panel_1.add(sna)
    sna.place(x=500, y=115)
    e = Label(panel_1, text="Enter Your Branch : ",font=f2, bg="#4d4545",fg="white")
    panel_1.add(e)
    e.place(x=300, y=160)
    sbr = Entry(panel_1, width=25,font=f2)
    panel_1.add(sbr)
    sbr.place(x=500, y=160)
    g = Label(panel_1, text="Enter Your mobile number : ",font=f2, bg="#4d4545",fg="white")
    panel_1.add(g)
    g.place(x=250, y=205)
    smo = Entry(panel_1, width=25,font=f2)
    panel_1.add(smo)
    smo.place(x=500, y=205)
    i = Label(panel_1, text="Enter email : ",font=f2, bg="#4d4545",fg="white")
    panel_1.add(i)
    i.place(x=300, y=250)
    sem = Entry(panel_1, width=35,font=f2)
    panel_1.add(sem)
    sem.place(x=500, y=250)
    bt = Button(panel_1, text="Submit",font=f2,command=add_student,fg="white",bg="#79827c")
    panel_1.add(bt)
    bt.place(x=450, y=300)

def Add_book():
    sleep()

    def add_books():
        sleep()
        a=bno.get()
        b=bna.get()
        c=bau.get()
        stud_book[a] = [b, c]

        query = f"insert into all_books values('{a}','{b}','{c}')"
        con.execute(query)
        con.commit()
        ti = Label(panel_1, text="Add Book", font=f2, bg="#4d4545",fg="white")
        panel_1.add(ti)
        ti.place(x=450, y=25)
        ti = Label(panel_1, text="Data added Sucessfully", font=f2, bg="#4d4545",fg="white")
        panel_1.add(ti)
        ti.place(x=450, y=75)
        messagebox.showinfo("Sucess", "Book Added Sucessfully!!")

    ti = Label(panel_1, text="Add Book",font=f2, bg="#4d4545",fg="white")
    panel_1.add(ti)
    ti.place(x=450, y=25)
    a = Label(panel_1, text="Enter Book Number : ",font=f2, bg="#4d4545",fg="white")
    panel_1.add(a)
    a.place(x=300, y=70)
    bno = Entry(panel_1, width=25,font=f2)
    panel_1.add(bno)
    bno.place(x=500, y=70)
    c = Label(panel_1, text="Enter Book Name : ",font=f2, bg="#4d4545",fg="white")
    panel_1.add(c)
    c.place(x=300, y=115)
    bna = Entry(panel_1, width=25,font=f2)
    panel_1.add(bna)
    bna.place(x=500, y=115)
    e = Label(panel_1, text="Enter Book Author : ",font=f2, bg="#4d4545",fg="white")
    panel_1.add(e)
    e.place(x=300, y=160)
    bau = Entry(panel_1, width=25,font=f2)
    panel_1.add(bau)
    bau.place(x=500, y=160)
    bt = Button(panel_1, text="Submit",font=f2,command=add_books,fg="white",bg="#79827c")
    panel_1.add(bt)
    bt.place(x=450, y=205)

def search_stud():
    sleep()
    def search_student():
        sleep()
        a = rno.get()
        if a not in stud_roll:
            messagebox.showerror("Invalid", "Roll no not Present!!!!")
            search_stud()
        else:
            ti = Label(panel_1, text="Student roll no :", font=f2, bg="#4d4545",fg="white")
            panel_1.add(ti)
            ti.place(x=250, y=70)
            a1 = Label(panel_1, text=f"{a}", font=f2, bg="#4d4545",fg="white")
            panel_1.add(a1)
            a1.place(x=500, y=70)
            ti = Label(panel_1, text="Student Name :", font=f2, bg="#4d4545",fg="white")
            panel_1.add(ti)
            ti.place(x=250, y=120)
            a1 = Label(panel_1, text=f"{stud_roll[a][0]}", font=f2, bg="#4d4545",fg="white")
            panel_1.add(a1)
            a1.place(x=500, y=120)
            ti = Label(panel_1, text="Branch:", font=f2, bg="#4d4545",fg="white")
            panel_1.add(ti)
            ti.place(x=250, y=170)
            a1 = Label(panel_1, text=f"{stud_roll[a][1]}", font=f2, bg="#4d4545",fg="white")
            panel_1.add(a1)
            a1.place(x=500, y=170)
            ti = Label(panel_1, text="Student Mobile:", font=f2, bg="#4d4545",fg="white")
            panel_1.add(ti)
            ti.place(x=250, y=220)
            a1 = Label(panel_1, text=f"{stud_roll[a][2]}", font=f2, bg="#4d4545",fg="white")
            panel_1.add(a1)
            a1.place(x=500, y=220)
            ti = Label(panel_1, text="Student Email:", font=f2, bg="#4d4545",fg="white")
            panel_1.add(ti)
            ti.place(x=250, y=270)
            a1 = Label(panel_1, text=f"{stud_roll[a][3]}", font=f2, bg="#4d4545",fg="white")
            panel_1.add(a1)
            a1.place(x=500, y=270)

            if a in issue_book:
                ti = Label(panel_1, text="Issued book :", font=f2, bg="#4d4545",fg="white")
                panel_1.add(ti)
                ti.place(x=150, y=320)
                a1 = Label(panel_1, text=f"{issue_book[a][1]}", font=f2, bg="#4d4545",fg="white")
                panel_1.add(a1)
                a1.place(x=200, y=370)
                a1 = Label(panel_1, text=f"On :{issue_book[a][3]}", font=f2, bg="#4d4545",fg="white")
                panel_1.add(a1)
                a1.place(x=350, y=370)

    ti = Label(panel_1, text="Search Student", font=f2, bg="#4d4545",fg="white")
    panel_1.add(ti)
    ti.place(x=450, y=25)
    a = Label(panel_1, text="Enter Enrollment no : ", font=f2, bg="#4d4545",fg="white")
    panel_1.add(a)
    a.place(x=250, y=70)
    rno = Entry(panel_1, width=25, font=f2)
    panel_1.add(rno)
    rno.place(x=500, y=70)
    bt = Button(panel_1, text="Submit",font=f2,command=search_student,fg="white",bg="#79827c")
    panel_1.add(bt)
    bt.place(x=450, y=116)

def search_book():
    sleep()
    def search_books():
        sleep()
        a = bno.get()
        if a not in stud_book:
            messagebox.showerror("Invalid", "Invalid Book no!!!!")
            search_book()
        else:
            a1 = Label(panel_1, text="Book Name : ", font=f2, bg="#4d4545",fg="white")
            panel_1.add(a1)
            a1.place(x=250, y=70)
            b = Label(panel_1, text=f"{stud_book[a][0]}",font=f2, bg="#4d4545",fg="white")
            panel_1.add(b)
            b.place(x=500, y=70)

            a1 = Label(panel_1, text="Book No : ", font=f2, bg="#4d4545",fg="white")
            panel_1.add(a1)
            a1.place(x=250, y=120)
            b = Label(panel_1, text=f"{a}",font=f2, bg="#4d4545",fg="white")
            panel_1.add(b)
            b.place(x=500, y=120)

            a1 = Label(panel_1, text="Book Author : ", font=f2, bg="#4d4545",fg="white")
            panel_1.add(a1)
            a1.place(x=250, y=170)
            b = Label(panel_1, text=f"{stud_book[a][1]}",font=f2, bg="#4d4545",fg="white")
            panel_1.add(b)
            b.place(x=500, y=170)

            c = True
            for i in issue_book:
                if issue_book[i][2] == a:
                    a1=Label(panel_1,text="Issued by - ",font=f2, bg="#4d4545",fg="white")
                    panel_1.add(a1)
                    a1.place(x=150, y=220)
                    b = Label(panel_1, text=f"{issue_book[i][0]}", font=f2, bg="#4d4545",fg="white")
                    panel_1.add(b)
                    b.place(x=200, y=270)
                    b = Label(panel_1, text=f"On :{issue_book[i][3]}", font=f2, bg="#4d4545",fg="white")
                    panel_1.add(b)
                    b.place(x=150, y=320)
                    c=False
            if c == True:
                b = Label(panel_1, text="Book is available", font=f2, bg="#4d4545",fg="white")
                panel_1.add(b)
                b.place(x=200, y=300)
    ti = Label(panel_1, text="Search Book", font=f2, bg="#4d4545",fg="white")
    panel_1.add(ti)
    ti.place(x=450, y=25)
    a = Label(panel_1, text="Enter Book no : ", font=f2, bg="#4d4545",fg="white")
    panel_1.add(a)
    a.place(x=250, y=70)
    bno = Entry(panel_1, width=25,font=f2)
    panel_1.add(bno)
    bno.place(x=500, y=70)
    bt = Button(panel_1, text="Submit",font=f2,command=search_books,fg="white",bg="#79827c")
    panel_1.add(bt)
    bt.place(x=450, y=116)
def remove_student():
    sleep()
    def remove():
        sleep()
        a=sro.get()
        if a not in stud_roll:
            messagebox.showerror("Invalid", "Invalid Roll no!!!!")
            remove_student()
        else:
            if a in issue_book:
                sleep()
                a1 = Label(panel_1, text=f"Book Pending: {issue_book[a][1]}", font=f2, bg="#4d4545",fg="white")
                panel_1.add(a1)
                a1.place(x=250, y=70)
                a1 = Label(panel_1, text=f"On: {issue_book[a][3]}", font=f2, bg="#4d4545",fg="white")
                panel_1.add(a1)
                a1.place(x=250, y=120)
            else:
                stud_roll.pop(a)
                query = f"delete from all_students where roll_no='{a}'"
                con.execute(query)
                con.commit()
                ti = Label(panel_1, text="Remove Student", font=f2, bg="#4d4545",fg="white")
                panel_1.add(ti)
                ti.place(x=450, y=25)
                a1 = Label(panel_1, text="Data Removed Sucessfully !!!!", font=f2, bg="#4d4545",fg="white")
                panel_1.add(a1)
                a1.place(x=250, y=70)

    ti = Label(panel_1, text="Remove Student", font=f2, bg="#4d4545",fg="white")
    panel_1.add(ti)
    ti.place(x=450, y=25)
    a = Label(panel_1, text="Enter Enrollment no : ", font=f2, bg="#4d4545",fg="white")
    panel_1.add(a)
    a.place(x=250, y=70)
    sro = Entry(panel_1, width=25, font=f2)
    panel_1.add(sro)
    sro.place(x=500, y=70)
    bt = Button(panel_1, text="Submit",font=f2,command=remove,fg="white",bg="#79827c")
    panel_1.add(bt)
    bt.place(x=450, y=116)

def remove_book():
    sleep()
    def remove():
        sleep()
        a=sro.get()
        if a not in stud_book:
            messagebox.showerror("Invalid", "Invalid Book no!!!!")
            remove_book()
        else:
                stud_book.pop(a)
                query = f"delete from all_books where book_no='{a}'"
                con.execute(query)
                con.commit()
                ti = Label(panel_1, text="Remove Book", font=f2, bg="#4d4545",fg="white")
                panel_1.add(ti)
                ti.place(x=450, y=25)
                a1 = Label(panel_1, text="Data Removed Sucessfully !!!!", font=f2, bg="#4d4545",fg="white")
                panel_1.add(a1)
                a1.place(x=250, y=70)

    ti = Label(panel_1, text="Remove Book", font=f2, bg="#4d4545",fg="white")
    panel_1.add(ti)
    ti.place(x=450, y=25)
    a = Label(panel_1, text="Enter Book no : ", font=f2, bg="#4d4545",fg="white")
    panel_1.add(a)
    a.place(x=250, y=70)
    sro = Entry(panel_1, width=25, font=f2)
    panel_1.add(sro)
    sro.place(x=500, y=70)
    bt = Button(panel_1, text="Submit",font=f2,command=remove,fg="white",bg="#79827c")
    panel_1.add(bt)
    bt.place(x=450, y=116)


panel=PanedWindow(pane, bd=2,height=570,width=1345,bg="#4d4545")
pane.add(panel)
panel.place(x=5,y=90)
def hov(a):
    tp1.configure(fg="black",bg="white")
def lea(a):
    tp1.configure(fg="White",bg="#4d4545")
tp1=Button(panel,text="Issue Book",height=1,width=35,command=Issue,font=f2,fg="White",bg="#4d4545",bd=3)
panel.add(tp1)
tp1.place(x=15,y=50)
tp1.bind("<Enter>",hov)
tp1.bind("<Leave>",lea)
def hov(a):
    tp2.configure(fg="black",bg="white")
def lea(a):
    tp2.configure(fg="White",bg="#4d4545")
tp2=Button(panel,text="Return Book",height=1,width=35,command=Return_book,font=f2,fg="White",bg="#4d4545",bd=3)
panel.add(tp2)
tp2.place(x=15,y=90)
tp2.bind("<Enter>",hov)
tp2.bind("<Leave>",lea)
def hov(a):
    tp3.configure(fg="black", bg="white")
def lea(a):
    tp3.configure(fg="White", bg="#4d4545")
tp3=Button(panel,text="Add Student",height=1,width=35,command=Add_stud,font=f2,fg="White",bg="#4d4545",bd=3)
panel.add(tp3)
tp3.place(x=15,y=130)
tp3.bind("<Enter>",hov)
tp3.bind("<Leave>",lea)
def hov(a):
    tp4.configure(fg="black",bg="white")
def lea(a):
    tp4.configure(fg="White",bg="#4d4545")
tp4=Button(panel,text="Add Book",height=1,width=35,command=Add_book,font=f2,fg="White",bg="#4d4545",bd=3)
panel.add(tp4)
tp4.place(x=15,y=170)
tp4.bind("<Enter>",hov)
tp4.bind("<Leave>",lea)
def hov(a):
    tp5.configure(fg="black",bg="white")
def lea(a):
    tp5.configure(fg="White",bg="#4d4545")
tp5=Button(panel,text="Search Book",height=1,width=35,font=f2,command=search_book,fg="White",bg="#4d4545",bd=3)
panel.add(tp5)
tp5.place(x=15,y=210)
tp5.bind("<Enter>",hov)
tp5.bind("<Leave>",lea)
def hov(a):
    tp6.configure(fg="black",bg="white")
def lea(a):
    tp6.configure(fg="White",bg="#4d4545")
tp6=Button(panel,text="Search Student",height=1,width=35,font=f2,command=search_stud,fg="White",bg="#4d4545",bd=3)
panel.add(tp6)
tp6.place(x=15,y=250)
tp6.bind("<Enter>",hov)
tp6.bind("<Leave>",lea)
def hov(a):
    tp7.configure(fg="black",bg="white")
def lea(a):
    tp7.configure(fg="White",bg="#4d4545")
tp7=Button(panel,text="Remove Student",height=1,width=35,font=f2,command=remove_student,fg="White",bg="#4d4545",bd=3)
panel.add(tp7)
tp7.place(x=15,y=290)
tp7.bind("<Enter>",hov)
tp7.bind("<Leave>",lea)
def hov(a):
    tp11.configure(fg="black",bg="white")
def lea(a):
    tp11.configure(fg="White",bg="#4d4545")
tp11=Button(panel,text="Remove Book",height=1,width=35,font=f2,command=remove_book,fg="White",bg="#4d4545",bd=3)
panel.add(tp11)
tp11.place(x=15,y=330)
tp11.bind("<Enter>",hov)
tp11.bind("<Leave>",lea)

def hov(a):
    tp8.configure(fg="black",bg="white")
def lea(a):
    tp8.configure(fg="White",bg="#4d4545")
tp8=Button(panel,text="All Students Info",height=1,width=35,font=f2,command=all_info,fg="White",bg="#4d4545",bd=3)
panel.add(tp8)
tp8.place(x=15,y=370)
tp8.bind("<Enter>",hov)
tp8.bind("<Leave>",lea)
def hov(a):
    tp9.configure(fg="black",bg="white")
def lea(a):
    tp9.configure(fg="White",bg="#4d4545")
tp9=Button(panel,text="All Books Info",height=1,width=35,font=f2,command=all_book,fg="White",bg="#4d4545",bd=3)
panel.add(tp9)
tp9.place(x=15,y=410)
tp9.bind("<Enter>",hov)
tp9.bind("<Leave>",lea)
def hov(a):
    tp10.configure(fg="black",bg="white")
def lea(a):
    tp10.configure(fg="White",bg="#4d4545")
tp10=Button(panel,text="All Issued Books",height=1,width=35,font=f2,command=all_issue_books,fg="White",bg="#4d4545",bd=3)
panel.add(tp10)
tp10.place(x=15,y=450)
tp10.bind("<Enter>",hov)
tp10.bind("<Leave>",lea)
def hov(a):
    tp.configure(fg="black",bg="white")
def lea(a):
    tp.configure(fg="White",bg="#4d4545")
tp=Button(panel,text="Clear",height=1,width=35,font=f2,command=sleep,fg="White",bg="#4d4545",bd=3)
panel.add(tp)
tp.place(x=15,y=490)
tp.bind("<Enter>",hov)
tp.bind("<Leave>",lea)
panel_1=PanedWindow(panel,bd=2,height=560,width=990,bg="#4d4545")
panel.add(panel_1)
panel_1.place(x=350,y=0)




base.mainloop()




