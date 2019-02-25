# from tkinter import *
# master = Tk()
# Label(master, text="First Name").grid(row=0)
# Label(master, text="Last Name").grid(row=1)
# e1 = Entry(master)
# e2 = Entry(master)
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
# mainloop( )


# from tkinter import *
# def show_entry_fields():
#    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
# master = Tk()
# Label(master, text="First Name").grid(row=0)
# Label(master, text="Last Name").grid(row=1)
# e1 = Entry(master)
# e2 = Entry(master)
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
# Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
# Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
# mainloop()


# from tkinter import *
# def show_entry_fields():
#    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
#    e1.delete(0,END)
#    e2.delete(0,END)
# master = Tk()
# Label(master, text="First Name").grid(row=0)
# Label(master, text="Last Name").grid(row=1)
# e1 = Entry(master)
# e2 = Entry(master)
# e1.insert(10,"Miller")
# e2.insert(10,"Jill")
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
# Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
# Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
# mainloop( )



from tkinter import *
fields = 'Last Name', 'First Name', 'Job', 'Country'
def fetch(entries):
   for entry in entries:
      field = entry[0]
      text  = entry[1].get()
      print('%s: "%s"' % (field, text)) 
def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries
if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
   b1 = Button(root, text='Show',
          command=(lambda e=ents: fetch(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Quit', command=root.quit)
   b2.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()