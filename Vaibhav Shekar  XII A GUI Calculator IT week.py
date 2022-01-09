from tkinter import *
exp = ""
memory = 0

def press(num):
    global exp         #global keyword allows you to modify the variable outside of the current scope. It is used to create a global variable and make changes to the variable in a local context.
    exp = exp + str(num) 
    eqn.set(exp)
      
def clear():
    global exp
    exp = ""
    eqn.set(exp)
    
def total():
    global exp
    total = str(eval(exp))  # str- returs as string, eval-evaluates 
    exp = total
    eqn.set(total)
      
def memstore():
    global exp
    global memory
    memory = memory + int(exp)
   
def memrecall():
    global exp
    global memory
    exp = str(memory)
    eqn.set(exp)
      
def memclear():
    global memory
    memory = 0
       
gui=Tk()
gui.title('Calculator')
gui.configure(background = "#F5F5F5")
gui.geometry("357x348")
gui.resizable(0,0)
    
eqn = StringVar()
txt = Entry(gui, textvariable = eqn, bg = 'white', relief = SUNKEN, borderwidth = 5, width = 34)
txt.grid(columnspan = 4, ipadx = 70)
 
button1 = Button(gui,font=('Helvetica',11), text = '1', fg = 'black', bg = "#eee", cursor = "hand2", command=lambda:press(1), height=3, width = 9)
button1.grid(row=4, column= 0)
    
button2 = Button(gui,font=('Helvetica',11), text = '2', fg = 'black', bg = "#eee", cursor = "hand2", command=lambda:press(2), height=3, width = 9)
button2.grid(row=4, column= 1)
        
button3 = Button(gui,font=('Helvetica',11), text = '3', fg = 'black', bg = "#eee", cursor = "hand2", command=lambda:press(3), height=3, width = 9)
button3.grid(row=4, column= 2)

button4 = Button(gui, font=('Helvetica',11), text = '4', fg = 'black', bg = "#eee", cursor = "hand2", command=lambda:press(4), height=3, width = 9)
button4.grid(row=3, column= 0)
    
button5 = Button(gui, font=('Helvetica',11), text = '5', fg = 'black', bg = "#eee", cursor = "hand2", command=lambda:press(5), height=3, width = 9)
button5.grid(row=3, column= 1)

button6 = Button(gui, font=('Helvetica',11), text = '6', fg = 'black',bg = "#eee", cursor = "hand2", command=lambda:press(6), height=3, width = 9)
button6.grid(row=3, column= 2)

button7 = Button(gui, font=('Helvetica',11), text = '7', fg = 'black', bg = "#eee", cursor = "hand2", command=lambda:press(7), height=3, width = 9)
button7.grid(row=2, column= 0)
    
button8 = Button(gui, font=('Helvetica',11), text = '8', fg = 'black', bg = "#eee", cursor = "hand2", command=lambda:press(8), height=3, width = 9)
button8.grid(row=2, column= 1)
    
button9 = Button(gui, font=('Helvetica',11), text = '9', fg = 'black', bg = "#eee", cursor = "hand2", command=lambda:press(9), height=3, width = 9)
button9.grid(row=2, column=2)
    
button0 = Button(gui,font=('Helvetica',11), text = '0', fg = 'black', bg = "#eee", cursor = "hand2", command=lambda:press(0), height=3, width = 9)
button0.grid(row=5, column= 1)
    
mlt = Button(gui, font=('Helvetica',10,'bold'),text = '╳', fg = 'black', bg = '#E0FFFF', command=lambda:press('*'), height=3, width = 9)
mlt.grid(row=1, column= 3)
    
dvd = Button(gui,font=('Helvetica',10, 'bold'), text = '➗', fg = 'black', bg = '#E0FFFF', command=lambda:press('/'), height=3, width = 9)
dvd.grid(row=4, column= 3)
    
eq = Button(gui, font=('Helvetica',16),text = '=', fg = 'black', bg = '#90EE90', command=total, height=2, width = 6)
eq.grid(row=5, column= 3)
    
add = Button(gui,font=('Helvetica',10, 'bold'), text = '➕', fg = 'black', bg = '#E0FFFF', command=lambda:press('+'), height=3, width = 9)
add.grid(row=2, column= 3)
    
sub = Button(gui,font=('Helvetica',10, 'bold'), text = '➖', fg = 'black', bg = '#E0FFFF', command=lambda:press('-'), height=3, width = 9)
sub.grid(row=3, column= 3)
    
clr = Button(gui,font=('Helvetica',11), text = 'Clear', fg = 'black', bg = '#ADD8E6', command=clear, height=3, width = 9)
clr.grid(row=5, column= 0)
    
dcml = Button(gui,font=('Helvetica',11), text = '◉(dec)', fg = 'black', bg = "#eee", cursor = "hand2", command=lambda:press('.'), height=3, width = 9)
dcml.grid(row=5, column= 2)

memstr = Button(gui,font=('Helvetica',11), text = 'M+', fg = 'black', bg = '#ADD8E6', command=memstore, height=3, width = 9)
memstr.grid(row=1,column= 2)

memr = Button(gui,font=('Helvetica',11), text = 'Mr', fg = 'black', bg = '#ADD8E6', command=memrecall, height=3, width = 9)
memr.grid(row=1,column= 1)

memclr = Button(gui,font=('Helvetica',11), text = 'MC', fg = 'black', bg = '#ADD8E6', command=memclear, height=3, width = 9)
memclr.grid(row=1,column= 0)
  
gui.mainloop()

    
