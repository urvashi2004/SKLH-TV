from tkinter import *
from tkinter import messagebox
import mysql.connector as ms
from HomePageChoices import HomePageChoicesFunc
from Choice import ChoiceFunc

def LoginFunc():
    db = ms.connect(host="localhost",user="root",passwd="urvashi22")

    if db.is_connected():
        print("Connection Established")
    else:
        print("Connection Not Connected")

    cs = db.cursor()

    cs.execute("use sklh_tv;")
    cs.execute("select * from users;")

    data = cs.fetchall()

    root = Tk()

    root.geometry("1280x720")
    root.title("Login Page")
    root.configure(bg = "#5E17EB")
    root.resizable(False, False)

    username_var = StringVar()
    passwd_var = StringVar()

    def submit():
        username = username_var.get()
        passwd = passwd_var.get()

        username_var.set("")
        passwd_var.set("")

        con1 = False
        con2 = False

        for i in data:
            if i[0] == username:
                con1 = True
                if i[2] == passwd:
                    con2 = True
                else:
                    print("Password does not match")
                break
            else:
                print("Username does not exists")

        if con1 == False:
            messagebox.showerror("Username Error", "Username not in database")
            root.destroy()
            ChoiceFunc()
        elif con2 == False:
            messagebox.showerror("Password Error", "Passwords does not match")
            root.destroy()
            ChoiceFunc()
        elif (con1 == True) and (con2 == True):
            root.destroy()
            HomePageChoicesFunc()

    head_label = Label(root, text = "Login", justify = "center", font = ("Arial", 25))
    head_label.place(x=100, y=40, width=1025, height=75)

    username_label = Label(root, text = "Username : ", font = ("Arial", 25))
    username_label.place(x=100, y=300, width=300, height=75)

    username_entry = Entry(root, textvariable = username_var, font = ("Arial", 25))
    username_entry.place(x=425, y=300, width=750, height=75)

    passwd_label = Label(root, text = "Password : ", font = ("Arial", 25))
    passwd_label.place(x=100, y=425, width=300, height=75)

    passwd_entry = Entry(root, textvariable = passwd_var, font = ("Arial", 25), show = "*")
    passwd_entry.place(x=425, y=425, width=750, height=75)

    sub_button = Button(root, text = "Submit Entry", font = ("Arial", 25), command = lambda:submit())
    sub_button.place(x=460, y=640, width=457, height=75)

    def Click():
        root.destroy()
        ChoiceFunc()

    button_back = Button(root, text="Back", font = ("Arial", 20), borderwidth=0, command=lambda:Click())
    button_back.place(x=5 ,y=5, width=100, height=60)

    root.mainloop()