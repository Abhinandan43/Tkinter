import tkinter as tk

root=tk.Tk()
root.title("Geometry Method")
root.geometry("300x300")

a=tk.Label(root, text="Python",bg="red",fg="white")
a.pack(fill=tk.X,padx=10,side=tk.LEFT)

a=tk.Label(root, text="Java",bg="blue",fg="white")
a.pack(fill=tk.X,padx=8,side=tk.LEFT)

a=tk.Label(root, text="C++",bg="green",fg="white")
a.pack(fill=tk.X,padx=6,side=tk.LEFT)

a=tk.Label(root, text="Ruby",bg="indigo",fg="white")
a.pack(fill=tk.X,padx=4,side=tk.LEFT)

root.mainloop()
