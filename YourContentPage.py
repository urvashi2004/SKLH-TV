from tkinter import * 

def YourContentPageFunc():
    root = Tk()

    root.geometry("1280x720")
    root.title("Your Profile Page")
    root.configure(bg = "#5E17EB")
    root.resizable(False, False)

    type_label = Label(root, text = "Your Profile", font = ("Arial", 25))
    type_label.place(x=125, y=40, width=1025, height=75)

    want_but = Button(root, text = "Want To Watch", font = ("Arial", 25))
    want_but.place(x=100, y=220, width=500, height=200)

    watch_but = Button(root, text = "Watching", font = ("Arial", 25))
    watch_but.place(x=700, y=220, width=500, height=200)

    done_but = Button(root, text = "Already Watched", font = ("Arial", 25))
    done_but.place(x=400, y=480, width=500, height=200)

    button_back = Button(root, text="BACK", font = ("Arial", 20), borderwidth=0)
    button_back.place(x=5 ,y=5, width=100, height=60)

    root.mainloop()
