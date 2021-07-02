import tkinter as tk
root=tk.Tk()
root.geometry("300x500")
def button():
    if t.get()=="0":
        msg=messagebox.showinfo("Name","Name is "+t2.get())
    elif t.get()=="1":
        msg=messagebox.showinfo("L-Name","Surname is "+t2.get())
label=tk.Label(root, text="Enter 0 for F-name and 1 for L-name")
label.grid(row=0)
t=tk.Entry(root)
t.grid(row=0, column=1)
label=tk.Label(root, text="Input")
label.grid(row=1)
t2=tk.Entry(root)
t2.grid(row=1, column=1)
b=tk.Button(root, text="Enter", command=button)
b.grid(row=2,column=1)
root.mainloop()