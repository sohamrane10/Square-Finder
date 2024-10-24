# GUI-->graphical user interface

from tkinter import *
root=Tk()
root.title("Square Finder by Soham Rane")
root.geometry("1000x400")
f=("Arial",40,"bold")

def find():
	try:    
		num=float(ent.get())
		square=num**2
		res="square="+str(round(square,2))
		msg.configure(text=res)
	except ValueError:
		res="You should enter numbers only"
		msg.configure(text=res)

lab=Label(root,text="Enter Number ",font=f)
lab.pack(pady=5)
ent=Entry(root,font=f)
ent.pack(pady=5)
btn=Button(root,text="Find Square",font=f,command=find)
btn.pack(pady=5)
msg=Label(root,font=f)
msg.pack(pady=5)

root.mainloop()