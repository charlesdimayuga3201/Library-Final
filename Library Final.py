from tkinter import *
import tkinter as tk
import pymysql as p
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.ttk import Treeview
import datetime
from PIL import Image, ImageTk
from tkinter import Canvas, Entry, Text, Button, PhotoImage

b1,b2,b3,b4,b5,b6,b7,b8,sID,cur,con,e1,e2,e3,e4,e5,i,ps=None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
window,win=None,None
com1d,com1m,com1y,com2d,com2m,com2y=None,None,None,None,None,None

month=['January','February','March','April','May','June','July','August','September','October','November','December']
y = list(range(2020, 2040))
d = list(range(1,32))

def loginstd():
    global window,sID
    connectdb()
    for i in range(cur.rowcount):
        data=cur.fetchone()
        if e1.get().strip()==str(data[1]) and e2.get().strip()==(data[2]):
            sID=e1.get()
            print(sID)
            closedb()
            stud()
            break
    else:
        messagebox.showinfo("Error","Failed to Login")

def show_btn_book():
    btn_borrowbook = tk.PhotoImage(file = "./images/book_borrow.png")
    b1=Button(image=btn_borrowbook, borderwidth=0, highlightthickness=0, command=borrowbook)
    b1.place(x=312,y=307,width=125,height=53)
    b1.image=btn_borrowbook
    
    btn_returnbook = tk.PhotoImage(file = "./images/book_return.png")
    b2=Button(image=btn_returnbook, borderwidth=0, highlightthickness=0, command=returnbook)
    b2.place(x=442,y=307,width=125,height=53)
    b2.image=btn_returnbook

    btn_viewbook = tk.PhotoImage(file = "./images/book_view.png")
    b3=Button(image=btn_viewbook, borderwidth=0, highlightthickness=0, command=viewbook)
    b3.place(x=311,y=362,width=125,height=53)
    b3.image=btn_viewbook

    btn_returnbook = tk.PhotoImage(file = "./images/book_borrowed.png")
    b4=Button(image=btn_returnbook, borderwidth=0, highlightthickness=0, command=borrowedbook)
    b4.place(x=441,y=362,width=125,height=53)
    b4.image=btn_returnbook

def stud():
    global window
    window.destroy()
    global win,b1,b2,b3,b4
    win=Tk()
    win.title('Library')
    win.geometry("878x702")
    win.resizable(False,False)

    bg_image=tk.PhotoImage(file="./images/bg_img.png")
    bg_label=tk.Label(image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image=bg_image

    book_action = tk.PhotoImage(file = "./images/book_btn2.png")
    book_btn=Button(image=book_action, borderwidth=0, highlightthickness=0, command=show_btn_book)
    book_btn.place(x=364,y=248,width=150,height=53)
    book_btn.image=book_action

    logout_btn = tk.PhotoImage(file = "./images/logout_btn.png")
    b5=Button(image=logout_btn, borderwidth=0, highlightthickness=0, command=logout)
    b5.place(x=317.0,y=494.0,width=244.0,height=71.0)
    b5.image=logout_btn
    
    win.mainloop()

def stud1():
    global win,b1,b2,b3,b4
    win=Tk()
    win.title('Library')
    win.geometry("878x702")
    win.resizable(False,False)

    bg_image=tk.PhotoImage(file="./images/bg_img.png")
    bg_label=tk.Label(image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image=bg_image

    book_action = tk.PhotoImage(file = "./images/book_btn2.png")
    book_btn=Button(image=book_action, borderwidth=0, highlightthickness=0, command=show_btn_book)
    book_btn.place(x=364,y=248,width=150,height=53)
    book_btn.image=book_action

    logout_btn = tk.PhotoImage(file = "./images/logout_btn.png")
    b5=Button(image=logout_btn, borderwidth=0, highlightthickness=0, command=logout)
    b5.place(x=317.0,y=494.0,width=244.0,height=71.0)
    b5.image=logout_btn
    
    win.mainloop()

def closebooks():
    global win
    win.destroy()
    stud1()

def borrowbook():
    global win,sID
    win.destroy()
    win=Tk()
    win.title('BORROW Book')
    win.geometry("878x702")
    win.resizable(False,False)
    
    bg_image=tk.PhotoImage(file="./images/bg_img.png")
    bg_label=tk.Label(image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image=bg_image

    global e1,e2,b1,b2

    studid_lbl=Label(win,text='Student ID', font='Helvetica 12', bg="#F7F6F8")
    studid_lbl.place(x=230,y=227)
    bookid_lbl=Label(win,text='Book ID',  font='Helvetica 12', bg="#F7F6F8")
    bookid_lbl.place(x=448,y=227)
    borrowdate_lbl=Label(win,text='Borrow date',  font='Helvetica 12', bg="#F7F6F8")
    borrowdate_lbl.place(x=230,y=318)

    e1=Entry(win, bd=0,bg="#FFFFFF",highlightthickness=0, font='Helvetica 17')
    e1.place(x=230.0,y=255.0,width=194.0,height=50.0)
    e1.insert(0, sID)
    e1.configure(state = 'disabled')

    e2=Entry(win,bd=0,bg="#FFFFFF",highlightthickness=0, font='Helvetica 17')
    e2.place(x=447.0,y=255.0,width=194.0,height=50.0)

    retbook_btn = tk.PhotoImage(file = "./images/book_borrowbtn.png")
    b1=Button(image=retbook_btn, borderwidth=0, highlightthickness=0, command=borrowbooks)
    b1.place(x=230.0,y=494.0,width=194.0,height=71.0)

    close_bookbtn = tk.PhotoImage(file = "./images/close_btn.png")
    b2=Button(image=close_bookbtn, borderwidth=0, highlightthickness=0, command=closebooks)
    b2.place(x=447.0,y=494.0,width=194.0,height=71.0)

    # name=Label(win,text='BORROW ',font='Helvetica 30 bold')

    # sid=Label(win,text='Student ID')
    # no=Label(win,text='BOOK NO')
    # borrow=Label(win,text='BORROW DATE')
    # global e1,b,b1
    # e1=Entry(win,width=25)
    # e1.insert(0, sID)
    # e1.configure(state = 'disabled')
    # global e4
    # e4=Entry(win,width=25)
    
    global com1y,com1m,com1d
    com1y=Combobox(win,value=y, font='Helvetica 14')
    com1m=Combobox(win,value=month, font='Helvetica 14')
    com1d=Combobox(win,value=d, font='Helvetica 14')
    now=datetime.datetime.now()
    com1y.set(now.year)
    com1m.set(month[now.month-1])
    com1d.set(now.day)
    com1y.place(x=230,y=346,width=80.0,height=50.0)
    com1m.place(x=310,y=346,width=130.0,height=50.0)
    com1d.place(x=440,y=346,width=60.0,height=50.0)
    
    # b=Button(win, height=2,width=21,text=' BORROW BOOK ',command=borrowbooks)
    # b1=Button(win, height=2,width=21,text=' CLOSE ',command=closebooks)
    # name.place(x=55,y=30)
    # sid.place(x=70,y=130)
    # no.place(x=70,y=170)
    # borrow.place(x=70,y=210)
    # e1.place(x=180,y=130)
    # e4.place(x=180,y=170)
    
    # b.place(x=178,y=270)
    # b1.place(x=178,y=312)
    win.mainloop()

def borrowbooks():
    connectdb()
   
    check = "SELECT * FROM Book WHERE bookid=%s"
    ret = (e1.get(),)
    cur.execute(check, ret)
    result = cur.fetchone()
   
    if (result == None):
        messagebox.showinfo("Status", "Book not found!")
    else:
        q='INSERT INTO BookBorrow VALUE("%s","%s","%s","%s")'
        stats_borrow = 'Update Book Set status = %s Where bookid = %s'
        stats_b = "Not Available"
        for_book=(stats_b, e2.get())
        cur.execute(stats_borrow,for_book)
        con.commit()
        i=datetime.datetime(int(com1y.get()),month.index(com1m.get())+1,int(com1d.get()))
        i=i.isoformat()
        z = " "
        cur.execute(q%(e1.get(),e2.get(),i,z))
        con.commit()
        messagebox.showinfo("Success", "Book Borrowed!")
        closedb()
        win.destroy()
        stud1()
    
def returnbook():
    global win
    win.destroy()
    win=Tk()
    win.title('Return Book')
    win.geometry("878x702")
    win.resizable(False,False)
    bg_image=tk.PhotoImage(file="./images/bg_img.png")
    bg_label=tk.Label(image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image=bg_image

    global e1,b1

    bookid_lbl=Label(win,text='Book ID', font='Helvetica 12', bg="#F7F6F8")
    bookid_lbl.place(x=230,y=227)

    e1=Entry(win, bd=0,bg="#FFFFFF",highlightthickness=0, font='Helvetica 17')
    e1.place(x=230.0,y=255.0,width=194.0,height=50.0)

    retbook_btn = tk.PhotoImage(file = "./images/book_returnbtn.png")
    b1=Button(image=retbook_btn, borderwidth=0, highlightthickness=0, command=returnbooks)
    b1.place(x=230.0,y=494.0,width=194.0,height=71.0)

    close_bookbtn = tk.PhotoImage(file = "./images/close_btn.png")
    b2=Button(image=close_bookbtn, borderwidth=0, highlightthickness=0, command=closebooks)
    b2.place(x=447.0,y=494.0,width=194.0,height=71.0)

    # ret=Label(win,text='RETURN ',font='Helvetica 30 bold')
    # book=Label(win,text='BOOK',font='Helvetica 30 bold')
    # no=Label(win,text='BOOK NO')
    # exp=Label(win,text='')
    # global b,b1
    # global e4
    # e4=Entry(win,width=25)

    # b=Button(win, height=2,width=21,text=' RETURN BOOK ',command=returnbooks)
    # b1=Button(win, height=2,width=21,text=' CLOSE ',command=closebooks)
    # ret.place(x=55,y=30)
    # book.place(x=225,y=30)
    # no.place(x=70,y=120)
    # exp.place(x=70,y=200)
    # e4.place(x=180,y=120)
    # b.place(x=178,y=200)
    # b1.place(x=178,y=242)
    win.mainloop()

def returnbooks():
    connectdb()
    check = "SELECT * FROM Book WHERE bookid=%s"
    ret = (e1.get(),)
    cur.execute(check, ret)
    result = cur.fetchone()
    if (result == None):
        messagebox.showinfo("Result", "Book not found!")
    else:
        print (e1.get())
        r_book = 'Update Book set status = %s Where bookid = %s'
        s_book = "Available"
        o_result = (s_book, e1.get())
        cur.execute(r_book,o_result)
        con.commit()
    
        a='Update BookBorrow Set returnbook = %s Where bookids = %s '
        status = "Returned"
        val = (status,e1.get()) 
        cur.execute(a,val)
        con.commit()
    
        messagebox.showinfo("Success", "Book Returned!")
        closedb()
        win.destroy()
        stud1()

def viewbook():
    win=Tk()
    win.title('View Books')
    win.geometry("1000x300+270+180")
    win.resizable(False,False)

    treeview=Treeview(win,columns=("Book ID","Title","Author","Genre","Status"),show='headings')
    treeview.heading("Book ID", text="Book ID")
    treeview.heading("Title", text="Title")
    treeview.heading("Author", text="Author")
    treeview.heading("Genre", text="Genre")
    treeview.heading("Status", text="Status")
    treeview.column("Book ID", anchor='center')
    treeview.column("Title", anchor='center')
    treeview.column("Author", anchor='center')
    treeview.column("Genre", anchor='center')
    treeview.column("Status", anchor='center')
    index=0
    iid=0
    connectdb()
    q='SELECT * FROM Book'
    cur.execute(q)
    details=cur.fetchall()
    for row in details:
        treeview.insert("",index,iid,value=row)
        index=iid=index+1
    treeview.pack()
    win.mainloop()
    closedb()

def borrowedbook():
    connectdb()
    q='SELECT * FROM BookBorrow where stdid = %s'
    val = (sID,)
    cur.execute(q,val)
    details=cur.fetchall()
    if len(details)!=0:
        win=Tk()
        win.title('Borrowed  Books')
        win.geometry("800x300+270+180")
        win.resizable(False,False)    
        treeview=Treeview(win,columns=("Student ID","Book ID","Borrow Date","Return Book"),show='headings')
        treeview.heading("Student ID", text="Student ID")
        treeview.heading("Book ID", text="Book ID")
        treeview.heading("Borrow Date", text="Borrow Date")
        treeview.heading("Return Book", text="Return Book")
        treeview.column("Student ID", anchor='center')
        treeview.column("Book ID", anchor='center')
        treeview.column("Borrow Date", anchor='center')
        treeview.column("Return Book", anchor='center')
        index=0
        iid=0
        for row in details:
            treeview.insert("",index,iid,value=row)
            index=iid=index+1
        treeview.pack()
        win.mainloop()
    else:
        messagebox.showinfo("Message","No Book Borrowed!")
    closedb()

def loginadmin():
    if e1.get()=='admin' and e2.get()=='admin':
        admin()
    else:
        messagebox.showinfo("Error","Failed to Login!")

def show_btn_del():
    btn_delstud = tk.PhotoImage(file = "./images/del_stud.png")
    b6=Button(image=btn_delstud, borderwidth=0, highlightthickness=0, command=delete_student)
    b6.place(x=513,y=293,width=125,height=53)
    b6.image=btn_delstud
    
    btn_delbook = tk.PhotoImage(file = "./images/del_book.png")
    b7=Button(image=btn_delbook, borderwidth=0, highlightthickness=0, command=deletebook)
    b7.place(x=513,y=348,width=125,height=53)
    b7.image=btn_delbook

def show_btn_view():
    btn_viewstuds = tk.PhotoImage(file = "./images/view_studs.png")
    b3=Button(image=btn_viewstuds, borderwidth=0, highlightthickness=0, command=view_student)
    b3.place(x=374,y=293,width=125,height=53)
    b3.image=btn_viewstuds
    
    btn_viewbooks = tk.PhotoImage(file = "./images/view_books.png")
    b4=Button(image=btn_viewbooks, borderwidth=0, highlightthickness=0, command=viewbook)
    b4.place(x=374,y=348,width=125,height=53)
    b4.image=btn_viewbooks

    btn_viewborrowed = tk.PhotoImage(file = "./images/view_bboks.png")
    b4=Button(image=btn_viewborrowed, borderwidth=0, highlightthickness=0, command=borrowedbook1)
    b4.place(x=374,y=403,width=125,height=73)
    b4.image=btn_viewborrowed

def show_btn_add():
    btn_addstud = tk.PhotoImage(file = "./images/add_stud.png")
    b1=Button(image=btn_addstud, borderwidth=0, highlightthickness=0, command=add_student)
    b1.place(x=237,y=293,width=125,height=53)
    b1.image=btn_addstud
    
    btn_addbook = tk.PhotoImage(file = "./images/add_book.png")
    b2=Button(image=btn_addbook, borderwidth=0, highlightthickness=0, command=addbook)
    b2.place(x=236,y=348,width=125,height=53)
    b2.image=btn_addbook

def admin():
    window.destroy()
    global win,b1,b2,b3,b4,cur,con
    win=Tk()
    win.title('Admin')
    win.geometry("878x702")
    win.resizable(False,False)

    background_image=tk.PhotoImage(file="./images/bg_img.png")
    background_label=tk.Label(image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image=background_image 

    addimg = tk.PhotoImage(file = "./images/add_img.png")
    add_btn=Button(image=addimg, borderwidth=0, highlightthickness=0, command=show_btn_add)
    add_btn.place(x=237,y=238,width=125,height=53)
    add_btn.image=addimg
    
    viewimg = tk.PhotoImage(file = "./images/view_img.png")
    view_btn=Button(image=viewimg, borderwidth=0, highlightthickness=0, command=show_btn_view)
    view_btn.place(x=375,y=238,width=125,height=53)
    view_btn.image=viewimg

    delimg = tk.PhotoImage(file = "./images/del_img.png")
    del_btn=Button(image=delimg, borderwidth=0, highlightthickness=0, command=show_btn_del)
    del_btn.place(x=513,y=238,width=125,height=53)
    del_btn.image=delimg

    logout_btn = tk.PhotoImage(file = "./images/logout_btn.png")
    b8=Button(image=logout_btn, borderwidth=0, highlightthickness=0, command=logout)
    b8.place(x=317.0,y=494.0,width=244.0,height=71.0)
    b8.image=logout_btn

    win.mainloop()

def admin1():
    global win,b1,b2,b3,b4,cur,con
    win=Tk()
    win.title('Admin')
    win.geometry("878x702")
    win.resizable(False,False)

    background_image=tk.PhotoImage(file="./images/bg_img.png")
    background_label=tk.Label(image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image=background_image 

    addimg = tk.PhotoImage(file = "./images/add_img.png")
    add_btn=Button(image=addimg, borderwidth=0, highlightthickness=0, command=show_btn_add)
    add_btn.place(x=237,y=238,width=125,height=53)
    add_btn.image=addimg
    
    viewimg = tk.PhotoImage(file = "./images/view_img.png")
    view_btn=Button(image=viewimg, borderwidth=0, highlightthickness=0, command=show_btn_view)
    view_btn.place(x=375,y=238,width=125,height=53)
    view_btn.image=viewimg

    delimg = tk.PhotoImage(file = "./images/del_img.png")
    del_btn=Button(image=delimg, borderwidth=0, highlightthickness=0, command=show_btn_del)
    del_btn.place(x=513,y=238,width=125,height=53)
    del_btn.image=delimg

    logout_btn = tk.PhotoImage(file = "./images/logout_btn.png")
    b8=Button(image=logout_btn, borderwidth=0, highlightthickness=0, command=logout)
    b8.place(x=317.0,y=494.0,width=244.0,height=71.0)
    b8.image=logout_btn

def logout():    
    win.destroy()
    try:
        closedb()
    except:
        print("Logged Out")
    home()

def closedb():
    global con,cur
    cur.close()
    con.close()

def addbook():
    global win
    win.destroy()
    win=Tk()
    win.title('Add Book')
    win.geometry("878x702")
    win.resizable(False,False)

    bg_image=tk.PhotoImage(file="./images/bg_img.png")
    bg_label=tk.Label(image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image=bg_image

    global b,b1,b5,b4,e1,e2,e3,e4

    bookid_lbl=Label(win,text='Book ID', font='Helvetica 12', bg="#F7F6F8")
    bookid_lbl.place(x=230,y=227)
    title_label=Label(win,text='Title',  font='Helvetica 12', bg="#F7F6F8")
    title_label.place(x=448,y=227)
    author_lbl=Label(win,text='Author',  font='Helvetica 12', bg="#F7F6F8")
    author_lbl.place(x=230,y=318)
    genre_lbl=Label(win,text='Genre',  font='Helvetica 12', bg="#F7F6F8")
    genre_lbl.place(x=448,y=318)

    e1=Entry(win, bd=0,bg="#FFFFFF",highlightthickness=0, font='Helvetica 17')
    e1.place(x=230.0,y=255.0,width=194.0,height=50.0)
    e2=Entry(win,bd=0,bg="#FFFFFF",highlightthickness=0, font='Helvetica 17')
    e2.place(x=447.0,y=255.0,width=194.0,height=50.0)
    e3=Entry(win,bd=0,bg="#FFFFFF",highlightthickness=0, font='Helvetica 17')
    e3.place(x=230.0,y=346.0,width=194.0,height=50.0)
    e4=Entry(win,bd=0,bg="#FFFFFF",highlightthickness=0, font='Helvetica 17')
    e4.place(x=447.0,y=346.0,width=194.0,height=50.0)

    addbook_btn = tk.PhotoImage(file = "./images/addbook_todb.png")
    b1=Button(image=addbook_btn, borderwidth=0, highlightthickness=0, command=addbooks)
    b1.place(x=230.0,y=494.0,width=194.0,height=71.0)

    close_bookbtn = tk.PhotoImage(file = "./images/close_btn.png")
    b2=Button(image=close_bookbtn, borderwidth=0, highlightthickness=0, command=closebooks1)
    b2.place(x=447.0,y=494.0,width=194.0,height=71.0)

    win.mainloop()

def closebooks1():
    global win
    win.destroy()
    admin1()

def addbooks():
    connectdb()
    q='INSERT INTO Book VALUE("%i","%s","%s","%s","%s")'
    global cur,con
    stats = "Available"
    cur.execute(q%(int(e1.get()),e2.get(),e3.get(),e4.get(),stats))
    con.commit()
   
    messagebox.showinfo("Success", "Book Added!")
    closedb()
    win.destroy()
    admin1()

def viewbook():
    win=Tk()
    win.title('View Books')
    win.geometry("1000x300+270+180")

    treeview=Treeview(win,columns=("Book ID","Title","Author","Genre","Status"),show='headings')
    treeview.heading("Book ID", text="Book ID")
    treeview.heading("Title", text="Title")
    treeview.heading("Author", text="Author")
    treeview.heading("Genre", text="Genre")
    treeview.heading("Status", text="Status")
    treeview.column("Book ID", anchor='center')
    treeview.column("Title", anchor='center')
    treeview.column("Author", anchor='center')
    treeview.column("Genre", anchor='center')
    treeview.column("Status", anchor='center')
    index=0
    iid=0
    connectdb()
    q='SELECT * FROM Book'
    cur.execute(q)
    details=cur.fetchall()
    for row in details:
        treeview.insert("",index,iid,value=row)
        index=iid=index+1
    treeview.pack()
    win.mainloop()
    closedb()

def deletebook():
    global win
    win.destroy()
    win=Tk()
    win.title('Delete Book')
    win.geometry("878x702")
    win.resizable(False,False)

    bg_image=tk.PhotoImage(file="./images/bg_img.png")
    bg_label=tk.Label(image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image=bg_image

    global e1,e2,b1,b2

    bookid_lbl=Label(win,text='Book ID', font='Helvetica 12', bg="#F7F6F8")
    bookid_lbl.place(x=230,y=227)
    adminpass_lbl=Label(win,text='Admin Password',  font='Helvetica 12', bg="#F7F6F8")
    adminpass_lbl.place(x=448,y=227)

    e1=Entry(win, bd=0,bg="#FFFFFF",highlightthickness=0, font='Helvetica 17')
    e1.place(x=230.0,y=255.0,width=194.0,height=50.0)
    e2=Entry(win,bd=0,bg="#FFFFFF",highlightthickness=0, font='Helvetica 17')
    e2.place(x=447.0,y=255.0,width=194.0,height=50.0)

    delbook_btn = tk.PhotoImage(file = "./images/delbook_fdb.png")
    b1=Button(image=delbook_btn, borderwidth=0, highlightthickness=0, command=deletebooks)
    b1.place(x=230.0,y=494.0,width=194.0,height=71.0)

    close_bookbtn = tk.PhotoImage(file = "./images/close_btn.png")
    b2=Button(image=close_bookbtn, borderwidth=0, highlightthickness=0, command=closebooks1)
    b2.place(x=447.0,y=494.0,width=194.0,height=71.0)

    win.mainloop()

def deletebooks():
    connectdb()
    bk = 'SELECT * FROM Book WHERE bookid= %s'
    s_book = (e1.get(),)
    cur.execute(bk,s_book)
    d_book =cur.fetchone()
    if(d_book == None):
        messagebox.showinfo("Message", "Book not found!")
    else:
        if e2.get()=='admin':
            q='DELETE FROM Book WHERE bookid="%i"'
            cur.execute(q%(int(e1.get())))
            con.commit()
            
            messagebox.showinfo("Success", "Book Deleted!")
            closedb()
            win.destroy()
            admin1()
        else:
            messagebox.showinfo("Error", "Incorrect Password!")
            closedb()

def add_student():
    global win
    win.destroy()
    win=Tk()
    win.title('Add Student')
    win.geometry("878x702")
    win.resizable(False,False)

    bg_image=tk.PhotoImage(file="./images/bg_img.png")
    bg_label=tk.Label(image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image=bg_image 

    global e1,b,e2,e3,e4,e5

    name_lbl=Label(win,text='Name', font='Helvetica 12', bg="#F7F6F8")
    name_lbl.place(x=230,y=213)
    studid_lbl=Label(win,text='Student ID',  font='Helvetica 12', bg="#F7F6F8")
    studid_lbl.place(x=230,y=305)
    pass_lbl=Label(win,text='Password',  font='Helvetica 12', bg="#F7F6F8")
    pass_lbl.place(x=448,y=305)
    yearlvl_lbl=Label(win,text='Year Level',  font='Helvetica 12', bg="#F7F6F8")
    yearlvl_lbl.place(x=230,y=396)
    course_lbl=Label(win,text='Course',  font='Helvetica 12', bg="#F7F6F8")
    course_lbl.place(x=448,y=396)

    e1=Entry(win, bd=0,bg="#FFFFFF",highlightthickness=0, font='Helvetica 17')
    e1.place(x=230.0,y=241.0,width=411.0,height=50.0)
    e2=Entry(win,bd=0,bg="#FFFFFF",highlightthickness=0, font='Helvetica 17')
    e2.place(x=230.0,y=333.0,width=194.0,height=50.0)
    e3=Entry(win,bd=0,bg="#FFFFFF",highlightthickness=0, font='Helvetica 17')
    e3.place(x=447.0,y=333.0,width=194.0,height=50.0)
    e4=Entry(win,bd=0,bg="#FFFFFF",highlightthickness=0, font='Helvetica 17')
    e4.place(x=230.0,y=424.0,width=194.0,height=50.0)
    e5=Entry(win,bd=0,bg="#FFFFFF",highlightthickness=0, font='Helvetica 17')
    e5.place(x=447.0,y=424.0,width=194.0,height=50.0)

    addstud_btn = tk.PhotoImage(file = "./images/addstud_todb.png")
    b1=Button(image=addstud_btn, borderwidth=0, highlightthickness=0, command=add_students)
    b1.place(x=230.0,y=494.0,width=194.0,height=71.0)

    close_studbtn = tk.PhotoImage(file = "./images/close_btn.png")
    b2=Button(image=close_studbtn, borderwidth=0, highlightthickness=0, command=close_students)
    b2.place(x=447.0,y=494.0,width=194.0,height=71.0)

    win.mainloop()

def add_students():
    connectdb()
    global con,cur
    us1 = "SELECT * FROM Login where studid = %s"
    ck = (e2.get(),)
    cur.execute(us1,ck)
    done = cur.fetchone()
    if(done != None):
         messagebox.showinfo("Message", "Student ID Exist!")

    else:
        q='INSERT INTO Login VALUE("%s","%i","%s","%s","%s")'
        
        cur.execute(q%(e1.get(),int(e2.get()),e3.get(),e4.get(),e5.get()))
        con.commit()
       
        messagebox.showinfo("Success", "Student Added!")
        closedb()
        win.destroy()
        admin1()

def close_students():
    global win
    win.destroy()
    admin1()

def view_student():
    win=Tk()
    win.title('View Student')
    win.geometry("1000x300+270+180")
    win.resizable(False,False)
    treeview=Treeview(win,columns=("Name","Student ID","Password","YearLevel","Course"),show='headings')
    treeview.heading("Name", text="Name")
    treeview.heading("Student ID", text="Student ID")
    treeview.heading("Password", text="Password")
    treeview.heading("YearLevel", text="YearLevel")
    treeview.heading("Course", text="Course")
    treeview.column("Name", anchor='center')
    treeview.column("Student ID", anchor='center')
    treeview.column("Password", anchor='center')
    treeview.column("YearLevel", anchor='center')
    treeview.column("Course", anchor='center')
    index=0
    iid=0
    connectdb()
    details=cur.fetchall()
    for row in details:
        treeview.insert("",index,iid,value=row)
        index=iid=index+1
    treeview.pack()
    win.mainloop()
    closedb()

def borrowedbook1():
    connectdb()
    q='SELECT * FROM BookBorrow '
    cur.execute(q)
    details=cur.fetchall()
    if len(details)!=0:
        win=Tk()
        win.title('Borrowed Books')
        win.geometry("800x300+270+180")
        win.resizable(False,False)    
        treeview=Treeview(win,columns=("Student ID","Book ID","Borrow Date","Return Book"),show='headings')
        treeview.heading("Student ID", text="Student ID")
        treeview.heading("Book ID", text="Book ID")
        treeview.heading("Borrow Date", text="Borrow Date")
        treeview.heading("Return Book", text="Return Book")
        treeview.column("Student ID", anchor='center')
        treeview.column("Book ID", anchor='center')
        treeview.column("Borrow Date", anchor='center')
        treeview.column("Return Book", anchor='center')
        index=0
        iid=0
        for row in details:
            treeview.insert("",index,iid,value=row)
            index=iid=index+1
        treeview.pack()
        win.mainloop()
    else:
        messagebox.showinfo("Message","No Book Borrowed!")
    closedb()

def delete_student():
    global win
    win.destroy()
    win=Tk()
    win.title('Delete Studet')
    win.geometry("878x702")
    win.resizable(False,False)

    bg_image=tk.PhotoImage(file="./images/bg_img.png")
    bg_label=tk.Label(image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image=bg_image

    global e1,e2,b1,b2

    studid_lbl=Label(win,text='Student ID', font='Helvetica 12', bg="#F7F6F8")
    studid_lbl.place(x=230,y=227)
    adminpass_lbl=Label(win,text='Admin Password',  font='Helvetica 12', bg="#F7F6F8")
    adminpass_lbl.place(x=448,y=227)

    e1=Entry(win, bd=0,bg="#FFFFFF",highlightthickness=0, font='Helvetica 17')
    e1.place(x=230.0,y=255.0,width=194.0,height=50.0)
    e2=Entry(win,bd=0,bg="#FFFFFF",highlightthickness=0, font='Helvetica 17')
    e2.place(x=447.0,y=255.0,width=194.0,height=50.0)

    delbook_btn = tk.PhotoImage(file = "./images/delstud_fdb.png")
    b1=Button(image=delbook_btn, borderwidth=0, highlightthickness=0, command=delete_students)
    b1.place(x=230.0,y=494.0,width=194.0,height=71.0)

    close_bookbtn = tk.PhotoImage(file = "./images/close_btn.png")
    b2=Button(image=close_bookbtn, borderwidth=0, highlightthickness=0, command=closebooks1)
    b2.place(x=447.0,y=494.0,width=194.0,height=71.0)

    win.mainloop()

def delete_students():
    connectdb()
    check = "SELECT * FROM Login WHERE studid=%s"
    ret = (e1.get(),)
    cur.execute(check, ret)
    result = cur.fetchone()
    if (result == None):
         messagebox.showinfo("Result", "Student Not Found!")
    else:
        if e2.get()=='admin':
            q='DELETE FROM Login WHERE studid="%i"'
            cur.execute(q%(int(e1.get())))
            con.commit()
            
            messagebox.showinfo("Success", "Student Deleted!")
            closedb()
            win.destroy()
            admin1()
        else:
            messagebox.showinfo("Error", "Incorrect Password!")
            closedb()

def connectdb():
    global con,cur
    #Enter your username and password of MySQL
    con=p.connect(host="localhost",user="root",passwd="")
    cur=con.cursor()
    cur.execute('CREATE DATABASE IF NOT EXISTS LIBRARY')
    cur.execute('USE LIBRARY')
    global enter
    if enter==1:
        l='CREATE TABLE IF NOT EXISTS Login(name varchar(50),studid varchar(10),password varchar(30),yearlevel varchar(20),course varchar(20))'
        b='CREATE TABLE IF NOT EXISTS Book(bookid int(15), title varchar(50),author varchar(50),genre varchar(50),status varchar(20))'
        i='CREATE TABLE IF NOT EXISTS BookBorrow(stdid varchar(50),bookids varchar(50),borrow date,returnbook varchar(20))'
        cur.execute(l)
        cur.execute(b)
        cur.execute(i)
        enter=enter+1
    query='SELECT * FROM Login'
    cur.execute(query)

def home():
    try:
        global window,b1,b2,e1,e2,con,cur,win
        window=Tk()
        window.title('Library Management System')
        window.resizable(False,False)
        window.geometry("878x702")
        
        bg_image=tk.PhotoImage(file="./images/bg_img.png")
        bg_label=tk.Label(image=bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image=bg_image 
        
        usid=Label(window,text='Student ID', font='Helvetica 12', bg="#F7F6F8")
        usid.place(x=260,y=200)
        paswrd=Label(window,text='Password',  font='Helvetica 12', bg="#F7F6F8")
        paswrd.place(x=260,y=293)

        e1=Entry(window, bd=0,bg="#FFFFFF",highlightthickness=0, font='Helvetica 17')
        e1.place(x=260.0,y=228.0,width=359.0,height=58.0)
        e2=Entry(window,bd=0,bg="#FFFFFF",highlightthickness=0, font='Helvetica 17', show = "*")
        e2.place(x=260.0,y=320.0,width=358.0,height=58.0)

        std_btn_img = tk.PhotoImage(file = "./images/std_img_log.png")
        b1=Button(image=std_btn_img, borderwidth=0, highlightthickness=0, command=loginstd)
        b1.place(x=251.0,y=410.0,width=375.0,height=71.0)
        admin_btn_img = tk.PhotoImage(file = "./images/admin_img_log.png")
        b2=Button(image=admin_btn_img, borderwidth=0, highlightthickness=0, command=loginadmin)
        b2.place(x=249.0,y=486.0,width=375.0,height=71.0)

        window.mainloop()
    except Exception:
        window.destroy()
enter = 1 
home()
