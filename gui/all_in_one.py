from tkinter import *
import tkinter as tk
from tkinter.filedialog   import askopenfilename      
from tkinter.messagebox import *

def NewFile():
    print ("New File!")
def OpenFile():
    name = askopenfilename()
    print (name)
def About():
    print ("This is a simple example of a menu")

def dialog():
    if askyesno('Verify', 'Really quit?'):
        # showwarning('Yes', 'Not yet implemented')
        master.destroy()
    else:
        showinfo('No', 'Quit has been cancelled')


def show_entry_fields():
    rval = ""
    if var.get() !=0: 
        rval = "Male" if var.get()==1 else "Female"
    checkboxes = [CheckVarEng.get(), CheckVarHnd.get(), CheckVarTam.get(), CheckVarTel.get()]
    selected_lang = list(filter(lambda x:(x!=""), checkboxes))
    print("First Name: %s\nLast Name: %s\nGender : %s\nSelected Language : %s" \
        % (e1.get(), e2.get(), rval, selected_lang))

master = Tk()

master.title("Pythn GUI")
width = 500
height = 250
screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()
x = (screen_width/4) - (width/4)
y = (screen_height/4) - (height/4)
master.geometry("%dx%d+%d+%d" % (width, height, x, y))
master.resizable(0, 0)
master.config(bg="#6666ff")


''' Radio button starts here '''
var = IntVar()
def get_radio_button(m):
    Label(m,text="Gender").grid(row=3)
    R1 = Radiobutton(m, text="Male", variable=var, value=1)
    R1.grid(row=3,column=1)
    R2 = Radiobutton(m, text="Female", variable=var, value=2)
    R2.grid(row=3,column=2)
''' Radio button ends here '''


''' Checkbox starts here '''
CheckVarEng = StringVar()
CheckVarHnd = StringVar()
CheckVarTel = StringVar()
CheckVarTam = StringVar()

def get_checkbox(m):
    Label(m,text="Languages").grid(row=4)
    c1 = Checkbutton(m, text = "English", variable = CheckVarEng, \
                    onvalue = "English", offvalue = "")
    c2 = Checkbutton(m, text = "Hindi", variable = CheckVarHnd, \
                    onvalue = "Hindi", offvalue = "")  
    c3 = Checkbutton(m, text = "Telgu", variable = CheckVarTel, \
                    onvalue = "Telgu", offvalue = "")  
    c4 = Checkbutton(m, text = "Tamil", variable = CheckVarTam, \
                    onvalue = "Tamil", offvalue = "")  
    c1.grid(row=4, column=1)
    c2.grid(row=4, column=2)
    c3.grid(row=5, column=1)
    c4.grid(row=5, column=2)
    
''' Checkbox ends here '''


''' Menu starts here '''
def menu(m):
    menu = Menu(m)
    m.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="New", command=NewFile)
    filemenu.add_command(label="Open...", command=OpenFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=dialog)

    helpmenu = Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About...", command=About)

''' Menu ends here '''
    
Label(master, text="First Name",fg="blue").grid(row=0)
Label(master, text="Last Name").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

menu(master)
get_radio_button(master)
get_checkbox(master)

Button(master, text='Quit', command=master.quit).grid(row=6, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=6, column=1, sticky=W, pady=4)

mainloop()