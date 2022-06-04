from asyncio.windows_events import NULL
from tkinter import *
import tkinter as tk
import pymysql as p
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.ttk import Treeview
import datetime
from PIL import Image, ImageTk
# from tkinter import Canvas, Entry, Text, Button, PhotoImage

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

# mini drop down, actions in book
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
    win.resizable(False,False)

    global screen_height, screen_width, x_cordinate, y_cordinate
    window_width = 878
    window_height = 702
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

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
    win.resizable(False,False)

    global screen_height, screen_width, x_cordinate, y_cordinate
    window_width = 878
    window_height = 702
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

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
    win.title('Borrow Book')
    win.resizable(False,False)
    
    global screen_height, screen_width, x_cordinate, y_cordinate
    window_width = 878
    window_height = 702
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

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

    brw_bookbtn = tk.PhotoImage(file = "./images/book_borrowbtn.png")
    b1=Button(image=brw_bookbtn, borderwidth=0, highlightthickness=0, command=borrowbooks)
    b1.place(x=230.0,y=494.0,width=194.0,height=71.0)

    close_bookbtn = tk.PhotoImage(file = "./images/close_btn.png")
    b2=Button(image=close_bookbtn, borderwidth=0, highlightthickness=0, command=closebooks)
    b2.place(x=447.0,y=494.0,width=194.0,height=71.0)
    
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
    win.mainloop()

def borrowbooks():
    connectdb()
    
    if (e2.get() != ""):

        print (e2.get())
        check1 = "SELECT status FROM Book WHERE bookid=%s"
        ret1 = (e2.get(),)
        cur.execute(check1, ret1)
        result = cur.fetchone()
        if(result != None):    
            if(result[0] == 'Not Available'):
                messagebox.showinfo("Message", "Book already Borrowed!")

            else: 
                stats_borrow = 'UPDATE Book Set status = %s Where bookid = %s'
                stats_b = "Not Available"
                
                for_book=(stats_b, e2.get())
                cur.execute(stats_borrow,for_book)
                con.commit()

                q='INSERT INTO BookBorrow(stdid,bookid,borrowdate,returndate)VALUE("%s","%s","%s",NULL)'
                i=datetime.datetime(int(com1y.get()),month.index(com1m.get())+1,int(com1d.get()))
                i=i.isoformat()
              
                cur.execute(q%(e1.get(),e2.get(),i))
                con.commit()
                messagebox.showinfo("Success", "Book Borrowed!")
                closedb()
                win.destroy()
                stud1()
        else:
            messagebox.showinfo("Message", "No book Found!")
    else: 
         messagebox.showinfo("Error", "Field can't be Empty!")
def returnbook():
    global win,sID
    win.destroy()
    win=Tk()
    win.title('Return Book')
    win.resizable(False,False)

    global screen_height, screen_width, x_cordinate, y_cordinate
    window_width = 878
    window_height = 702
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    bg_image=tk.PhotoImage(file="./images/bg_img.png")
    bg_label=tk.Label(image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image=bg_image

    global e1,e2,b1
    studid_lbl=Label(win,text='Student ID', font='Helvetica 12', bg="#F7F6F8")
    studid_lbl.place(x=230,y=227)
    bookid_lbl=Label(win,text='Borrow Key',  font='Helvetica 12', bg="#F7F6F8")
    bookid_lbl.place(x=448,y=227)
    borrowdate_lbl=Label(win,text='Return date',  font='Helvetica 12', bg="#F7F6F8")
    borrowdate_lbl.place(x=230,y=318)

    e1=Entry(win, bd=0,bg="#FFFFFF",highlightthickness=0, font='Helvetica 17')
    e1.place(x=230.0,y=255.0,width=194.0,height=50.0)
    e1.insert(0, sID)
    e1.configure(state = 'disabled')

    e2=Entry(win, bd=0,bg="#FFFFFF",highlightthickness=0, font='Helvetica 17')
    e2.place(x=447.0,y=255.0,width=194.0,height=50.0)

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
    
    retbook_btn = tk.PhotoImage(file = "./images/book_returnbtn.png")
    b1=Button(image=retbook_btn, borderwidth=0, highlightthickness=0, command=returnbooks)
    b1.place(x=230.0,y=494.0,width=194.0,height=71.0)

    close_bookbtn = tk.PhotoImage(file = "./images/close_btn.png")
    b2=Button(image=close_bookbtn, borderwidth=0, highlightthickness=0, command=closebooks)
    b2.place(x=447.0,y=494.0,width=194.0,height=71.0)

    
    win.mainloop()

def returnbooks():
    connectdb()
    if (e2.get() != ""):
        n_var = 'SELECT bookid FROM BookBorrow WHERE borrowkey=%s'
        n_val = (e2.get(),)
        cur.execute(n_var,n_val)
        n_result = cur.fetchone()
        
        if(n_result != None):
            s_var = 'SELECT stdid FROM BookBorrow where borrowkey = %s'
            s_val = (e2.get())
            cur.execute(s_var, s_val)
            s_result = cur.fetchone()
            if(s_result[0] == e1.get()):
                print (e2.get())
                check1 = "SELECT status FROM Book WHERE bookid=%s"
                ret1 = (n_result[0],)
                cur.execute(check1, ret1)
                result = cur.fetchone()

                if(result != None):
                    d_var = 'SELECT returndate FROM BookBorrow where borrowkey = %s'
                    d_val = (e2.get())
                    cur.execute(d_var, d_val)
                    d_result = cur.fetchone()
                    if(result[0] == 'Not Available' and d_result[0] == None):
                        check = "SELECT * FROM Book WHERE bookid=%s"
                        ret = (ret1)
                        cur.execute(check, ret)
                        result = cur.fetchone()
                        if (result == None):
                            messagebox.showinfo("Message", "Book not Found!")
                        else:
                            print (e2.get())
                            r_book = 'UPDATE Book SET status = %s Where bookid = %s'
                            s_book = "Available"
                            o_result = (s_book, n_result[0])
                            cur.execute(r_book,o_result)
                            con.commit()
                            
                            a='UPDATE BookBorrow SET returndate = %s Where  borrowkey = %s'
                            i=datetime.datetime(int(com1y.get()),month.index(com1m.get())+1,int(com1d.get()))
                            i=i.isoformat()
                            stats_ret = i 
                            val = (stats_ret,e2.get()) 
                            
                            cur.execute(a,val)
                            con.commit()
                        
                            messagebox.showinfo("Success", "Book Returned!")
                            closedb()
                            win.destroy()
                            stud1()

                    else: 
                        messagebox.showinfo("Success", "Book already Returned!")
                else:
                    messagebox.showinfo("Message", "Book not Found!")
            else:
                messagebox.showinfo("Message", "Book borrowed by other student!")
        else:
            messagebox.showinfo("Message", "Borrow Key Not Found!")
    else:
        messagebox.showinfo("Error", "Field can't be Empty!")
    
def viewbook():
    connectdb()
    q='SELECT * FROM Book'
    cur.execute(q)
    details=cur.fetchall()
    if len(details)!=0:
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

        for row in details:
            treeview.insert("",index,iid,value=row)
            index=iid=index+1
        treeview.pack()
        win.mainloop()
    else:
        messagebox.showinfo("Message","No book Lists!")
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
        win.geometry("1000x300+270+180")
        win.resizable(False,False)    
        treeview=Treeview(win,columns=("Borrow Key","Student ID","Book ID","Borrow Date","Return Date"),show='headings')
        treeview.heading("Borrow Key", text="Borrow Key")
        treeview.heading("Student ID", text="Student ID")
        treeview.heading("Book ID", text="Book ID")
        treeview.heading("Borrow Date", text="Borrow Date")
        treeview.heading("Return Date", text="Return Date")
        treeview.column("Borrow Key", anchor='center')
        treeview.column("Student ID", anchor='center')
        treeview.column("Book ID", anchor='center')
        treeview.column("Borrow Date", anchor='center')
        treeview.column("Return Date", anchor='center')
        index=0
        iid=0
        for row in details:
            treeview.insert("",index,iid,value=row)
            index=iid=index+1
        treeview.pack()
        win.mainloop()
    else:
        messagebox.showinfo("Message","No book Borrowed!")
    closedb()

def loginadmin():
    if e1.get()=='admin' and e2.get()=='admin':
        admin()
    else:
        messagebox.showinfo("Error","Failed to Login!")

def show_btn_del():
    btn_delstud = tk.PhotoImage(file = "./images/delete_stud.png")
    b6=Button(image=btn_delstud, borderwidth=0, highlightthickness=0, command=delete_student)
    b6.place(x=513,y=293,width=125,height=53)
    b6.image=btn_delstud
    
    btn_delbook = tk.PhotoImage(file = "./images/delete_book.png")
    b7=Button(image=btn_delbook, borderwidth=0, highlightthickness=0, command=deletebook)
    b7.place(x=513,y=348,width=125,height=53)
    b7.image=btn_delbook
     
    btn_delbook1 = tk.PhotoImage(file = "./images/delete_record.png")
    b8=Button(image=btn_delbook1, borderwidth=0, highlightthickness=0, command=delborrowed_rec)
    b8.place(x=513,y=403,width=125,height=53)
    b8.image=btn_delbook1

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
    win.resizable(False,False)

    global screen_height, screen_width, x_cordinate, y_cordinate
    window_width = 878
    window_height = 702
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

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

    delimg = tk.PhotoImage(file = "./images/delete_img.png")
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
    win.resizable(False,False)

    global screen_height, screen_width, x_cordinate, y_cordinate
    window_width = 878
    window_height = 702
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

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

    delimg = tk.PhotoImage(file = "./images/delete_img.png")
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
    win.resizable(False,False)

    global screen_height, screen_width, x_cordinate, y_cordinate
    window_width = 878
    window_height = 702
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

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
    global cur,con
    if (e1.get() == "" or e2.get() == "" or e3.get() == "" or e4.get() == ""):
        messagebox.showinfo("Error", "Field can't be Empty!")
    else:
        us1 = "SELECT * FROM Book where bookid = %s"
        ck = (e1.get(),)
        cur.execute(us1,ck)
        done = cur.fetchone()
        if(done != None):
            messagebox.showinfo("Message", "Book ID Exist!")
        else:
            q='INSERT INTO Book VALUE("%i","%s","%s","%s","%s")'
            
            stats = "Available"
            cur.execute(q%(int(e1.get()),e2.get(),e3.get(),e4.get(),stats))
            con.commit()
        
            messagebox.showinfo("Success", "Book Added!")
            closedb()
            win.destroy()
            admin1()

def add_student():
    global win
    win.destroy()
    win=Tk()
    win.title('Add Student')
    win.resizable(False,False)

    global screen_height, screen_width, x_cordinate, y_cordinate
    window_width = 878
    window_height = 702
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

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

    if (e1.get() == "" or e2.get() == "" or e3.get() == "" or e4.get() == "" or e5.get() == ""):
        messagebox.showinfo("Error", "Field can't be Empty!")

    else: 
        us1 = "SELECT * FROM Student where studid = %s"
        ck = (e2.get(),)
        cur.execute(us1,ck)
        done = cur.fetchone()
        if(done != None):
            messagebox.showinfo("Message", "Student ID Exist!")

        else:
            q='INSERT INTO Student VALUE("%s","%i","%s","%s","%s")'
            
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
    connectdb()
    q='SELECT * FROM Student'
    cur.execute(q)
    details=cur.fetchall()
    if len(details)!=0:
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

        for row in details:
            treeview.insert("",index,iid,value=row)
            index=iid=index+1
        treeview.pack()
        win.mainloop()
    else:
        messagebox.showinfo("Message","No student Lists!")
    closedb()

def borrowedbook1():
    connectdb()
    
    q='SELECT * FROM BookBorrow '
    cur.execute(q)
    details=cur.fetchall()
    if len(details)!=0:
        win=Tk()
        win.title('Borrowed Books')
        win.geometry("1000x300+270+180")
        win.resizable(False,False)    
        treeview=Treeview(win,columns=("Borrow Key","Student ID","Book ID","Borrow Date","Return Date"),show='headings')
        treeview.heading("Borrow Key", text="Borrow Key")
        treeview.heading("Student ID", text="Student ID")
        treeview.heading("Book ID", text="Book ID")
        treeview.heading("Borrow Date", text="Borrow Date")
        treeview.heading("Return Date", text="Return Date")
        treeview.column("Borrow Key", anchor='center')
        treeview.column("Student ID", anchor='center')
        treeview.column("Book ID", anchor='center')
        treeview.column("Borrow Date", anchor='center')
        treeview.column("Return Date", anchor='center')
        index=0
        iid=0
        for row in details:
            treeview.insert("",index,iid,value=row)
            index=iid=index+1
        treeview.pack()
        win.mainloop()
    else:
        messagebox.showinfo("Message","No book Borrowed!")
    closedb()

def delete_student():
    global win
    win.destroy()
    win=Tk()
    win.title('Delete Studet')
    win.resizable(False,False)

    global screen_height, screen_width, x_cordinate, y_cordinate
    window_width = 878
    window_height = 702
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    bg_image=tk.PhotoImage(file="./images/bg_img.png")
    bg_label=tk.Label(image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image=bg_image

    global e1,e2,b1,b2

    studid_lbl=Label(win,text='Student ID', font='Helvetica 12', bg="#F7F6F8")
    studid_lbl.place(x=230,y=227)

    e1=Entry(win, bd=0,bg="#FFFFFF",highlightthickness=0, font='Helvetica 17')
    e1.place(x=230.0,y=255.0,width=194.0,height=50.0)

    delstud_btn = tk.PhotoImage(file = "./images/delrec_fdb.png")
    b1=Button(image=delstud_btn, borderwidth=0, highlightthickness=0, command=delsingle_stud)
    b1.place(x=230.0,y=410.0,width=194.0,height=71.0)

    delallstud_btn = tk.PhotoImage(file = "./images/delall.png")
    b2=Button(image=delallstud_btn, borderwidth=0, highlightthickness=0, command=delall_stud)
    b2.place(x=447.0,y=410.0,width=194.0,height=71.0)

    close_bookbtn = tk.PhotoImage(file = "./images/close_btn.png")
    b3=Button(image=close_bookbtn, borderwidth=0, highlightthickness=0, command=closebooks1)
    b3.place(x=341.0,y=494.0,width=194.0,height=71.0)

    win.mainloop()

def delall_stud():
    global win
    connectdb()
    q='SELECT * FROM Student'
    cur.execute(q)
    details=cur.fetchall()
    if len(details)!=0:
        MsgBox = messagebox.askquestion ('Delete all','This will delete all student. Are you sure?', icon = 'warning')
        if MsgBox == 'yes':
            q='DELETE FROM Student'
            cur.execute(q)
            con.commit()
            
            messagebox.showinfo("Success", "Students Deleted!")
            closedb()
            win.destroy()
            admin1()
    else:
        messagebox.showinfo("Message","No students to Delete!")
    closedb()

def delsingle_stud():
    connectdb()
    if (e1.get() == ""):
        messagebox.showinfo("Error", "Field can't be Empty!")
    else:
        check = "SELECT * FROM Student WHERE studid=%s"
        ret = (e1.get(),)
        cur.execute(check, ret)
        result = cur.fetchone()
        if (result == None):
            messagebox.showinfo("Result", "Student Not Found!")
        else:
            MsgBox = messagebox.askquestion ('Delete','Are you sure you want to delete?', icon = 'warning')
            if MsgBox == 'yes':
                q='DELETE FROM Student WHERE studid="%i"'
                cur.execute(q%(int(e1.get())))
                con.commit()
                
                messagebox.showinfo("Success", "Student Deleted!")
                closedb()
                win.destroy()
                admin1()
    closedb()

def deletebook():
    global win
    win.destroy()
    win=Tk()
    win.title('Delete Book')
    win.resizable(False,False)

    global screen_height, screen_width, x_cordinate, y_cordinate
    window_width = 878
    window_height = 702
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    bg_image=tk.PhotoImage(file="./images/bg_img.png")
    bg_label=tk.Label(image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image=bg_image

    global e1,e2,b1,b2

    bookid_lbl=Label(win,text='Book ID', font='Helvetica 12', bg="#F7F6F8")
    bookid_lbl.place(x=230,y=227)
    e1=Entry(win, bd=0,bg="#FFFFFF",highlightthickness=0, font='Helvetica 17')
    e1.place(x=230.0,y=255.0,width=194.0,height=50.0)

    delbook_btn = tk.PhotoImage(file = "./images/delrec_fdb.png")
    b1=Button(image=delbook_btn, borderwidth=0, highlightthickness=0, command=delsingle_book)
    b1.place(x=230.0,y=410.0,width=194.0,height=71.0)

    delallbook_btn = tk.PhotoImage(file = "./images/delall.png")
    b2=Button(image=delallbook_btn, borderwidth=0, highlightthickness=0, command=delall_book)
    b2.place(x=447.0,y=410.0,width=194.0,height=71.0)

    close_bookbtn = tk.PhotoImage(file = "./images/close_btn.png")
    b3=Button(image=close_bookbtn, borderwidth=0, highlightthickness=0, command=closebooks1)
    b3.place(x=341.0,y=494.0,width=194.0,height=71.0)
    
    win.mainloop()

def delall_book():
    global win
    connectdb()
    q='SELECT * FROM Book'
    cur.execute(q)
    details=cur.fetchall()
    if len(details)!=0:
        MsgBox = messagebox.askquestion ('Delete all','This will delete all Books. Are you sure?', icon = 'warning')
        if MsgBox == 'yes':
            q='DELETE FROM Book'
            cur.execute(q)
            con.commit()
            
            messagebox.showinfo("Success", "Books Deleted!")
            closedb()
            win.destroy()
            admin1()
    else:
        messagebox.showinfo("Message","No books to Delete!")
    closedb()

def delsingle_book():
    connectdb()
    if (e1.get() == ""):
        messagebox.showinfo("Error", "Field can't be Empty!")
    else:
        bk = 'SELECT * FROM Book WHERE bookid= %s'
        s_book = (e1.get(),)
        cur.execute(bk,s_book)
        d_book =cur.fetchone()
        if(d_book == None):
            messagebox.showinfo("Message", "Book not Found!")
        else:
            MsgBox = messagebox.askquestion ('Delete','Are you sure you want to delete?', icon = 'warning')
            if MsgBox == 'yes':
                q='DELETE FROM Book WHERE bookid="%i"'
                cur.execute(q%(int(e1.get())))
                con.commit()
                
                messagebox.showinfo("Success", "Record Deleted!")
                closedb()
                win.destroy()
                admin1()
    closedb()

def delborrowed_rec():
    global win
    win.destroy()
    win=Tk()
    win.title('Delete Record')
    win.resizable(False,False)

    global screen_height, screen_width, x_cordinate, y_cordinate
    window_width = 878
    window_height = 702
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    bg_image=tk.PhotoImage(file="./images/bg_img.png")
    bg_label=tk.Label(image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image=bg_image

    global e1,e2,b1,b2,b3

    bookid_lbl=Label(win,text='Borrow Key', font='Helvetica 12', bg="#F7F6F8")
    bookid_lbl.place(x=230,y=227)

    e1=Entry(win, bd=0,bg="#FFFFFF",highlightthickness=0, font='Helvetica 17')
    e1.place(x=230.0,y=255.0,width=194.0,height=50.0)

    delbookborrowed_btn = tk.PhotoImage(file = "./images/delrec_fdb.png")
    b1=Button(image=delbookborrowed_btn, borderwidth=0, highlightthickness=0, command=delsingle_rec)
    b1.place(x=230.0,y=410.0,width=194.0,height=71.0)

    delallrec_btn = tk.PhotoImage(file = "./images/delall.png")
    b2=Button(image=delallrec_btn, borderwidth=0, highlightthickness=0, command=delall_rec)
    b2.place(x=447.0,y=410.0,width=194.0,height=71.0)

    close_bookbtn = tk.PhotoImage(file = "./images/close_btn.png")
    b3=Button(image=close_bookbtn, borderwidth=0, highlightthickness=0, command=closebooks1)
    b3.place(x=341.0,y=494.0,width=194.0,height=71.0)

    win.mainloop()

def delall_rec():
    global win
    connectdb()
    q='SELECT * FROM BookBorrow'
    cur.execute(q)
    details=cur.fetchall()
    if len(details)!=0:
        MsgBox = messagebox.askquestion ('Delete all','This will delete all records. Are you sure?', icon = 'warning')
        if MsgBox == 'yes':
            q='DELETE FROM BookBorrow'
            cur.execute(q)
            con.commit()
            
            messagebox.showinfo("Success", "Records Deleted!")
            closedb()
            win.destroy()
            admin1()
    else:
        messagebox.showinfo("Message","No records to Delete!")
    closedb()

def delsingle_rec():
    connectdb()
    if (e1.get() == ""):
        messagebox.showinfo("Error", "Field can't be Empty!")
    else:
        bk1 = 'SELECT * FROM BookBorrow WHERE borrowkey= %s'
        s_book1 = (e1.get(),)
        cur.execute(bk1,s_book1)
        d_book1 =cur.fetchone()
        if(d_book1 == None):
            messagebox.showinfo("Message", "Book not Found!")
        else:
            MsgBox = messagebox.askquestion ('Delete','Are you sure you want to delete?', icon = 'warning')
            if MsgBox == 'yes':
                q='DELETE FROM BookBorrow WHERE borrowkey="%i"'
                cur.execute(q%(int(e1.get())))
                con.commit()
                
                messagebox.showinfo("Success", "Record Deleted!")
                closedb()
                win.destroy()
                admin1()
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
        l='CREATE TABLE IF NOT EXISTS Student(name varchar(50),studid varchar(10),password varchar(30),yearlevel varchar(20),course varchar(20), PRIMARY KEY(studid))'
        b='CREATE TABLE IF NOT EXISTS Book(bookid int(15), title varchar(50),author varchar(50),genre varchar(50),status varchar(20), PRIMARY KEY(bookid))'
        i='CREATE TABLE IF NOT EXISTS BookBorrow(borrowkey int(20) AUTO_INCREMENT,stdid varchar(10),bookid varchar(15),borrowdate date,returndate date DEFAULT NULL , PRIMARY KEY (borrowkey))'
        c='ALTER TABLE BookBorrow AUTO_INCREMENT = 1001'
        
        cur.execute(l)
        cur.execute(b)
        cur.execute(i)
        cur.execute(c)
        enter=enter+1
    query='SELECT * FROM Student'
    cur.execute(query)

def closelogin():
    global window
    window.destroy()
    home()

def studhome():
    global window,b1,b2,e1,e2,con,cur,win
    window.destroy()
    window=Tk()
    window.title('Student Login')
    window.resizable(False,False)
    
    global screen_height, screen_width, x_cordinate, y_cordinate
    window_width = 878
    window_height = 702
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    bg_image=tk.PhotoImage(file="./images/bg_img.png")
    bg_label=tk.Label(image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image=bg_image 
    
    usid=Label(window,text='Student ID', font='Helvetica 12', bg="#F7F6F8")
    usid.place(x=260,y=230)
    paswrd=Label(window,text='Password',  font='Helvetica 12', bg="#F7F6F8")
    paswrd.place(x=260,y=323)

    e1=Entry(window, bd=0,bg="#FFFFFF",highlightthickness=0, font='Helvetica 17')
    e1.place(x=260.0,y=258.0,width=359.0,height=58.0)
    e2=Entry(window,bd=0,bg="#FFFFFF",highlightthickness=0, font='Helvetica 17', show = "*")
    e2.place(x=260.0,y=350.0,width=358.0,height=58.0)

    std_btn_img = tk.PhotoImage(file = "./images/student.png")
    b1=Button(image=std_btn_img, borderwidth=0, highlightthickness=0, command=loginstd)
    b1.place(x=230.0,y=494.0,width=194.0,height=71.0)
    close_studbtn = tk.PhotoImage(file = "./images/close_btn.png")
    b2=Button(image=close_studbtn, borderwidth=0, highlightthickness=0, command=closelogin)
    b2.place(x=447.0,y=494.0,width=194.0,height=71.0)
    window.mainloop()

def adminhome():
    global window,b1,b2,e1,e2,con,cur,win
    window.destroy()
    window=Tk()
    window.title('Admin Login')
    window.resizable(False,False)
    
    global screen_height, screen_width, x_cordinate, y_cordinate
    window_width = 878
    window_height = 702
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    bg_image=tk.PhotoImage(file="./images/bg_img.png")
    bg_label=tk.Label(image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image=bg_image 
    
    usid=Label(window,text='Username', font='Helvetica 12', bg="#F7F6F8")
    usid.place(x=260,y=230)
    paswrd=Label(window,text='Password',  font='Helvetica 12', bg="#F7F6F8")
    paswrd.place(x=260,y=323)

    e1=Entry(window, bd=0,bg="#FFFFFF",highlightthickness=0, font='Helvetica 17')
    e1.place(x=260.0,y=258.0,width=359.0,height=58.0)
    e1.insert(0,"admin")
    e2=Entry(window,bd=0,bg="#FFFFFF",highlightthickness=0, font='Helvetica 17', show = "*")
    e2.place(x=260.0,y=350.0,width=358.0,height=58.0)

    std_btn_img = tk.PhotoImage(file = "./images/admin.png")
    b1=Button(image=std_btn_img, borderwidth=0, highlightthickness=0, command=loginadmin)
    b1.place(x=230.0,y=494.0,width=194.0,height=71.0)
    close_adminbtn = tk.PhotoImage(file = "./images/close_btn.png")
    b2=Button(image=close_adminbtn, borderwidth=0, highlightthickness=0, command=closelogin)
    b2.place(x=447.0,y=494.0,width=194.0,height=71.0)
    window.mainloop()

def home():
    try:
        global window,b1,b2,e1,e2,con,cur,win
        window=Tk()
        window.title('Library Management System')
        window.resizable(False,False)
        
        global screen_height, screen_width, x_cordinate, y_cordinate
        window_width = 878
        window_height = 702
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        bg_image=tk.PhotoImage(file="./images/bg_img.png")
        bg_label=tk.Label(image=bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image=bg_image 
        
        selact=Label(window,text='WHO ARE YOU?', font='Helvetica 17', bg="#F7F6F8")
        selact.place(x=346,y=269)
        usid=Label(window,text='Student', font='Helvetica 17', bg="#F7F6F8")
        usid.place(x=298,y=451)
        paswrd=Label(window,text='Admin',  font='Helvetica 17', bg="#F7F6F8")
        paswrd.place(x=502,y=451)

        std_btn_img = tk.PhotoImage(file = "./images/imstud.png")
        b1=Button(image=std_btn_img, borderwidth=0, highlightthickness=0, command=studhome, bg="#F7F6F8")
        b1.place(x=298.0,y=340.0,width=100.0,height=100.0)
        admin_btn_img = tk.PhotoImage(file = "./images/imadmin.png")
        b2=Button(image=admin_btn_img, borderwidth=0, highlightthickness=0, command=adminhome, bg="#F7F6F8")
        b2.place(x=488.0,y=340.0,width=100.0,height=100.0)
        
        window.mainloop()
    except Exception:
        window.destroy()
enter = 1 
home()
