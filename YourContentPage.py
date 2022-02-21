'''from tkinter import * 

root = Tk()

root.geometry("1280x720")
root.title("Your Profile Page")
root.configure(bg = "#5E17EB")

type_label = Label(root, text = "Your Profile", font = ("Arial", 25))

want_but = Button(root, text = "Want To Watch", font = ("Arial", 25))
watch_but = Button(root, text = "Watching", font = ("Arial", 25))
done_but = Button(root, text = "Already Watched", font = ("Arial", 25))

type_label.place(x=150, y=200, width=657, height=75)
want_but.place(x=150, y=400, width=457, height=200)
watch_but.place(x=650, y=400, width=457, height=200)
done_but.place(x=290, y=600, width=457, height=200)

root.mainloop()'''

# Python program to create a table

from tkinter import *

class Table:
	
	def __init__(self,root):
		
		# code for creating table
		for i in range(total_rows):
			for j in range(total_columns):
				
				self.e = Entry(root, width=20, fg='blue',
							font=('Arial',16,'bold'))
				
				self.e.grid(row=i, column=j)
				self.e.insert(END, lst[i][j])

# take the data
lst = [(1,'Raj','Mumbai',19),
	(2,'Aaryan','Pune',18),
	(3,'Vaishnavi','Mumbai',20),
	(4,'Rachna','Mumbai',21),
	(5,'Shubham','Delhi',21)]

# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])

# create root window
root = Tk()

root.geometry("1280x720")
root.title("Your Profile Page")
root.configure(bg = "#5E17EB")

t = Table(root)
root.mainloop()
