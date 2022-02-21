import time
import mysql.connector as ms

db = ms.connect(host="localhost",user="root",passwd="urvashi22")
#need to change this for respective devices

if db.is_connected():
    print("Connection Established")
else:
    print("Connection Not Connected")

cursor = db.cursor()
cursor.execute("use sklh_tv")




print("                                                  ")
print("          ______________________________          ")
print("         |                                        ")
print("         |     ____                               ")
print("         |    |____                               ")
print("         |     ____|                              ")
print("         |                                        ")
print("                                                  ")
print("                                                  ")
print("                                                  ")
print("                                                  ")

time.sleep(3)

def login():
    username = input("Enter your username : ")
    password = input("Enter your password : ")
    while True:
        if username == user and password == userpass:
            print("Welcome",username)
            False
        else:
            print("User not found!")

def register():
    username = input("Enter your username : ")
    password = input("Enter your password : ")
    password2 = input("Confirm your password : ")
    print("Welcome",username)

print("\t"*4,"Select one of the two below :")
print("\t"*4,"      1. Login")
print("\t"*4,"    2. Register")

#choice to login or register
while True:
    ch = input("Please enter your choice (in num) : ")
    if ch=="1":
        login()
        False
    elif ch=="2":
        register()
        False
    else:
        print("Enter a valid choice.")

def content():
    print("Items in your watchlist : ")
    print("Items you are done with : ")
    print("Items currecntly watching : ")

def reccomend():
    print("Here are a few recommendations : ")
    
def search():
    name = input("Enter keywords : ")

def request():
    name = input("Enter the name of media : ")
    typec = input("Enter the type of media : ")
    year = input("Enter the year of release : ")

def change():
    while True:
        ch = input("Do you really want to change users 'Y'/'N' : ")
        if ch.lower() in "yes":
            login()
            False
        elif ch.lower() in "no":
            homepage()
            False
        else:
            print("Enter a valid choice!")

def homepage():
    print("           MENU           ")
    print("     1. Your Content      ")
    print("   2. Recommendations     ")
    print("       3. Search          ")
    print("     4. Request To Add    ")
    print("       5. Change User     ")
    print("         6. Logout        ")
    ch = input("Enter your choice : ")
    while True:
        if ch=="1":
            content()
            False
        elif ch=="2":
            recommend()
            False
        elif ch=="3":
            search()
            False
        elif ch=="4":
            request()
            False
        elif ch=="5":
            change()
            False
        else:
            print("Enter a valid choice!")
