import tkinter as tk
root = tk.Tk()
root.geometry('1280x720')
root.title('GENRE PAGE')
root.resizable(False, False)
root.config(bg='#0073FF')
root.eval('tk::PlaceWindow . center')
label_heading = tk.Label(root,
                    text='SELECT GENRE',
                    justify='center',
                    font='BurbankBigCondensed-Bold 70',
                    bg='#0073FF',
                    fg='white',
                    borderwidth=0).place(x=350, y=70, width=500, height=100)

button_1 = tk.Button(root,
                text='Action',
                font='CinzelDecorative-Bold 40',
                bg='#FE7D05',
                fg='white').place(x=100, y=220, width=263, height=200)

button_2 = tk.Button(root,
                text='Comedy',
                font='CinzelDecorative-Bold 40',
                bg='#F30C0D',
                fg='white').place(x=470, y=220, width=263, height=200)

button_3 = tk.Button(root,
                text='Horror',
                font='BurbankBigCondensed-Bold 40',
                bg='#7FD10B',
                fg='white').place(x=850, y=220, width=263, height=200)

button_4 = tk.Button(root,
                text='Romance',
                font='BurbankBigCondensed-Bold 40',
                bg='#FFCA34',
                fg='white').place(x=100, y=520, width=263, height=200)

button_5 = tk.Button(root,
                text='Fantasy',
                font='BurbankBigCondensed-Bold 40',
                bg='#F00272',
                fg='white').place(x=470, y=520, width=263, height=200)

button_6 = tk.Button(root,
                text='Crime',
                font='BurbankBigCondensed-Bold 40',
                bg='#F00272',
                fg='white').place(x=850, y=520, width=263, height=200)

button_back = tk.Button(root,
                text='<BACK>',
                font='BurbankBigCondensed-Bold 35',
                bg='#0072ff',
                fg='white',
                borderwidth=0).place(x=5,y=15, width=150, height=70)

root.mainloop()