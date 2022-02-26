from tkinter import *

root = Tk()

root.geometry("1280x720")
root.title("Genre Page")
root.resizable(False, False)
root.config(bg = "#5E17EB")

label_heading = Label(root, text = "SELECT GENRE", justify = "center", font = ("Arial", 25))
label_heading.place(x=125, y=40, width=1025, height=75)

button_1 = Button(root, text = "Action", font = ("Arial", 25))
button_1.place(x=110, y=200, width=263, height=150)

button_2 = Button(root, text = "Comedy", font = ("Arial", 25))
button_2.place(x=480, y=200, width=263, height=150)

button_3 = Button(root, text = "Horror", font = ("Arial", 25))
button_3.place(x=860, y=200, width=263, height=150)

button_4 = Button(root, text = "Romance", font = ("Arial", 25))
button_4.place(x=110, y=380, width=263, height=150)

button_5 = Button(root, text = "Fantasy", font = ("Arial", 25))
button_5.place(x=480, y=380, width=263, height=150)

button_6 = Button(root, text = "Romance", font = ("Arial", 25))
button_6.place(x=860, y=380, width=263, height=150)

button_back = Button(root, text="BACK", font = ("Arial", 20), borderwidth=0)
button_back.place(x=5 ,y=5, width=100, height=60)

button_ok = Button(root, text="OK", font = ("Arial", 20), borderwidth=0)
button_ok.place(x=125, y=600, width=1025, height=75)

root.mainloop()
