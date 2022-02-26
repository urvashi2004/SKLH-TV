from ast import Add
from tkinter import *
from math import *
import mysql.connector as ms

db = ms.connect(host="localhost",user="root",passwd="urvashi22")

if db.is_connected():
    print("Connection Established")
else:
    print("Connection Not Connected")

cs = db.cursor()

cs.execute("use sklh_tv;")
cs.execute("select * from content;")
data = cs.fetchall()

root = Tk()

root.geometry("1280x720")
root.title("Something Page")
root.configure(bg = "#5E17EB")
root.resizable(False, False)

for k in range(1,ceil(len(data)/21),21):
    type_label = Label(root, text = ("Page (" + str(k) + "/" + str(ceil((len(data)/21))) + ")"), font = ("Arial", 25))
    type_label.place(x=1070, y=5, width=200, height=60)

counter = -1
for i in range(len(data)):
    print(i)

    counter += 1
    
    def button(name):

        def Click():
            root.destroy()
            from AddToProfilePage import AddToProfilePageFunc
            AddToProfilePageFunc()

        name = Button(root, text = name, font = ("Arial", 25), command = lambda:Click())
        name.place(x=xp, y=yp, width=350, height=50)
    
    for xp in range(100,1100,370):
        for yp in range(100,650,70):
            button(data[counter][1])

            print("Counter is ",counter)

'''
    def next():
        i+18

    def previous():
        i-18

    button_back = Button(root, text="BACK", font = ("Arial", 20), borderwidth=0)
    button_back.place(x=5 ,y=5, width=100, height=60)

    less_display = Button(root,text='<', font = ("Arial", 20), borderwidth=0, command = lambda:next)
    less_display.place(x=5, y=332, width=50, height=100)
    
    great_display = Button(root,text='>', font = ("Arial", 20), borderwidth=0, command = lambda:previous)
    great_display.place(x=1210, y=332, width=50, height=100)
    '''

root.mainloop()