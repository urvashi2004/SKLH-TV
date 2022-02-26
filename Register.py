from tkinter import *
from tkinter import messagebox
import mysql.connector as ms

def RegisterFunc():
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
    root.title("Register Page")
    root.configure(bg = "#5E17EB")
    root.resizable(False, False)

    fullname_var = StringVar()
    username_var = StringVar()
    passwd_var = StringVar()
    conpasswd_var = StringVar()

    def submit():
        fullname = fullname_var.get()
        username = username_var.get()
        passwd = passwd_var.get()
        conpasswd = conpasswd_var.get()

        con1 = False
        con2 = False

        for i in data:
            if i[0] != username:
                con1 = True
                break
            else:
                print("Username already used")
                
        if passwd == conpasswd:
            con2 = True
        else:
            print("Passwords inserted not same")
        

        if con1 == False:
            messagebox.showerror("Username Error", "Username is already used.")
            root.destroy()
            from Choice import ChoiceFunc
            ChoiceFunc()

        elif con2 == False:
            messagebox.showerror("Password Error", "Passwords inserted are not same!")
            root.destroy()
            from Choice import ChoiceFunc
            ChoiceFunc()

        else:

            try:
                cs.execute("insert into users values ('" + username.lower() + "','" + fullname.title() + "','" + passwd + "');")
                print("Data insertion successful")
                db.commit()
                print("Data inserted in table is", fullname.title(), username.lower(), passwd)
                messagebox.showinfo("Info", "User Registered")
                root.destroy()
                from HomePageChoices import HomePageChoicesFunc
                HomePageChoicesFunc()
            
            except:
                print("Data insertion failed")
                messagebox.showerror("Error", "Could Not Register User")
                root.destroy()
                from Choice import ChoiceFunc
                ChoiceFunc()      

        fullname_var.set("")
        username_var.set("")
        passwd_var.set("")
        conpasswd_var.set("")

    head_label = Label(root, text = "Register", justify = "center", font = ("Arial", 25))
    head_label.place(x=100, y=40, width=1025, height=75)

    fullname_label = Label(root, text = "Full Name : ", font = ("Arial", 25))
    fullname_label.place(x=100, y=175, width=300, height=75)

    fullname_entry = Entry(root, textvariable = fullname_var, font = ("Arial", 25))
    fullname_entry.place(x=425, y=175, width=750, height=75)

    username_label = Label(root, text = "Username : ", font = ("Arial", 25))
    username_label.place(x=100, y=300, width=300, height=75)

    username_entry = Entry(root, textvariable = username_var, font = ("Arial", 25))
    username_entry.place(x=425, y=300, width=750, height=75)

    passwd_label = Label(root, text = "Password : ", font = ("Arial", 25))
    passwd_label.place(x=100, y=425, width=300, height=75)

    passwd_entry = Entry(root, textvariable = passwd_var, font = ("Arial", 25), show = "*")
    passwd_entry.place(x=425, y=425, width=750, height=75)

    conpasswd_label = Label(root, text = "Confirm Password : ", font = ("Arial", 25))
    conpasswd_label.place(x=100, y=550, width=300, height=75)

    conpasswd_entry = Entry(root, textvariable = conpasswd_var, font = ("Arial", 25), show = "*")
    conpasswd_entry.place(x=425, y=550, width=750, height=75)

    sub_button = Button(root, text = "Submit Entry", font = ("Arial", 25), command = lambda:submit())
    sub_button.place(x=460, y=640, width=457, height=75)

    def ClickB():
        root.destroy()
        from Choice import ChoiceFunc
        ChoiceFunc()

    button_back = Button(root, text="Back", font = ("Arial", 20), borderwidth=0, command = ClickB())
    button_back.place(x=5 ,y=5, width=100, height=60)

    root.mainloop()