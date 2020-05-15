from tkinter import *
root = Tk()
root.title("calculator")
root.resizable(0,0)
root.columnconfigure(0, weight=1)
root.rowconfigure(2, weight=1) 
f1 = Frame(root,width = 100,height = 80,highlightbackground="black",highlightthickness = 1)
f1.grid(padx = 20,pady =20)
ent =Entry(f1,width = 15)
ent.grid(padx = 3)
f2 = Frame(f1)
f2.grid()
math = ""
#-------Functions-------#
def button_click(num):
    current = ent.get()
    ent.delete(0,END)
    ent.insert(0,current+str(num))
    
def add():
    global math
    global f_num
    f = ent.get()
    math = "addition"
    f_num = int(f)
    ent.delete(0,END)
    
def subtract():
    global math
    global f_num
    f = ent.get()
    math = "subtraction"
    f_num = int(f)
    ent.delete(0,END)
    


def multiply():
    global math
    global f_num
    f = ent.get()
    math = "multiplication"
    f_num = int(f)
    ent.delete(0,END)
    


def divide():
    global math
    global f_num
    f = ent.get()
    math = "division"
    f_num = int(f)
    ent.delete(0,END)
    

def equal():
   global math
   s = ent.get()
   sec_num = int(s)
   ent.delete(0,END)
   if math == "addition":
       r = f_num + sec_num
       print(r)
       
   elif math == "subtraction":
       r = f_num - sec_num
       
   elif math == "multiplication":
       r = f_num*sec_num
      
   elif math == "division":
       r = f_num / sec_num
   
   ent.insert(0,r)
   
   
            
def clear():
    ent.delete(0,END)

#------Functions-End---#




#------Buttons-----#
num1 = Button(f2,text = "1",width = 5,height = 2,command=lambda: button_click(1))
num1.grid(row = 1,column = 0,padx = 2)
num2 = Button(f2,text = "2",width = 5,height = 2,command=lambda: button_click(2))
num2.grid(row = 1,column = 1,padx = 2)
num3 = Button(f2,text = "3",width = 5,height = 2,command=lambda: button_click(3))
num3.grid(row = 1,column = 2,padx = 2)
num4 = Button(f2,text = "4",width = 5,height = 2,command=lambda: button_click(4))
num4.grid(row = 2,column = 0,padx = 2)
num5 = Button(f2,text = "5",width = 5,height = 2,command=lambda: button_click(5))
num5.grid(row = 2,column = 1,padx = 2)
num6 = Button(f2,text = "6",width = 5,height = 2,command=lambda: button_click(6))
num6.grid(row = 2,column = 2,padx = 2)
num7 = Button(f2,text = "7",width = 5,height = 2,command=lambda: button_click(7))
num7.grid(row = 3,column = 0,padx = 2)
num8 = Button(f2,text = "8",width = 5,height = 2,command=lambda:button_click(8))
num8.grid(row = 3,column = 1,padx = 2)
num9 = Button(f2,text = "9",width = 5,height = 2,command=lambda: button_click(9))
num9.grid(row = 3,column = 2,padx = 2)
num0 = Button(f2,text = "0",width = 5,height = 2,command=lambda: button_click(0))
num0.grid(row = 4,column = 1,padx = 2)
multiply = Button(f2,text = "x",width = 5,height = 2,command = multiply)
multiply.grid(row = 1,column = 3,padx = 2)
sub = Button(f2,text = "-",width = 5,height = 2,command = subtract)
sub.grid(row = 2,column = 3,padx = 2)
result = Button(f2,text = "=",width = 5,height = 2,command = equal)
result.grid(row = 4,column = 0,padx = 2)
divide = Button(f2,text = "/",width = 5,height = 2,command = divide)
divide.grid(row = 4,column = 3,padx = 2)
add = Button(f2,text = "+",width = 5,height = 2,command=add)
add.grid(row = 3,column = 3,padx = 2)
clear = Button(f2,text = "CLR",width = 5,height = 2,command = clear)
clear.grid(row = 4,column = 2,padx = 2)


#------Buttons-End-----#




root.mainloop()
