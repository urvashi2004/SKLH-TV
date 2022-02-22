from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tkinter
import importlib
import mysql.connector as mysql



def signupwindowaction():
    signupwindow = Tk()
    signupwindow.title("PrepMasterBETA")
    signupwindow.geometry("1280x720")   
    signupwindow.config(bg="#5E17EB")
    signupwindow.resizable(False, False)

    def accountdone1():
        mycon = mysql.connect(host='localhost', user='root', passwd='comp123', database='sklh_tv')
        mycursor = mycon.cursor()
        try:
            mycursor.execute('insert into sign_in_student values("%s","%s","%s","%s","%s","%s");'%(f_name.get(),user_name.get(),passwd_key.get(),conpas_db.get()))
            mycon.commit()
            mycursor.execute('insert into account_student values("%s","%s");'%(user_name.get(),passwd_key.get()))
            mycon.commit()
            messagebox.showinfo("SHOWINFO", "ACCOUNT CREATED!")
            signupwindow.destroy()      
        except:
            messagebox.showerror('SHOWERROR','RECORD INSERTION UNSUCCESSFUL!')

    def accountdone2(e):
        mycon = mysql.connect(host='localhost', user='root', passwd='comp123', database='sklh_tv')
        mycursor = mycon.cursor()
        try:
            mycursor.execute('insert into sign_in_user values("%s","%s","%s","%s","%s","%s");'%(f_name.get(),user_name.get(),passwd_key.get(),conpas_db.get()))
            mycon.commit()
            mycursor.execute('insert into account_user values("%s","%s");'%(user_name.get(),passwd_key.get()))
            mycon.commit()
            messagebox.showinfo("SHOWINFO", "ACCOUNT CREATED!")
            signupwindow.destroy()
            #from MasterPrepBETA import loginaction
            #loginaction()        
        except:
            messagebox.showerror('SHOWERROR','RECORD INSERTION UNSUCCESSFUL!')

    f_name = StringVar()
    fullname = Entry(signupwindow,
                textvariable=f_name,
                justify="center",
                bg="#0c5dc0",
                borderwidth=0,
                font="calibri 20",).place(x=799, y=50, width=435, height=55)

    user_name = StringVar()
    username = Entry(signupwindow,
                textvariable=user_name,
                justify="center",
                bg="#0c5dc0",
                borderwidth=0,
                font="calibri 20",).place(x=799, y=153, width=435, height=55)

    passwd_key = StringVar()
    passkey   = Entry(signupwindow,
                textvariable=passwd_key,
                justify="center",
                bg="#0c5dc0",
                borderwidth=0,
                show="*",
                font="calibri 20",).place(x=799, y=254, width=435, height=55)

   
    conpas_db = StringVar()
    confirm_password    = Entry(signupwindow,
                textvariable=conpas_db,
                justify="center",
                borderwidth=0,
                bg="#0c5dc0",
                font="calibri 20",).place(x=799, y=455, width=435, height=55)

    email_db = StringVar()
    emailad   = Entry(signupwindow,
                textvariable=email_db,
                justify="center",
                borderwidth=0,
                bg="#0c5dc0",
                font="calibri 20",).place(x=799, y=551, width=435, height=55)

    Display = Button(signupwindow, 
	    			text ="SIGN UP",
		    		font ="BurbankBigCondensed-Bold 25",
			    	bg="#57595c",
                    borderwidth=0,
                    fg='white',
				    command = lambda:accountdone1()).place(x=920, y=631, width=200, height=53)
    signupwindow.bind('<Return>',accountdone2)



    mainloop()
signupwindowaction()
    