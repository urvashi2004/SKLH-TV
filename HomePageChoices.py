from tkinter import *
from RequestPage import *
from YourContentPage import *

def HomePageChoicesFunc():
    root = Tk()

    root.geometry("1280x720")
    root.title("HOME PAGE")
    root.resizable(False, False)
    root.config(bg = "#5E17EB")

    label_heading = Label(root, text = "SKLH TV", justify = "center", font = ("Arial", 25))
    label_heading.place(x=125, y=40, width=1025, height=75)

    def ClickExp():
        root.destroy()

    explore_but = Button(root, text = "Explore", font = ("Arial", 25), command=lambda:ClickExp())
    explore_but.place(x=110, y=200, width=400, height=200)

    def ClickYour():
        root.destroy()
        YourContentPageFunc()

    your_but = Button(root, text = "Your Content", font = ("Arial", 25), command=lambda:ClickYour())
    your_but.place(x=800, y=200, width=400, height=200)

    def ClickRecs():
        root.destroy()

    recs_but = Button(root, text = "Reccomendations", font = ("Arial", 25), command=lambda:ClickRecs())
    recs_but.place(x=110, y=450, width=400, height=200)

    def ClickReq():
        root.destroy()
        RequestPageFunc()

    req_but = Button(root, text = "Request To Add", font = ("Arial", 25), command=lambda:ClickReq())
    req_but.place(x=800, y=450, width=400, height=200)

    def Click():
        from Choice import ChoiceFunc
        root.destroy()
        ChoiceFunc()

    logout = Button(root, text="LOGOUT", font = ("Arial", 20), borderwidth=0, command=lambda:Click())
    logout.place(x=5 ,y=5, width=120, height=60)

    root.mainloop()