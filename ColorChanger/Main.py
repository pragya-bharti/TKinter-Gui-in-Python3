from tkinter import *
root = Tk()
root.title("Color Selector")
root.geometry('400x200')

options_list = ['white', 'black', 'yellow', 'green', 'blue', 'grey', 'red']

selection = StringVar(root)
selection.set('white')

def set_color(v):
    option_menu.config(activebackground=v)
    option_menu.config(background=v)
    label.config(text= f'Color: {v}')

option_menu = OptionMenu(root, selection, *options_list, command = set_color)
option_menu.pack()
label = Label(root)
label.pack(pady=20)

set_color(selection.get())

root.mainloop()