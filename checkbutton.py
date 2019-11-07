from tkinter import *
master=Tk()
master.title("checkbutton")
checkbutton=Checkbutton(master,text="male",activebackground="powder blue")
checkbutton2=Checkbutton(master,text="female",activebackground="powder blue")
checkbutton.grid(sticky=W)
checkbutton2.grid(sticky=W)
master.mainloop()

