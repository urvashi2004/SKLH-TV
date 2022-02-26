from tkinter import *

root = Tk()

root.geometry("1280x720")
root.title("Logo Page")
root.resizable(False, False)
root.config(bg = "#5E17EB")

photo = PhotoImage(file = "SKLH TV Logo.png")

photoimage = photo.subsample(1)

def Click():
    root.destroy()
    from Choice import ChoiceFunc
    ChoiceFunc()

Logo_But = Button(root, image = photoimage, command = lambda:Click())
Logo_But.place(x=280, height=720, width=720)

root.mainloop()