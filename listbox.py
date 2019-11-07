from tkinter import *
root=Tk()
listbox=Listbox(root,bg="pink",bd=5,height=10,width=20)
listbox.insert(1,"Car")
listbox.insert(2,"Bus")
listbox.insert(3,"Scooter")
listbox.pack()
root.mainloop()
