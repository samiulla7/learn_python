# from tkinter import *
# master = Tk()
# var1 = IntVar()
# Checkbutton(master, text="male", variable=var1).grid(row=0,column=1, sticky=W)
# var2 = IntVar()
# Checkbutton(master, text="female", variable=var2).grid(row=0,column=2, sticky=W)
# mainloop()


# from tkinter import *
# master = Tk()

# def var_states():
#    print("male: %d,\nfemale: %d" % (var1.get(), var2.get()))

# Label(master, text="Your sex:").grid(row=0, sticky=W)
# var1 = IntVar()
# Checkbutton(master, text="male", variable=var1).grid(row=1, sticky=W)
# var2 = IntVar()
# Checkbutton(master, text="female", variable=var2).grid(row=2, sticky=W)
# Button(master, text='Quit', command=master.quit).grid(row=3, sticky=W, pady=4)
# Button(master, text='Show', command=var_states).grid(row=4, sticky=W, pady=4)
# mainloop()


from tkinter import *
class Checkbar(Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)
   def state(self):
      return map((lambda var: var.get()), self.vars)
if __name__ == '__main__':
   root = Tk()
   lng = Checkbar(root, ['Python', 'Ruby', 'Perl', 'C++'])
   tgl = Checkbar(root, ['English','German'])
   lng.pack(side=TOP,  fill=X)
   tgl.pack(side=LEFT)
   lng.config(relief=GROOVE, bd=2)

   def allstates(): 
      print(list(lng.state()), list(tgl.state()))
   Button(root, text='Quit', command=root.quit).pack(side=RIGHT)
   Button(root, text='Peek', command=allstates).pack(side=RIGHT)
   root.mainloop()