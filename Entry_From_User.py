from tkinter import *
root=Tk(className=" Entry Method from User")
root.geometry("300x300")

Label(root,text="Email Id",fg="green").grid(row=0)

label2=Label(root,text="Password",fg="green").grid(row=1)

a1=Entry(root).grid(row=0,column=1)
a2=Entry(root).grid(row=1,column=1)
root.mainloop()
