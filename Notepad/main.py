from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import pandas as pd
import os
from tkinter.filedialog import askopenfile, asksaveasfilename

win = ThemedTk(theme="aqua")
win.title("Notepad")
win.geometry("720x480")
win.minsize(720, 480)
win.config(background='#272C35')

def open_file():
    blank.delete("1.0", END)
    file = askopenfile(mode='r', filetypes=[('All', '*'), ('Text files', '*.txt'), ('Hyper Text Language Markup', '*.html'), ('Comma-Separated Values', '*.csv')])
    if file is not None:
        text = file.read()
        blank.insert("1.0", text)

def save_file():
    notepad_text = blank.get("1.0", "end-1c")
    file = asksaveasfilename(title="Save", filetypes=[('All', '*'), ('Text files', '*.txt'), ('Hyper Text Language Markup', '*.html'), ('Comma-Separated Values', '*.csv')])
    with open(file, "w") as data:
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
editmenu.add_command(label="Undo")
editmenu.add_command(label="Redo")
editmenu.add_separator()
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_separator()
editmenu.add_command(label="Delete")
editmenu.add_command(label="Cancel")
editmenu.add_command(label="Restore")

displaymenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Display", menu=displaymenu)
displaymenu.add_command(label="Zoom")

toolsmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Tools", menu=toolsmenu)
toolsmenu.add_command(label="Preferences")

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About")


blank = Text(win, font=("arail", 11), bg='#272C35', fg='#fff', width='720', height='480')
blank.pack()

print(dir(Menu))

win.mainloop()