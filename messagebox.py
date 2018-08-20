from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('Message', 'pop up messages of tkinter')

answer = tkinter.messagebox.askquestion('Question 1', 'are you happy?')
if answer == 'yes':
    print('Morning Sir!')
else:
    print('morning madam!')

root.mainloop()
