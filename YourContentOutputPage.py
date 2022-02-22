from tkinter import *
from  tkinter import ttk
import mysql.connector as ms

db = ms.connect(host="localhost", user="root", passwd="urvashi22")

if db.is_connected():
    print("Connection Established")
else:
    print("Connection Not Connected")

cs = db.cursor()

cs.execute("use sklh_tv;")
cs.execute("select * from content;")

data = cs.fetchall()

root  = Tk()

root.geometry("1280x720")
root.title("Your Profile Page")
root.configure(bg = "#5E17EB")
root.resizable(False, False)

type_label = Label(root, text = "Your Want To Watch List", font = ("Arial", 25))
type_label.place(x=125, y=40, width=1025, height=75)

game_frame = Frame(root)
game_frame.pack()
game_frame.place(x=125, y=150, width=1025, height=500)

#scrollbar
game_scroll = Scrollbar(game_frame)
game_scroll.pack(side=RIGHT, fill=Y)

my_game = ttk.Treeview(game_frame, yscrollcommand=game_scroll.set)
my_game.pack()
my_game.place(x=125, y=150, width=1060, height=500)

game_scroll.config(command=my_game.yview)

#define our column
my_game['columns'] = ('col_id', 'col_name', 'col_type', 'col_year', 'col_region','col_genre','col_summary')

# format our column
my_game.column("#0", width=0,  stretch=NO)
my_game.column("col_id",anchor=CENTER, width=50)
my_game.column("col_name",anchor=CENTER,width=200)
my_game.column("col_type",anchor=CENTER,width=60)
my_game.column("col_year",anchor=CENTER,width=50)
my_game.column("col_region",anchor=CENTER,width=100)
my_game.column("col_genre",anchor=CENTER,width=100)
my_game.column("col_summary",anchor=CENTER,width=445)

#Create Headings 
my_game.heading("#0",text="",anchor=CENTER)
my_game.heading("col_id",text="ID",anchor=CENTER)
my_game.heading("col_name",text="NAME",anchor=CENTER)
my_game.heading("col_type",text="TYPE",anchor=CENTER)
my_game.heading("col_year",text="YEAR",anchor=CENTER)
my_game.heading("col_region",text="REGION",anchor=CENTER)
my_game.heading("col_genre",text="GENRE",anchor=CENTER)
my_game.heading("col_summary",text="SUMMARY",anchor=CENTER)

#add data 
for i in range(len(data)):
    for j in data:
        my_game.insert(parent='', index='end', iid=i, text='', values=j)
'''my_game.insert(parent='',index='end',iid=0,text='',
values=('M101','Your Name','Movie',2016,'Japan','Fantasy','Two teenagers share a profound, magical connection upon discovering they are swapping bodies. Things manage to become even more complicated when the boy and girl decide to meet in person.'))
my_game.insert(parent='',index='end',iid=1,text='',
values=('2','Ranger','102','Wisconsin', 'Green Bay'))
my_game.insert(parent='',index='end',iid=2,text='',
values=('3','Deamon','103', 'California', 'Placentia'))
my_game.insert(parent='',index='end',iid=3,text='',
values=('4','Dragon','104','New York' , 'White Plains'))
my_game.insert(parent='',index='end',iid=4,text='',
values=('5','CrissCross','105','California', 'San Diego'))
my_game.insert(parent='',index='end',iid=5,text='',
values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
my_game.insert(parent='',index='end',iid=6,text='',
values=('7','RayRizzo','107','Colorado' , 'Denver'))
my_game.insert(parent='',index='end',iid=7,text='',
values=('8','Byun','108','Pennsylvania' , 'ORVISTON'))
my_game.insert(parent='',index='end',iid=8,text='',
values=('9','Trink','109','Ohio' , 'Cleveland'))
my_game.insert(parent='',index='end',iid=9,text='',
values=('10','Twitch','110','Georgia' , 'Duluth'))
my_game.insert(parent='',index='end',iid=10,text='',
values=('11','Animus','111', 'Connecticut' , 'Hartford'))'''
my_game.pack()

button_back = Button(root, text="BACK", font = ("Arial", 20), borderwidth=0)
button_back.place(x=5 ,y=5, width=100, height=60)

root.mainloop()
