import tkinter as tk
root=tk.Tk(className=" Grid Geometry")
root.geometry("300x300")

colours={'red','green','blue','magenta','yellow','purple'}
c=0
for x in colours:
    tk.Label(text=x,relief=tk.RIDGE,width=20).grid(row=c,column=0)
    tk.Entry(bg=x,relief=tk.SUNKEN,width=10).grid(row=c,column=1)
    c += 1
root.mainloop()
