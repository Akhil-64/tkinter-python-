from tkinter import *
root=Tk()
scale=Scale(root,from_=50,to=100,orient=HORIZONTAL)
scale1=Scale(root,from_=100,to=200)
scale.pack()
scale1.pack()
root.mainloop()
