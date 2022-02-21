'''

#01

import codecs

file = codecs.open(r"D:\OTT Project\SKLH TV\1 Logo Page.html")
print(file.read())



#02

import webbrowser as wb

page = r"C:\Users\van76\OneDrive\Desktop\FLASK TUTORIAL\SKLH TV\1 Logo Page.html"
wb.open_new_tab(page)



#03

import webbrowser as wb
import os

file = open(r"C:\Users\van76\OneDrive\Desktop\FLASK TUTORIAL\SKLH TV\1 Logo Page.html","w")

html_template = r"""
<html>
    <head>
        <style>
            img{
                display:block;
                margin-left: auto;
                margin-right: auto;
            }
            </style>
    </head>
    <body style="background-color: #5E17EB;">
        <img src="D:\OTT Project\SKLH TV Logo.png"
        alt="OTT Logo"
        class="center"
        width="655"
        height="655">
    </body>
</html>
"""

file.write(html_template)
wb.open_new_tab(file)
file.close()

#newfile = r"file:///"+os.getcwd()+"/"+r"C:\Users\van76\OneDrive\Desktop\FLASK TUTORIAL\SKLH TV\1 Logo Page.html"



#04
import os

#page = r"C:\Users\van76\OneDrive\Desktop\FLASK TUTORIAL\SKLH TV\1 Logo Page.html"

os.system("start"+ r"C:\Users\van76\OneDrive\Desktop\FLASK TUTORIAL\SKLH TV\1 Logo Page.html")
'''


