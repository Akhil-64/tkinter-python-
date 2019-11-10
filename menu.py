from tkinter import *
root=Tk()

menu=Menu(root)
filemenu=Menu(menu,tearoff=0)

filemenu.add_command(label="New")
filemenu.add_command(label="Open...")
filemenu.add_separator()
filemenu.add_command(label="Exit")
menu.add_cascade(label="File",menu=filemenu)

helpmenu=Menu(menu,tearoff=0)
helpmenu.add_command(label="About")
menu.add_cascade(label="Help",menu=helpmenu)




root.config(menu=menu)
mainloop()
