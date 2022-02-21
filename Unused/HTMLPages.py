#logo page

"""def page1():
    with open("ALogo Page.html","w") as file1:
        code1 = '''
        <html lang="en">
            <head>
                <title>
                    Logo Page
                </title>
                <style>
                    img{
                        display:block;
                        margin-left: auto;
                        margin-right: auto;
                    }
                </style>
            </head>
            <body style="background-color: #5E17EB;">
                <img src="SKLH TV Logo.png"
                alt="OTT Logo"
                class="center"
                width="655"
                height="655">
            </body>
        </html>
        '''
        file1.write(code1)

#login register choice page

def page2():
    with open("BChoice Page.html") as file2:
        code2 = '''
        <html lang="en">
            <head>
                <title>
                    Login Page
                </title>
                <style>
                    .wrapper{
                        text-align: center;
                        margin-top: 6%;
                    }
                    .button{
                        margin: 3%;
                        border-color: white;
                        border-width: 10px;
                    }
                    .button:hover{
                        border-color:#01A3E3;
                    }
                </style>
            </head>
            <body style="background-image: repeating-radial-gradient(circle,#eacda3,#d6ae7b);">
                <div class="wrapper">
                    <button class="button">
                        <a href="01 Open login page.py"> </a>
                        <img src="Login.jpg"
                        alt="Login Button"
                        width="400"
                        height="400">
                    </button>
                    <button class="button">
                        <a href="01 Open login page.py"> </a>
                        <img src="Register.jpg"
                        alt="Register Button"
                        width="400"
                        height="400">
                    </button>
                </div>
            </body>
        </html>
        '''
        file2.write(code2)
"""

def add(a,b):
    return a+b
