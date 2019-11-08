from tkinter import *
master=Tk()
root=Canvas(master,height=500,width=500)
root.create_arc(20,30,300,300,start=90,extent=180,fill="powder blue",outline="red")
root.create_arc(400,300,200,50,start=90,extent=180,style="arc",outline="red")#style=cord
root.create_text(130,350,text="semi-cirle",font="Times 20 italic bold")
root.create_text(300,350,text="arc",font="Times 20 italic bold")
root.pack()
master.mainloop()
