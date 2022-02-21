from tkinter import *

project = Tk()
img = ImageTk.PhotoImage(Image.open(r"D:\OTT Project\SKLH TV Logo"))
panel = Label(project, image = img)
width = project.winfo_screenwidth()
height= project.winfo_screenheight()
project.geometry("%dx%d" % (width, height))
project.title("SKLH TV")
    
'''start = Label(project,text="Please Select An Option")
start.pack()

button1 = Button(
    project,
    text="Already a user",
    bg="light blue",
    activebackground="white",
    width=40,
    height=10)
button1.pack()
button2 = Button(
    project,
    text="New user",
    bg="light blue",
    activebackground="white",
    width=40,
    height=10)
button2.pack()'''

project.mainloop()
