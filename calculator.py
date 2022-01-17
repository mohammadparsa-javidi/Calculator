from tkinter import *
win = Tk()
win.title("calculator")

def btnClick(number):
    global val
    
    val = val+str(number)
    data.set(val)
val = ""

def btnClear():
    global val
    val = "" 
    data.set(val)

def btnEquals():
    global val
    result=str(eval(val))
    data.set(result)


win.geometry("500x500")
data = StringVar()
entry = Entry(win,textvariable=data,bd=29,justify=RIGHT,font=("ariel",20))
entry.grid(row=1,columnspan=4)

btn1 = Button(win,text="1",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda: btnClick(1))
btn1.place(x=0,y=95)
btn2 = Button(win,text="2",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda: btnClick(2))
btn2.place(x=88,y=95)
btn3 = Button(win,text="3",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda: btnClick(3))
btn3.place(x=178,y=95)
btn_add = Button(win,text="+",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda: btnClick("+"))
btn_add.place(x=269,y=95)
btn4 = Button(win,text="4",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda: btnClick(4))
btn4.place(x=0,y=165)
btn5 = Button(win,text="5",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda: btnClick(5))
btn5.place(x=88,y=165)
btn6 = Button(win,text="6",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda: btnClick(6))
btn6.place(x=178,y=165)
btn_sub = Button(win,text="-",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda: btnClick("-"))
btn_sub.place(x=268,y=165)
btn7 = Button(win,text="7",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda: btnClick(7))
btn7.place(x=0,y=235)
btn8 = Button(win,text="8",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda: btnClick(8))
btn8.place(x=88,y=235)
btn9 = Button(win,text="9",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda: btnClick(9))
btn9.place(x=180,y=235)
btn_multipy = Button(win,text="*",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda: btnClick("*"))
btn_multipy.place(x=270,y=235)
btn_division = Button(win,text="/",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda: btnClick("/"))
btn_division.place(x=270,y=310)
btn_dot = Button(win,text=".",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda: btnClick("."))
btn_dot.place(x=360,y=310)
btn0 = Button(win,text="0",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda: btnClick(0))
btn0.place(x=88,y=308)
btn_equals = Button(win,text="=",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=btnEquals)
btn_equals.place(x=180,y=310)
btn_clear = Button(win,text="clear",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=btnClear)
btn_clear.place(x=0,y=310)

win.mainloop()