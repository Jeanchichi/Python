import pyqrcode
from tkinter import *
import tkinter.ttk as ttk
from ttkthemes import ThemedTk
from PIL import Image,ImageTk

win = ThemedTk(theme="equilux")
win.title("QR Code Generator")
win.config(background="#181818")

def Generate():
    text = entryl.get()
    qr = pyqrcode.create(text)
    file_name = "my qrcode"
    save_path = r'C:\Users\Jeceey\Downloads\ '
    name = save_path+file_name+'.png'
    qr.png(name, scale=10)
    image = Image.open(name)
    image = image.resize((400, 400), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    win.imagelabel.config(image=image)
    win.imagelabel = image

text = ttk.Label(win, text= "Enter text or link :")
text.grid(row=0, column=0, padx=0, pady=3)

entryl = ttk.Entry(win, width=40)
entryl.grid(row=0, column=1, padx=3, pady=3)

button = ttk.Button(win, text="Generate", command=Generate)
button.grid(row=0, column=2, padx=3, pady=3)

show_qr = ttk.Label(win, text="QR Code :")
show_qr.grid(row=1, column=0, padx=3, pady=3)

win.imagelabel = ttk.Label(win, background='#181818')
win.imagelabel.grid(row=2, column=0, padx=3, pady=3, columnspan=3)

win.mainloop()