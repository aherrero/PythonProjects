
from tkinter import *
from tkinter.ttk import *   # For the combobox

from tkinter import scrolledtext    #specify for scrolltext
from tkinter import messagebox  # specify for messagebox

from tkinter.ttk import Progressbar

value_progress = 0

def clicked():
    # lbl.configure(text="Clicked")
    text_lbl = txt.get()
    lbl2.configure(text= text_lbl)

    txtcombo =  combo.get()
    print("the combo is: " + txtcombo)

    global value_progress   # For some reason, in python3, the var are always local, if it is not explit to take the global
    value_progress += 1
    bar['value'] = value_progress
    bar2['value'] = value_progress

def clickedrad1():
    print("clicked First!")
    messagebox.showinfo('Message title','Message content')

def clickedrad2():
    messagebox.showwarning('Message title', 'second!')  #shows warning message

def clickedrad3():
    messagebox.showerror('Message title', 'third!')    #shows error message

    res = messagebox.askquestion('Message title','Message content')

def clicked2():
    res = messagebox.askyesno('Message title','Message content')
    res = messagebox.askyesnocancel('Message title','Message content')
    res = messagebox.askokcancel('Message title','Message content')
    res = messagebox.askretrycancel('Message title','Message content')


window = Tk()

window.geometry('800x600')

# frame.grid(column=0, row=0, columnspan=3, rowspan=2)

window.title("Welcome to My App")

lbl = Label(window, text="Hello", font=("Arial Bold", 14))
lbl.grid(column=0, row=0, columnspan=1, pady=5, padx=5)

lbl2 = Label(window, text="", font=("Arial Bold", 14))
lbl2.grid(column=1, row=0, columnspan=1, pady=5, padx=5)

btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=0, row=1,  columnspan=1, pady=5, padx=5)

# btn2 = Button(window, text="Click Me 2", bg="orange", fg="red")   # Not valid for tkinter.ttk
style = Style()
style.configure("BW.TLabel", foreground="black", background="red")
btn2 = Button(window, text="Click Me 2", style="BW.TLabel", command=clicked2)
btn2.grid(column=1, row=1,  columnspan=1, pady=5, padx=5)

txt = Entry(window,width=10)
txt.grid(column=0, row=2, columnspan=2, pady=5, padx=5)
txt.focus()

txt2 = Entry(window, width=10, state='disabled')
txt2.grid(column=0, row=3, columnspan=2, pady=5, padx=5)

combo = Combobox(window)
combo['values']= (1, 2, 3, 4, 5, "Text")
combo.current(1) #set the selected item
combo.grid(column=0, row=4, columnspan=2, pady=5, padx=5)

chk_state = BooleanVar()
chk_state.set(True) #set check state
chk = Checkbutton(window, text='Choose', var=chk_state)
chk.grid(column=0, row=5, columnspan=2, pady=5, padx=5)

rad1 = Radiobutton(window,text='First', value=1, command=clickedrad1)
rad2 = Radiobutton(window,text='Second', value=2, command=clickedrad2)
rad3 = Radiobutton(window,text='Third', value=3, command=clickedrad3)
rad1.grid(column=0, row=6, columnspan=1, pady=5, padx=5)
rad2.grid(column=1, row=6, columnspan=1, pady=5, padx=5)
rad3.grid(column=0, row=7, columnspan=2, pady=5, padx=5)

# selected = IntVar()
# rad1 = Radiobutton(window,text='First', value=1, variable=selected)
# print(selected.get())

txt2 = scrolledtext.ScrolledText(window,width=100,height=10)
txt2.grid(column=0,row=8, columnspan=2, pady=5, padx=5)
txt2.delete(1.0,END)
txt2.insert(INSERT,'You text goes here')

spin = Spinbox(window, from_=0, to=100, width=5)
spin.grid(column=0,row=9, columnspan=1, pady=5, padx=5)

var =IntVar()
var.set(36)
spin2 = Spinbox(window, from_=0, to=100, width=5, textvariable=var)
spin2.grid(column=1,row=10, columnspan=1, pady=5, padx=5)

bar = Progressbar(window, length=200)
bar.grid(column=0,row=11, columnspan=2, pady=5, padx=5)

style = Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='green')
bar2 = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
bar2.grid(column=0,row=12,columnspan=2, pady=5, padx=5)

window.mainloop()
