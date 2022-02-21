from tkinter import *

root = Tk()

root.geometry("1280x720")
root.title("Request To Add Page")
root.configure(bg = "#5E17EB")

type_list = ["Movie","Web Series"]

title_var = StringVar()
year_var = StringVar()
type1_var = StringVar()
option_var = IntVar()

def submit():
    title = title_var.get()
    year = year_var.get()
    type1 = type1_var.get()

    print("The title of the {} is '" + title + "' made in " + year.format(type1))

    title_var.set("")
    year_var.set("")
    type1_var.set("Select An Option")

title_label = Label(root, text = "Title : ", font = ("CinzelDecorative-Bold", 25))
title_entry = Entry(root, textvariable = title_var, font = ("Arial", 25))

year_label = Label(root, text = "Year : ", font = ("Arial", 25))
year_entry = Entry(root, textvariable = year_var, font = ("Arial", 25))

type_menu = OptionMenu(root, type1_var, *type_list)
type_menu.pack()

type_label = Label(root, text = "Type : ", font = ("Arial", 25))
'''
type_entry = Entry(root, textvariable = type_var, font = ("Arial", 25))
'''

sub_button = Button(root, text = "Submit Entry", font = ("Arial", 25), command = submit)
sub_button.pack()

title_label.place(x=125, y=125, width=200, height=75)
title_entry.place(x=400, y=125, width=750, height=75)

year_label.place(x=125, y=285, width=200, height=75)
year_entry.place(x=400, y=285, width=750, height=75)

type_label.place(x=125, y=445, width=200, height=75)
type_menu.place(x=400, y=445, width=750, height=75)

sub_button.place(x=460, y=560, width=457, height=75)

root.mainloop()

'''
https://www.geeksforgeeks.org/tkinter-optionmenu-widget/

root.bind('<Return>',selecttest1)
'''
