import tkinter as tk
root=tk.Tk(className="Tkinter Button")
root.geometry("300x300")

counter=100
def CountdownTimer(label):
    counter=100
    def count1():
        global counter
        counter -=1
        label.config(text=str(counter))
        label.after(1000,count1)
    count1()
label=tk.Label(root,fg="purple")
label.pack()
CountdownTimer(label)
button=tk.Button(root,text="Stop",fg="red",command=root.destroy)
button.pack(side=tk.LEFT)


root.mainloop()
