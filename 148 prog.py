from tkinter import *
master=Tk()
master.title("Canvas")
f1=PhotoImage(file="giphy.gif")
f2=PhotoImage(file=".gif")
root=Canvas(master,height=1000,width=1000,cursor="plus")
id=root.create_image(800,200,image=f1,anchor=NE,activeimage=f2)
id=root.create_text(500,100,text="Image",font="Times 20 italic bold")
root.pack()
master.mainloop()
