import tkinter as tk

def Hello():
    root1=tk.Tk()
    root1.title("Window2")
    root1.geometry("100x100")
    x=tk.Label(root1,text="Hello , Wow :)")
    x.pack()
    root1.mainloop()


root=tk.Tk()
root.title("Button Example")
root.geometry("400x400")

button=tk.Button(root,text="Quit",fg="purple",command=quit)
button.pack(side=tk.BOTTOM)

button2=tk.Button(root,text="New Button",fg="magenta",command=Hello)
button2.pack(side=tk.TOP)

root.mainloop()
