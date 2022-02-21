import mysql.connector as ms

db = ms.connect(host="localhost",user="root",passwd="urvashi22")
#need to change this for respective devices

if db.is_connected():
    print("Connection Established")
else:
    print("Connection Not Connected")

cs = db.cursor()

#uncomment the region below when using for the first time

#cs.execute("create database sklh_tv;")
cs.execute("use sklh_tv;")
#cs.execute('''create table users (Username varchar(20) primary key not null, Name varchar(40) not null, Password varchar(40) not null);''')
#cs.execute('''create table content(ID char(4) primary key not null, Name varchar(40) not null, Type varchar(10) not null,Year int not null,Director varchar(40),Male_Lead varchar(40),Female_Lead varchar(40),Summary varchar(2000));''')
#cursor.execute('''insert into content (ID,Name,Type,Year,Summary) values ("M152","Your Name","Movie",2016,"Two teenagers share a profound, magical connection upon discovering they are swapping bodies. Things manage to become even more complicated when the boy and girl decide to meet in person."''')
#cs.execute("desc users;")
#cs.execute("drop database sklh_tv;")
'''data = cs.fetchall()
print(data)

cs.execute("desc content;")
data = cs.fetchall()
print(data)'''
