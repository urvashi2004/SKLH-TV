from tkinter import *

root = Tk()

root.geometry("1280x720")
root.title("GENRE PAGE")
root.resizable(False, False)
root.config(bg = "#5E17EB")

label_heading = Label(root, text = "SELECT GENRE", justify = "center", font = ("Arial", 25))
label_heading.place(x=125, y=40, width=1025, height=75)

button_1 = Button(root, text = "Action", font='CinzelDecorative-Bold 40')
button_1.place(x=100, y=220, width=263, height=200)

button_2 = Button(root, text = "Comedy", font='CinzelDecorative-Bold 40')
button_2.place(x=470, y=220, width=263, height=200)

button_3 = Button(root, text = "Horror", font='CinzelDecorative-Bold 40')
button_3.place(x=850, y=220, width=263, height=200)

button_4 = Button(root, text = "Romance", font='CinzelDecorative-Bold 40')
button_4.place(x=100, y=480, width=263, height=200)

button_5 = Button(root, text = "Fantasy", font='CinzelDecorative-Bold 40')
button_5.place(x=470, y=480, width=263, height=200)

button_6 = Button(root, text = "Romance", font='CinzelDecorative-Bold 40')
button_6.place(x=850, y=480, width=263, height=200)

root.mainloop()
