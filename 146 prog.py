from tkinter import *
master=Tk()
canvas=Canvas(master,height=800,width=800)
w=canvas.create_oval(150,20,350,200,fill="red")
w=canvas.create_oval(50,500,400,300)

w=canvas.create_arc(500,300,700,50,start=90,extent=180,style="arc")
w=canvas.create_arc(300,400,600,300,start=180,extent=360,style="arc")
canvas.create_arc(600,100,700,300,style="arc",start=0,extent=45)




canvas.create_rectangle(450,400,600,600,fill="red",outline="black")

canvas.create_line(700,350,400,350)
canvas.create_line(700,400,700,600)


canvas.pack()
master.mainloop()
