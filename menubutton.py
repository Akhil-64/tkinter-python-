from tkinter import *
root=Tk()
master=Menubutton(root,text="menubutton",activebackground="blue")
master.grid()
master.menu=Menu(master,tearoff=0)
master["menu"]=master.menu
a=IntVar()
b=IntVar()
master.menu.add_checkbutton(label="option1",variable=a,activebackground="powder blue")
master.menu.add_checkbutton(label="option2",variable=b,activebackground="powder blue")
master.pack()

root.mainloop()
