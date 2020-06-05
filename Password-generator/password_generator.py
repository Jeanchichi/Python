import string
from random import randint, choice
from tkinter import *

def genarate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits

    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)



window = Tk()
window.title("Password generator")
window.geometry("720x480")
window.minsize(720, 480)
window.iconbitmap('lock.ico')
window.config(background='#181818')

frame = Frame(window, bg='#181818')

width = 300
height = 300
image = PhotoImage(file='password.png').zoom(32).subsample(32)
canvas = Canvas(frame, width=width, height=height, bg='#181818', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

right_frame = Frame(frame, bg='#181818')

label_title = Label(right_frame, text="Password generator", font=("Helvetica", 20), bg='#181818', fg='white')
label_title.pack()

password_entry = Entry(right_frame, font=("Helvetica", 20), bg='#181818', fg='white')
password_entry.pack()

generate_button = Button(right_frame, text="Generate", font=("Helvetica", 15), bg='white', fg='black', command=genarate_password)
generate_button.pack(pady=20, fill=X)


right_frame.grid(row=0, column=1, sticky=W)

frame.pack(expand=YES)


window.mainloop()
