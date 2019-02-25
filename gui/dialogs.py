# from tkinter import *
# from tkinter.messagebox import *
# def answer():
#     showerror("Answer", "Sorry, no answer available")
# def callback():
#     if askyesno('Verify', 'Really quit?'):
#         showwarning('Yes', 'Not yet implemented')
#     else:
#         showinfo('No', 'Quit has been cancelled')
# Button(text='Quit', command=callback).pack(fill=X)
# Button(text='Answer', command=answer).pack(fill=X)
# mainloop()



from tkinter import *
from tkinter.filedialog   import askopenfilename      
def callback():
    name= askopenfilename() 
    print (name)
errmsg = 'Error!'
Button(text='File Open', command=callback).pack(fill=X)
mainloop()