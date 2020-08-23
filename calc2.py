# calc_using_tkinter
# Made a simple calculator which perform a basic maths calculation in python using tkinter.

from tkinter import *
root=Tk()

root.title("Calc")
root.geometry("570x440")
root.resizable(0,0)
root.configure(bg="black")

val=StringVar()

def clear():
    val.set("")

def enter(value):
    val.set(val.get()+value)

def evaluate():
    try:
        val.set(eval(val.get()))
    except Exception as e:
        val.set("Error")
        print(e)


entry=Entry(root,justify=RIGHT,font=("" ,30),insertwidth=4,textvariable=val)
entry.place(x=10,y=10,height=50,width=550)

b1=Button(root,text="7",font=("" ,30),bg="gray",activebackground="yellow",activeforeground="red")
b1.place(x=10,y=70,width=130)
b1.configure(command=lambda :enter("7"))

b2=Button(root,text="8",font=("" ,30),bg="gray",activebackground="yellow",activeforeground="red")
b2.place(x=150,y=70,width=130)
b2.configure(command=lambda :enter("8"))

b3=Button(root,text="9",font=("" ,30),bg="gray",activebackground="yellow",activeforeground="red")
b3.place(x=290,y=70,width=130)
b3.configure(command=lambda :enter("9"))

b4=Button(root,text="/",font=("" ,30),bg="gray",activebackground="yellow",activeforeground="red")
b4.place(x=430,y=70,width=130)
b4.configure(command=lambda :enter("/"))

b5=Button(root,text="4",font=("" ,30),bg="gray",activebackground="yellow",activeforeground="red")
b5.place(x=10,y=160,width=130)
b5.configure(command=lambda :enter("4"))

b6=Button(root,text="5",font=("" ,30),bg="gray",activebackground="yellow",activeforeground="red")
b6.place(x=150,y=160,width=130)
b6.configure(command=lambda :enter("5"))

b7=Button(root,text="6",font=("" ,30),bg="gray",activebackground="yellow",activeforeground="red")
b7.place(x=290,y=160,width=130)
b7.configure(command=lambda :enter("6"))

b8=Button(root,text="*",font=("" ,30),bg="gray",activebackground="yellow",activeforeground="red")
b8.place(x=430,y=160,width=130)
b8.configure(command=lambda :enter("*"))

b9=Button(root,text="1",font=("" ,30),bg="gray",activebackground="yellow",activeforeground="red")
b9.place(x=10,y=250,width=130)
b9.configure(command=lambda :enter("1"))

b10=Button(root,text="2",font=("" ,30),bg="gray",activebackground="yellow",activeforeground="red")
b10.place(x=150,y=250,width=130)
b10.configure(command=lambda :enter("2"))

b11=Button(root,text="3",font=("" ,30),bg="gray",activebackground="yellow",activeforeground="red")
b11.place(x=290,y=250,width=130)
b11.configure(command=lambda :enter("3"))

b12=Button(root,text="-",font=("" ,30),bg="gray",activebackground="yellow",activeforeground="red")
b12.place(x=430,y=250,width=130)
b12.configure(command=lambda :enter("-"))

b13=Button(root,text="C",font=("" ,30),bg="gray",activebackground="yellow",activeforeground="red")
b13.place(x=10,y=340,width=130)
b13.configure(command=clear)

b14=Button(root,text="0",font=("" ,30),bg="gray",activebackground="yellow",activeforeground="red")
b14.place(x=150,y=340,width=130)
b14.configure(command=lambda :enter("0"))

b15=Button(root,text="=",font=("" ,30),bg="gray",activebackground="yellow",activeforeground="red")
b15.place(x=290,y=340,width=130)
b15.configure(command=evaluate)

b16=Button(root,text="+",font=("" ,30),bg="gray",activebackground="yellow",activeforeground="red")
b16.place(x=430,y=340,width=130)
b16.configure(command=lambda :enter("+"))

root.mainloop()
