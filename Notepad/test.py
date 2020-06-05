from tkinter import *
from tkinter import ttk
from library import win
import os
from tkinter.filedialog import askopenfile,asksaveasfilename

win = Tk()
win.title("Notepad")
win.geometry("720x480")
win.minsize(720, 480)
win.config(background='#272C35')

def open_file():
    blank.delete("1.0", END)
    file = askopenfile(mode='r', filetypes=[('Text files', '*.txt')])
    if file is not None:
        text = file.read()
        blank.insert("1.0", text)

def save_file():
    notepad_text = blank.get("1.0", "end-1c")
    file = asksaveasfilename(title="Save", filetypes=[('Text files', '*.txt')])
    with open(file, "w") as data :
        data.write(notepad_text)

menubar = Menu(win)
win.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_command(label="Save as", command=save_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=win.destroy)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Delete")

displaymenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Display", menu=displaymenu)
displaymenu.add_command(label="Zoom")

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)


blank = Text(win, font=("arail", 11), bg='#272C35', fg='#fff', width='720', height='480')
blank.pack()

print(dir(Menu))

win.mainloop()