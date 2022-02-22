'''import tkinter as tk
root=tk.Tk()
root.title('SKLH TV')
root.geometry('1280x720')
root.resizable(True,True)
bg=tk.PhotoImage(file="sklhtvlogo.png")
root.eval('tk::PlaceWindow . center')
root.config(bg='#5E17EB')
label1 = tk.Label( root, image = bg)
label1.place(x = 400, y = 150)
root.mainloop()'''

from tkinter import *
from PIL import ImageTk

from singup import signup
canvas = Canvas(width=1280, height=720, bg='#5E17EB')
canvas.pack(expand=YES, fill=BOTH)

image1 = ImageTk.PhotoImage(file="sklhtvlogo.png")
canvas.create_image(400, 150, image=image1, anchor=NW)
i1=ImageTk.PhotoImage(file="register.png", size=400)
i2=ImageTk.PhotoImage(file='login.png', size=400)
def signupaction():
    canvas.destroy()
    from singup import signup

signupbutton= Button(canvas,
                     text='Signup',
                     image=i1,
                     compound= TOP,
                     borderwidth=0,command=lambda:signupaction()).place(x=300, y=200, width=100, height= 100)

loginbutton= Button(canvas,
                   text='login',
                   image=i2,
                   compound = TOP,
                   borderwidth=0).place(x=600, y=200, width= 500, height= 200)






mainloop() 