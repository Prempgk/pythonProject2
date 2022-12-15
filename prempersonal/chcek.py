from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os

def new():
    global file
    file=None
    root.title('Untitle-Notepad')
    TextArea.delete(1.0,END)



def new_window():
    def new():
        global file
        file = None
        root.title('Untitle-Notepad')
        TextArea.delete(1.0, END)

    def Openfile():
        global file
        file = askopenfilename(initialfile='Untitled.txt', defaultextension='.txt',
                               filetypes=[('All Files', "*.*"), ("Text Documents", "*.txt")])
        if file == '':
            file = None
        else:
            root.title(os.path.basename(file) + '-Notepad')
            TextArea.delete(1.0, END)
            f = open(file, 'r')
            TextArea.insert(1.0, f.read())
            f.close()

    def savefile():
        global file
        if file == None:
            file = asksaveasfilename(initialfile='untitled.txt', defaultextension='.txt',
                                     filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])
            if file == '':
                f = None
            else:
                f = open(file, 'w')
                f.write(TextArea.get(1.0, END))
                f.close()
                root.title(os.path.basename(file) + '-Notepad')
                print('File saved')
        else:
            f = open(file, 'w')
            f.write(TextArea.get(1.0, END))
            f.close()

    def cut():
        TextArea.event_generate(('<<Cut>>'))

    def copy():
        TextArea.event_generate(('<<Copy>>'))

    def paste():
        TextArea.event_generate(('<<Paste>>'))

    def quitapp():
        root.destroy()

    def about():
        showinfo('Notepad','Notepad by Code with Prem')

    root = Tk()
    root.geometry('600x600')
    root.title('Untitled-Notepad')
    TextArea = Text(root, font='lucida 13', undo=True)
    file = None
    TextArea.pack(expand=True, fill=BOTH)
    Menubar = Menu(root)
    FileMenu = Menu(Menubar, tearoff=0)
    FileMenu.add_command(label='New', command=new)
    FileMenu.add_command(label='New File', command=new_window)
    FileMenu.add_command(label='Open', command=Openfile)
    FileMenu.add_command(label='Save', command=savefile)
    FileMenu.add_separator()
    FileMenu.add_command(label='Exit', command=quitapp)
    Menubar.add_cascade(label='File', menu=FileMenu)
    EditMenu = Menu(Menubar, tearoff=0)
    Menubar.add_cascade(label='Edit', menu=EditMenu)
    EditMenu.add_command(label='Cut', command=cut)
    EditMenu.add_command(label='Copy', command=copy)
    EditMenu.add_command(label='Paste', command=paste)
    EditMenu.add_command(label='Undo', command=TextArea.edit_undo)
    EditMenu.add_command(label='Redo', command=TextArea.edit_redo)
    EditMenu.add_separator()
    HelpMenu = Menu(Menubar, tearoff=0)
    HelpMenu.add_command(label='About', command=about)
    HelpMenu.add_cascade(label='Help', menu=HelpMenu)
    HelpMenu.add_separator()
    root.config(menu=Menubar)
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
    root.mainloop()


def Openfile():
    global file
    file=askopenfilename(initialfile='Untitled.txt',defaultextension='.txt',filetypes=[('All Files', "*.*"), ("Text Documents", "*.txt")])
    if file=='':
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
        file = asksaveasfilename(initialfile='untitled.txt', defaultextension='.txt',
                                 filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])
        if file == '':
            f = None
        else:
            f = open(file, 'w')
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+'-Notepad')
            print('File saved')
    else:
        f=open(file,'w')
        f.write(TextArea.get(1.0,END))
        f.close()

def cut():
    TextArea.event_generate(('<<Cut>>'))
def copy():
    TextArea.event_generate(('<<Copy>>'))
def paste():
    TextArea.event_generate(('<<Paste>>'))
def quitapp():
    root.destroy()
def about():
    showinfo('Notepad','Notepad by Code with Prem')


root=Tk()
root.geometry('600x600')
root.title('Untitled-Notepad')
TextArea=Text(root,font='lucida 13',undo=True)
file=None
TextArea.pack(expand=True,fill=BOTH)
Menubar = Menu(root)
FileMenu = Menu(Menubar,tearoff=0)
FileMenu.add_command(label='New',command=new)
FileMenu.add_command(label='New File',command=new_window)
FileMenu.add_command(label='Open',command=Openfile)
FileMenu.add_command(label='Save',command=savefile)
FileMenu.add_separator()
FileMenu.add_command(label='Exit',command=quitapp)
Menubar.add_cascade(label='File',menu=FileMenu)
EditMenu = Menu(Menubar,tearoff=0)
Menubar.add_cascade(label='Edit',menu=EditMenu)
EditMenu.add_command(label='Cut',command=cut)
EditMenu.add_command(label='Copy',command=copy)
EditMenu.add_command(label='Paste',command=paste)
EditMenu.add_command(label='Undo',command=TextArea.edit_undo)
EditMenu.add_command(label='Redo',command=TextArea.edit_redo)
EditMenu.add_separator()
HelpMenu = Menu(Menubar,tearoff=0)
HelpMenu.add_command(label='About',command=about)
Menubar.add_cascade(label='Help',menu=HelpMenu)
HelpMenu.add_separator()
root.config(menu=Menubar)
Scroll = Scrollbar(TextArea)
Scroll.pack(side=RIGHT,fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)
root.mainloop()