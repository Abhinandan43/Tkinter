from tkinter import *
root=Tk()
root.title("My first page")
root.geometry("300x300")

var=StringVar()
label=Label(root,textvariable=var,relief=RAISED)
var.set("This is my House")
label.pack()

root.mainloop()
