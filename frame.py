from tkinter import *
root=Tk()
frame=Frame(root)
frame.pack()


root.title("Frames")

redbutton=Button(frame,activeforeground="red",height=10,width=10,text="red")
redbutton.pack(side=LEFT)
bluebutton=Button(frame,activeforeground="blue",height=10,width=10,text="blue")
bluebutton.pack(side=LEFT)
whitebutton=Button(frame,activeforeground="powder blue",height=10,width=10,text="poder blue")
whitebutton.pack(side=LEFT)
greenbutton=Button(frame,activeforeground="green",height=10,width=10,text="green")
greenbutton.pack(side=BOTTOM)
mainloop()
