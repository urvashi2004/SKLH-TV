from tkinter import *

def ChoiceFunc():
    root = Tk()

    root.geometry("1280x720")
    root.title("Choice Page")
    root.configure(bg = "#5E17EB")
    root.resizable(False, False)

    def ClickReg():
        root.destroy()
        from Register import RegisterFunc
        RegisterFunc()

    def ClickLog():
        root.destroy()
        from Login import LoginFunc
        LoginFunc()

    type_label = Label(root, text = "Select An Option To Enter", font = ("Arial", 25))
    type_label.place(x=125, y=40, width=1025, height=75)

    register_but = Button(root, text = "Register", font = ("Arial", 25), command = lambda:ClickReg())
    register_but.place(x=180, y=180, width=400, height=400)

    sign_but = Button(root, text = "Login", font = ("Arial", 25), command = lambda:ClickLog())
    sign_but.place(x=620, y=180, width=400, height=400)

    button_back = Button(root, text="QUIT", font = ("Arial", 20), borderwidth=0, command=lambda:root.destroy())
    button_back.place(x=5 ,y=5, width=100, height=60)

    root.mainloop()