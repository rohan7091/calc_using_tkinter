# calc_using_tkinter
#Made a simple calculator which perform a basic maths calculation in python using tkinter.

from tkinter import *

root=Tk()
root.title("Calculator")
root.geometry("330x550")
root.wm_iconbitmap("calcu.ico")
root.resizable(0,0)

def click(event):
    val=event.widget.cget("text")
    global scrvl
    if(val== "="):
        if(scrvl.get().isdigit()):
            value=int(scrvl.get())
        else:
            try:
                value=round(eval(scr.get()),5)
            except Exception as e:
                print(e)
                value="Error"

        scrvl.set(value)
        scr.update()

    elif(val=="C"):
        scrvl.set("")
        scr.update()

    else:
        scrvl.set(scrvl.get()+val)
        scr.update()

scrvl=StringVar()
scrvl.set("")

scr=Entry(root,textvariable=scrvl,font=("lucida",30,"bold"),insertwidth=4, bd=10,justify=RIGHT)
scr.pack(fill=X,padx=10,pady=10,ipadx=20)

f=Frame(root)
b=Button(f,text="7",font=("lucida",20,"bold",),bg="grey",padx=15,pady=15)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="8",font=("lucida",20,"bold"),bg="grey",padx=15,pady=15)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="9",font=("lucida",20,"bold"),bg="grey",padx=15,pady=15)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="/",font=("lucida",20,"bold"),bg="grey",padx=18,pady=15)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root)
b=Button(f,text="4",font=("lucida",20,"bold",),bg="grey",padx=15,pady=15)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="5",font=("lucida",20,"bold"),bg="grey",padx=15,pady=15)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="6",font=("lucida",20,"bold"),bg="grey",padx=15,pady=15)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="*",font=("lucida",20,"bold"),bg="grey",padx=18,pady=15)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root)
b=Button(f,text="1",font=("lucida",20,"bold",),bg="grey",padx=15,pady=15)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="2",font=("lucida",20,"bold"),bg="grey",padx=15,pady=15)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="3",font=("lucida",20,"bold"),bg="grey",padx=15,pady=15)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="-",font=("lucida",20,"bold"),bg="grey",padx=18,pady=15)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root)
b=Button(f,text=".",font=("lucida",20,"bold",),bg="grey",padx=19,pady=15)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="0",font=("lucida",20,"bold"),bg="grey",padx=15,pady=15)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="00",font=("lucida",20,"bold"),bg="grey",padx=7,pady=15)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="+",font=("lucida",20,"bold"),bg="grey",padx=15,pady=15)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root)
b=Button(f,text="C",font=("lucida",20,"bold",),bg="grey",padx=53,pady=15)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)


b=Button(f,text="=",font=("lucida",20,"bold"),bg="grey",padx=54,pady=15)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

f.pack()

root.mainloop()
