from tkinter import Tk, Frame, Label
from time import strftime

root = Tk()
root.title("Watch")
root.config(bg="black")

frame = Frame()
frame.pack()
frame.config(width=300, height=300, bg="black")

def update():
	current_time = strftime("%H:%M:%S")
	Label(frame, text=current_time, bg="black", fg="white", font=210).grid(row=1, column=0)
	root.after(100, update)

date = strftime("%d/%b/%Y")

Label(frame, text=date, bg="black", fg="white", font=220).grid(row=0, column=0)
	
update()

root.mainloop()