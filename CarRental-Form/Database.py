my_conn=sqlite3.connect('DATABASE1.db')
import tkinter as tk
from tkinter import *
import sqlite3
my_w=tk.Tk()
my_w.geometry("5000x5000")
r_set=my_conn.execute('''SELECT * from DETAILS LIMIT 0,10''');
i=0
for DETAILS in r_set:
    for j in range(len(DETAILS)):
        e=Entry(my_w,width=10,fg='blue')
        e.grid(row=i,column=j)
        e.insert(END,DETAILS[j])
    i=i+1
my_w.mainloop()