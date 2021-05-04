from tkinter import *
root=Tk(className="Tkinter Frame")
root.geometry("300x300")

frame=Frame(root)
frame.pack()

leftFrame=Frame(root)
leftFrame.pack(side=LEFT)

rightFrame=Frame(root)
rightFrame.pack(side=RIGHT)

button1=Button(frame,text="Submit",fg="Red",activebackground="magenta",command=quit)
button1.pack(side=LEFT)

button2=Button(frame,text="Remove",fg="green",activebackground="purple",command=root.destroy)
button2.pack(side=RIGHT)

root.mainloop()
