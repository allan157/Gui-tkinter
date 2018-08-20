from tkinter import *

root = Tk()

photo = PhotoImage(file="myface.jpg")
label = Label(root, image=photo)
label.pack()
root.mainloop()