from tkinter import *
root=Tk(className="CheckBox")
root.geometry("300x300")
var1=IntVar()
Checkbutton(root,text="Male",fg="blue",variable=var1).grid(row=0,sticky=W)

var2=IntVar()
Checkbutton(root,text="Female",fg="blue",variable=var2).grid(row=1,sticky=W)

root.mainloop()
