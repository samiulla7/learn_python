import tkinter as tk
from tkinter import *

root = tk.Tk()
# w = tk.Label(root,text="Hello Samiulla")
# canv = Canvas(root, width=80, height=80, bg='white')
# canv.grid(row=2, column=3)
# img = PhotoImage(file="download.jpeg")
# canv.create_image(20,20, anchor=NW, image=img)

# logo = PhotoImage(file="download.jpeg")
# w1 = tk.Label(root,image=canv).pack('right')
w1 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 50, 
              text="hello").pack(side="right")
explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""

w2 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=explanation).pack(side="left")
root.mainloop()