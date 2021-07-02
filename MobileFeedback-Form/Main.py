import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox


root= Tk()
root.geometry("500x500")
root.title("FEEDBACK")


def mentry ():
    name.delete(0,END)
    receipt.delete(0,END)
    
   
    
label_0 = Label (root, text="Mobile Feedback", width=20,font=("bold",18))
label_0.place(x=120,y=0)

label_1 = Label(root, text="Name Of the Phone",width=20,font=("bold",10))
label_1.place(x=-20,y=71)

name = Entry(root, borderwidth=0,width=35)
name.place(x=140,y=68)

label_2 = Label(root, text="Model Name", width=20,font=("bold",10))
label_2.place(x=-20,y=100)


receipt = Entry(root, borderwidth=0,width=35)
receipt.place(x=140,y=97)


label_3 = Label (root, text="Feedback", width=20,font=("bold",12))
label_3.place(x=-20,y=130)


label_4 = Label (root, text="Q1.Are you satisfied with the performance?",font=("bold",10))
label_4.place(x=20,y=160)

var=IntVar()
rb1=Radiobutton(root, text="Yes", padx=5,variable=var,  value=1).place(x=20,y=180)
rb2=Radiobutton(root, text="Partially", padx=5, variable=var, value=2).place(x=90,y=180)
rb3=Radiobutton(root, text="No", padx=5, variable=var,value=3).place(x=180,y=180)

var.set(2)

label_5 = Label(root, text="Q2.Are you satisfied with the camera?",font=("bold",10))
label_5.place(x=20,y=210)

var=IntVar()
rb4=Radiobutton(root, text="Yes", padx=5,variable=var, value=1).place(x=20,y=240)
rb5=Radiobutton(root, text="Partially", padx=20,variable=var,  value=2).place(x=74,y=240)
rb6=Radiobutton(root, text="No", padx=5,variable=var,  value=3).place(x=180,y=240)

var.set(5)

label_6 = Label(root, text="Q3.Are you satisfied with the battery?",font=("bold",10))
label_6.place(x=20,y=270)

var=IntVar()
rb7=Radiobutton(root, text="Yes", padx=5,variable=var, value=1).place(x=20,y=300)
rb8=Radiobutton(root, text="Partially", padx=20,variable=var, value=2).place(x=74,y=300)
rb9=Radiobutton(root, text="No", padx=5, variable=var,value=3).place(x=180,y=300)

var.set(7)

reset=Button(root, text="New Entries",command=mentry).place(x=100,y=350)

msg=Button(root,text="SUBMIT").place(x=200,y=350) 

root.mainloop()