from tkinter import *
m=Tk()
m.title("Canvas")
master=Canvas(m,bd=25,width=200,height=100,highlightcolor="red",cursor="plus")
master.pack()
height=100
width=500
y=int(height/2)
master.create_line(0, y,width, y )
p=[100,200,30,40,50,100,20,400]
master.create_polygon(p,fill="orange",outline="red")
#m.geometry("330*220 + 300 + 300")
m.mainloop()
