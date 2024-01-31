# MAKING A PRESENT CLICKING TTIME CLOCK 
from tkinter import Tk
from tkinter import Label
import time

root = Tk()
root.title('Clock')

def presnt_time():
  display_time = time.strftime("%H:%M:%S %p")
  digitalclock.config(text=display_time)
  digitalclock.after(200, presnt_time)


digitalclock = Label(root, font=('arial',150), bg="blue", fg="beige" )

digitalclock.pack()

presnt_time()

root.mainloop()












