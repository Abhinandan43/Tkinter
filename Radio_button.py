from tkinter import *
root=Tk(className="RadioButton")
root.geometry("300x300")

radioVariable=IntVar()
radio1=Radiobutton(root,text="January",fg="blue",variable=radioVariable,value=1).grid(row=0,column=0)
radio2=Radiobutton(root,text="February",fg="blue",variable=radioVariable,value=2).grid(row=1,column=0)
radio3=Radiobutton(root,text="March",fg="blue",variable=radioVariable,value=3).grid(row=2,column=0)
radio4=Radiobutton(root,text="April",fg="blue",variable=radioVariable,value=4).grid(row=3,column=0)

# We can also use grid method as
"""
radio1.grid(column=0,row=0)
radio2.grid(column=0,row=1)
radio3.grid(column=0,row=2)
radio4.grid(column=0,row=3)
"""

root.mainloop()
