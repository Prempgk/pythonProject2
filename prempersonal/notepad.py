from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def newfile():
    global file
    root.title('Untitled-Notepad')
    file=None
    TextArea.delete(1.0,END)


def openfile():
    global file
    file=askopenfilename(initialfile='untitled.txt',defaultextension='.txt',filetypes=[('All Files',"*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+'-Notepad')
        TextArea.delete(1.0,END)
        f=open(file,'r')
        TextArea.insert(1.0,f.read())
        f.close()


def savefile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile='Untitled.txt',defaultextension='.txt',filetypes=[('All Files','*.*'),('Text Documents','*.txt')])
        if file=='':
            f=None
        else:
            f=open(file,'w')
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+'-Notepad')
            print('File Saved')
    else:
        f = open(file, 'w')
        f.write(TextArea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy()
def cut():
    TextArea.event_generate(('<<Cut>>'))
def copy():
    TextArea.event_generate(('<<Copy>>'))
def paste():
    TextArea.event_generate(('<<Paste>>'))

def about():
    showinfo('Notepad','Notepad by Code with Prem')



def newwindow():
    def newfile():
        global file
        root.title('Untitled-Notepad')
        file = None
        TextArea.delete(1.0, END)

    def openfile():
        global file
        file = askopenfilename(initialfile='untitled.txt',defaultextension='.txt', filetypes=[('All Files', "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            root.title(os.path.basename(file) + '-Notepad')
            TextArea.delete(1.0, END)
            f = open(file, 'r')
            TextArea.insert(1.0, f.read())
            f.close()

    def Paste():
        TextArea.event_generate(('<<Paste>>'))

    def cut():
        TextArea.event_generate(('<<Cut>>'))

    def copy():
        TextArea.event_generate(('<<Copy>>'))



    root = Tk()
    root.title('Untitled-Notepad')
    root.geometry('644x788')
    TextArea = Text(root, font='lucida 13', undo=True)
    file = None
    TextArea.pack(expand=True,fill=BOTH)
    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label='New', command=newfile)
    FileMenu.add_command(label='New Window', command=newwindow)
    FileMenu.add_command(label='Open', command=openfile)
    FileMenu.add_command(label='Save', command=savefile)
    FileMenu.add_separator()
    FileMenu.add_command(label='Exit', command=quitApp)
    MenuBar.add_cascade(label='File', menu=FileMenu)
    EditMenu = Menu(MenuBar, tearoff=0)
    EditMenu.add_command(label='Cut', command=cut)
    EditMenu.add_command(label='Copy', command=copy)
    EditMenu.add_command(label='Paste', command=Paste)
    EditMenu.add_command(label='Undo', command=TextArea.edit_undo)
    EditMenu.add_command(label='Redo', command=TextArea.edit_redo)
    MenuBar.add_cascade(label='Edit', menu=EditMenu)
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label='About Notepad', command=about)
    MenuBar.add_cascade(label='Help', menu=HelpMenu)
    root.config(menu=MenuBar)
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
    root.mainloop()




root=Tk()
root.title('Untitled-Notepad')
root.geometry('644x788')
TextArea=Text(root,font='lucida 13',undo=True)
file=None
TextArea.pack(expand=True,fill=BOTH)
MenuBar=Menu(root)
FileMenu=Menu(MenuBar,tearoff=0)
FileMenu.add_command(label='New',command=newfile)
FileMenu.add_command(label='New Window', command=newwindow)
FileMenu.add_command(label='Open',command=openfile)
FileMenu.add_command(label='Save',command=savefile)
FileMenu.add_separator()
FileMenu.add_command(label='Exit',command=quitApp)
MenuBar.add_cascade(label='File',menu=FileMenu)
EditMenu=Menu(MenuBar,tearoff=0)
EditMenu.add_command(label='Cut',command=cut)
EditMenu.add_command(label='Copy', command=copy)
EditMenu.add_command(label='Paste', command=paste)
EditMenu.add_command(label='Undo',command=TextArea.edit_undo)
EditMenu.add_command(label='Redo', command=TextArea.edit_redo)
MenuBar.add_cascade(label='Edit',menu=EditMenu)
HelpMenu=Menu(MenuBar,tearoff=0)
HelpMenu.add_command(label='About Notepad',command=about)
MenuBar.add_cascade(label='Help',menu=HelpMenu)
root.config(menu=MenuBar)
Scroll=Scrollbar(TextArea)
Scroll.pack(side=RIGHT,fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)
root.mainloop()