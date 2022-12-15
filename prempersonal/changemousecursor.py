from tkinter import *

root = Tk()
root.geometry('600x600')
cursors = ['arrow', 'circle', 'clock', 'cross', 'dotbox', 'exchange', 'fleur', 'heart', 'man', 'mouse', 'pirate',
           'plus', 'shuttle', 'sizing', 'spider', 'spraycan', 'star', 'target', 'tcross', 'trek', 'watch']
for cursor in cursors:
    Button(root, text=cursor, cursor=cursor).pack_configure(padx=10, pady=5)

root.mainloop()
