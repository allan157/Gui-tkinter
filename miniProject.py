from tkinter import  *

def doNothing():
    print('once clicked should be linked to a main root window')

root = Tk()

#**** Main Menu***

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label='File', menu= subMenu)
subMenu.add_command(label='New Project..', command=doNothing)
subMenu.add_command(label='New', command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="exit", command=doNothing)

editMenu =Menu(menu)
menu.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Redo', command=doNothing)

#***** Toolbar***
toolbar = Frame(root, bg='blue')

insertButt = Button(toolbar, text='Insert image', command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt =  Button(toolbar, text="Print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

#*** statusbar ****

status = Label(root, text='preparing to display..', bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


root.mainloop()