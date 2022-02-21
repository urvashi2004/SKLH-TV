from tkinter import *
from  tkinter import ttk

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

my_game = ttk.Treeview(game_frame,yscrollcommand=game_scroll.set)
my_game.pack()

game_scroll.config(command=my_game.yview)

#define our column
 
my_game['columns'] = ('player_id', 'player_name', 'player_Rank', 'player_states', 'player_city')

# format our column
my_game.column("#0", width=0,  stretch=NO)
my_game.column("player_id",anchor=CENTER, width=80)
my_game.column("player_name",anchor=CENTER,width=80)
my_game.column("player_Rank",anchor=CENTER,width=80)
my_game.column("player_states",anchor=CENTER,width=80)
my_game.column("player_city",anchor=CENTER,width=80)

#Create Headings 
my_game.heading("#0",text="",anchor=CENTER)
my_game.heading("player_id",text="ID",anchor=CENTER)
my_game.heading("player_name",text="NAME",anchor=CENTER)
my_game.heading("player_Rank",text="YEAR",anchor=CENTER)
my_game.heading("player_states",text="TYPE",anchor=CENTER)
my_game.heading("player_city",text="SUMMARY",anchor=CENTER)

#add data 
my_game.insert(parent='',index='end',iid=0,text='',
values=('1','Ninja','101','Oklahoma', 'Moore'))
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
values=('11','Animus','111', 'Connecticut' , 'Hartford'))
my_game.pack()

root.mainloop()
