from tkinter import *
import os
savedFile = {1:""}


class Win:
    def create(self):
        self.master = Tk()
        self.master.title("Notepad")
        self.master.geometry("720x480")
        self.master.minsize(720, 480)
        self.master.config(background='#272C35')

    def add_text(self):
        self.content = Text(self.master, font=("arail", 11), bg='#272C35', fg='#fff', width='720', height='480')
        self.content.pack(expand=1, fill='both')

    def generate(self):
        self.master.mainloop()

    def add_menu(self):

        menuBar = Menu(self.master)

        menuFichier = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="File", menu=menuFichier)

        menuFichier.add_command(label="New", command=self.new)
        menuFichier.add_command(label="Open", command=self.fopen)
        menuFichier.add_command(label="Save", command=self.save)
        menuFichier.add_command(label="Save as", command=self.saveAs)
        menuFichier.add_command(label="Exit", command=self.quitter)
        self.master.config(menu=menuBar)

        menuEdition = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Edit", menu=menuEdition)
        menuEdition.add_command(label="Cancel")
        menuEdition.add_command(label="Restore")
        menuEdition.add_command(label="Copy", command=self.copy)
        menuEdition.add_command(label="Cut", command=self.cut)
        menuEdition.add_command(label="Paste", command=self.past)

        menuOutils = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Tools", menu=menuOutils)
        menuOutils.add_command(label="Preferences")

        menuAide = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Help", menu=menuAide)
        menuAide.add_command(label="About")

    def quitter(self):
        self.master.quit()

    def new(self):
        os.popen("python main.py")

    def fopen(self):
        file = self.master.filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(
            ("Text Files", "*.txt"), ("all files", "*.*")))
        fp = open(file, "r")
        r = fp.read()
        self.content.insert(1.0, r)

    def saveAs(self):
        # create save dialog
        fichier = self.master.filename = filedialog.asksaveasfilename(initialdir="/",
                                                                      title="Enregistrer Sous\         ", filetypes=(
                ("Fichier Texte", "*.txt"), ("Tous les fichiers", "*.*")))
        fichier = fichier + ".txt"
        # Utilisation du dictionnaire pour stocker le fichier
        savedFile[1] = fichier
        f = open(fichier, "w")
        s = self.content.get("1.0", END)
        f.write(s)
        f.close()

    def save(self):
        if savedFile[1] == "":
            self.saveAs()
        else:
            f = open(savedFile[1], "w")
        s = self.content.get("1.0", END)
        f.write(s)
        f.close()

    def copy(self):
        self.content.clipboard_clear()
        self.content.clipboard_append(self.content.selection_get())

        def past(self):
            self.content.insert(INSERT, self.content.clipboard_get())

    def cut(self):
        self.copy()
        self.content.delete("sel.first", "sel.last")
