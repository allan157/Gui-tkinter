from tkinter import *
import os

creds = 'tempfile.temp'

def signup():
    global pwordE
    global nameE
    global roots


    roots = Tk()
    roots.title('signup')
    intruction =  Label(roots, text='Please enter new cridentials\n')
    intruction.grid(row=0, column=0, sticky=E)

    nameL = Label(roots, text='New Username: ')
    PwordL = Label(roots, text='New Password: ')
    nameL.grid(row=1, column=0, sticky=W)
    PwordL.grid(rows=2, column=0, sticky=W)

    nameE = Entry(roots)
    nameE = Entry(roots, show='*')

    signUpButton = Button(roots, text='Signup', command=FSSignup)
    signUpButton.grid(columnspan=2, sticky=W )
    roots.mainloop()

def FSSignup():
    with open(creds, 'w')as f:
        f.write(nameE.get())
        f.write('\n')
        f.write(pwordE.get())
        f.close()

        roots.destory()
        Login()

    def Login():
        global NameEL
        global pwordEL

        rootA = Tk()
        rootA.title('Login')

        intruction = Label(rootA,text='Please Login\n')
        intruction.grid(dticky=E)

        nameL = Label(rootA, text='username:')
        pwordL = Label(rootA, text='Password: ')
        nameL.grid(row=2, sticky=W)

        nameEL =  Entry(rootA)
        nameEL = Entry(rootA, show='*')
        nameEL.grid(row=1, column=1)
        nameEL.grid(row=2, column=1)
        pwordL.grid(row=2,column=1)

        loginB = Button(rootA, text='Login', command=CheckLogin)
        loginB.grid(columnspan=2, sticky=W)

        rnuser = Button(rootA, text='Delete user', fg='red', command=DelUser)
        rnuser.grid(columnspan=2, sticky=W)

    def CheckLogin():
        with open(creds) as f:
            data = f.readlines()
            uname = data[0].rstrip()
           pword = data[1].rstrip()
        if NameEL.get() == uname and pwordEL == pword:
            r = Tk()
            r.title(':D')
            r.geometry('150x50')
            rlbl = Label(r, text='\n[!] Invalid ogin')
            rlbl.pack()
            r.mainloop()

    def DelUser():
        os.remove(creds)
        rootA.destroy()
        signup()

    if os.path.isfile(creds):
        Login()
    else:
        signup()