import subprocess as sb_p
import tkinter as tk
import registerVoter as regV
import admFunc as adFunc
from tkinter import *
from registerVoter import *
from admFunc import *


def AdminHome(root,frame1,frame3):
    root.title("ADMIN")
    for widget in frame1.winfo_children():
        widget.destroy()

    Button(frame3, text="ADMIN", command = lambda: AdminHome(root, frame1, frame3)).grid(row = 1, column = 0)
    frame3.pack(side=TOP)

    Label(frame1, text="ADMIN", font=('Helvetica', 25, 'bold')).grid(row = 0, column = 1)
    Label(frame1, text="").grid(row = 1,column = 0)

    #Admin Login
    #runServer = Button(frame1, text="RUN SERVER", width=15, command = lambda: sb_p.call('start python Server.py', shell=True))

    #Voter Login
    registerVoter = Button(frame1, text="REGISTER VOTER", width=15, command = lambda: regV.Register(root, frame1))

    #Show Votes
    showVotes = Button(frame1, text="SHOW VOTES", width=15, command = lambda: adFunc.showVotes(root, frame1))

    #Reset Data
    #reset = Button(frame1, text="RESET ALL", width=15, command = lambda: adFunc.resetAll(root, frame1))

    Label(frame1, text="").grid(row = 2,column = 0)
    Label(frame1, text="").grid(row = 4,column = 0)
    #Label(frame1, text="").grid(row = 6,column = 0)
    #Label(frame1, text="").grid(row = 8,column = 0)
    #runServer.grid(row = 3, column = 1, columnspan = 2)
    registerVoter.grid(row = 2, column = 1, columnspan = 2)
    showVotes.grid(row = 4, column = 1, columnspan = 2)
    #reset.grid(row = 9, column = 1, columnspan = 2)

    frame1.pack()
    root.mainloop()


def log_admin(root,frame1,admin_ID,password):

    if(admin_ID=="Admin" and password=="NidhiNehaNikitha"):
        frame3 = root.winfo_children()[1]
        AdminHome(root, frame1, frame3)
        msg = Message(frame1, text="ADMIN LOGIN SUCCESSFUL", width=500)
    elif(password!="NidhiNehaNikitha"):
         msg = Message(frame1, text="INCORRECT PASSWORD! TRY AGAIN .", width=500)
         msg.grid(row = 6, column = 0, columnspan = 5)
    else:
        msg = Message(frame1, text="INCORRECT ID! TRY AGAIN .", width=500)
        msg.grid(row = 6, column = 0, columnspan = 5)


def AdmLogin(root,frame1):

    root.title("ADMIN LOGIN")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="ADMIN LOGIN", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 2, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)
    Label(frame1, text="Admin ID:      ", anchor="e", justify=LEFT).grid(row = 2,column = 0)
    Label(frame1, text="Password:       ", anchor="e", justify=LEFT).grid(row = 3,column = 0)

    admin_ID = tk.StringVar()
    password = tk.StringVar()

    e1 = Entry(frame1, textvariable = admin_ID)
    e1.grid(row = 2,column = 2)
    e2 = Entry(frame1, textvariable = password, show = '*')
    e2.grid(row = 3,column = 2)

    sub = Button(frame1, text="LOGIN", width=10, command = lambda: log_admin(root, frame1, admin_ID.get(), password.get()))
    Label(frame1, text="").grid(row = 4,column = 0)
    sub.grid(row = 5, column = 3, columnspan = 2)

    frame1.pack()
    root.mainloop()
