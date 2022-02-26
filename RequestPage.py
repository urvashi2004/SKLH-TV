from tkinter import *
from tkinter import messagebox
import mysql.connector as ms

def RequestPageFunc():
    db = ms.connect(host="localhost",user="root",passwd="urvashi22")

    if db.is_connected():
        print("Connection Established")
    else:
        print("Connection Not Connected")

    cs = db.cursor()
    cs.execute("use sklh_tv;")

    root = Tk()

    root.geometry("1280x720")
    root.title("Request To Add Page")
    root.configure(bg = "#5E17EB")
    root.resizable(False, False)

    title_var = StringVar()
    year_var = StringVar()
    type1_var = StringVar()

    def submit():
        title = title_var.get()
        year = year_var.get()
        type1 = type1_var.get()

        messagebox.showinfo("Request Sent", title.title() + " made in " + year + " is requested successfully.")

        cs.execute("insert into request values ('" + title.title() + "','" + year + "','" + type1 + "');")

        title_var.set("")
        year_var.set("")
        type1_var.set("")

        root.destroy()
        from HomePageChoices import HomePageChoicesFunc
        HomePageChoicesFunc()

    head_label = Label(root, text = "Request To Add", justify = "center", font = ("Arial", 25))
    head_label.place(x=125, y=40, width=1025, height=75)

    title_label = Label(root, text = "Title : ", font = ("CinzelDecorative-Bold", 25))
    title_label.place(x=125, y=175, width=200, height=75)

    title_entry = Entry(root, textvariable = title_var, font = ("Arial", 25))
    title_entry.place(x=400, y=175, width=750, height=75)

    year_label = Label(root, text = "Year : ", font = ("Arial", 25))
    year_label.place(x=125, y=335, width=200, height=75)

    year_entry = Entry(root, textvariable = year_var, font = ("Arial", 25))
    year_entry.place(x=400, y=335, width=750, height=75)

    type_menu = OptionMenu(root, type1_var, "Movie", "Web Series")
    type_menu.place(x=400, y=475, width=750, height=75)

    type_label = Label(root, text = "Type : ", font = ("Arial", 25))
    type_label.place(x=125, y=475, width=200, height=75)

    sub_button = Button(root, text = "Submit Entry", font = ("Arial", 25), command = lambda:submit())
    sub_button.place(x=460, y=590, width=457, height=75)

    def Click():
        root.destroy()
        from HomePageChoices import HomePageChoicesFunc
        HomePageChoicesFunc()

    button_back = Button(root, text="BACK", font = ("Arial", 20), borderwidth=0, command = lambda:Click())
    button_back.place(x=5 ,y=5, width=100, height=60)

    root.mainloop()
