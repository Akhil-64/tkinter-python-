from tkinter import *
root=Tk()
v=IntVar()
master=Radiobutton(root,text="GfG",variable=v,value=1).pack(anchor=W)#anchor for left alignment
master=Radiobutton(root,text="Pnj",variable=v,value=2).pack(anchor=W)
root.mainloop()
