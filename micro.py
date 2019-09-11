import tkinter as tk
from tkinter import *
import tkinter.messagebox

from PIL import ImageTk,Image
list1=[]
list2=['DIS50','DIS100']
def prom():
    data=e3.get()
    x='n'
    for i in list2:
        if i==data:
            x='Y'
            tkinter.messagebox.showinfo(title="Hello %s"%(nameinfo.get()),message="Promotion Applied")
            tot=sum(list1)
            temp=tot
            gst=tot*0.08
            cgst=tot*0.08
            total=tot+gst+cgst
            dis=total-(total*0.05)            
            print ("Gross Total :",tot)
            print ("GST : ",gst)
            print ("CGST : ",cgst)
            print ("Total Amount Payable : ",tot+gst+cgst)
            tkinter.messagebox.showinfo(title="Hello %s”"%(nameinfo.get()),message="Gross Total: Rs. %d/- \n GST : Rs. %e/- \n CGST : Rs. %f/- \n Amount to be Paid : Rs. %g/-"%(tot,gst,cgst,dis))
            

    while x=='n':
        tkinter.messagebox.showinfo(title="Hello %s"%(nameinfo.get()),message="Invalid")
        break
def add():
    data=Lb.get(ACTIVE)
    if data=='Pen 10/-':
        tb.insert(END,'\nPen\t10/- x %d'%(qnt.get()+1) )
        list1.append(10*(qnt.get()+1))
    elif data=='Pencil 5/-':
        tb.insert(END,'\nPencil\t5/- x %d'%(qnt.get()+1))
        list1.append(5*(qnt.get()+1))
    elif data=='Eraser 10/-':
        tb.insert(END,'\nEraser\t10/- x %d'%(qnt.get()+1))
        list1.append(10*(qnt.get()+1))

    elif data=='Sharpner 15/-':
        tb.insert(END,'\nSharpner\t15/- x %d'%(qnt.get()+1))
        list1.append(15*(qnt.get()+1))
    elif data=='Notebook 30/-':
        tb.insert(END,'\nNotebook\t30/- x %d'%(qnt.get()+1))
        list1.append(30*(qnt.get()+1))
    elif data=='Scale 12/-':
        tb.insert(END,'\nScale\t12/- x %d'%(qnt.get()+1))
        list1.append(12*(qnt.get()+1))
    elif data=='A4 paper 1/-':
        tb.insert(END,'\nA4 paper\t1/- x %d'%(qnt.get()+1))
        list1.append(1*(qnt.get()+1))
    

def total():
    tot=sum(list1)
    temp=tot
    gst=tot*0.08
    cgst=tot*0.08
    total=tot+gst+cgst
    print ("Gross Total : ",tot)
    print ("GST : ",gst)
    print ("CGST : ",cgst)
    print ("Total Amount Payable : ",tot+gst+cgst)
    tkinter.messagebox.showinfo(title="Hello %s”"%(nameinfo.get()),message="Gross Total: Rs. %d/- \n GST : Rs. %e/- \n CGST : Rs. %f/- \n Amount to be Paid : Rs. %g/-"%(tot,gst,cgst,total))
def clr():
    tb.delete(1.0,END)
    del list1[:]

    tkinter.messagebox.showinfo(title="Hello %s"%(nameinfo.get()),message="WELCOME")
    

f=Tk()
f.title("WELCOME TO SUPERMARKET")

f.configure(background='brown')
img= ImageTk.PhotoImage(Image.open("ghostsupermarket.jpg"))
#Displaying it
imglabel=Label(f,image=img).grid(row=6,column=1,padx=5,pady=5)
nameinfo=StringVar()
data=IntVar()
qnt=IntVar()
promocode=StringVar()
#Label("Supermarket Billing System")
name=Label(f,text='Customer Name :')
e1=Entry(f,width=30,bd=3,textvariable=nameinfo)
prod=Label(f,text='Products :')
Lb=Listbox(f,height=15,width=35,bd=3)
Lb.insert(0,'Items')
Lb.insert(1,'')
Lb.insert(2,'Pen 10/-')
Lb.insert(3,'Pencil 5/-' )
Lb.insert(4,'Eraser 10/-')
Lb.insert(5,'Sharpner 15/-')
Lb.insert(6,'Notebook 30/-')
Lb.insert(7,'Scale 12/-')
Lb.insert(8,'A4 paper 1/-' )
quan=Label(f,text='Quantity :')
e2=Entry(f,width=10,bd=3,textvariable=qnt)
promo=Label(f,text='Promo Code :')
e3=Entry(f,width=30,bd=3,textvariable=StringVar)
b4=Button(f,text='Apply',width=12,bd=3,command=prom)
b1=Button(f,text='Add Items',width=12,bd=3,command=add)
tb=Text(f,height=5,width=20,bd=3)
b3=Button(f,text='Clear Items',width=12,bd=3,padx=3,command=clr)
b2=Button(f,text='Total',width=12,bd=3,command=total)

name.grid(row=0,column=0,padx=5,pady=5)
e1.grid(row=0,column=1,padx=3,pady=3)
prod.grid(row=1,column=0,padx=5,pady=5)
Lb.grid(row=1,column=1,padx=5,pady=5)
quan.grid(row=2,column=0,padx=5,pady=5)
e2.grid(row=2,column=1,padx=0,pady=5)
promo.grid(row=3,column=0,padx=5,pady=5)
e3.grid(row=3,column=1,padx=4,pady=4)
b1.grid(row=1,column=2,padx=3,pady=3)
tb.grid(row=6,column=3,columnspan=10,padx=5,pady=5)
b3.grid(row=2,column=2,padx=5,pady=5)
b2.grid(row=6,column=15,padx=5,pady=50)
b4.grid(row=3,column=2,padx=5,pady=5)
f.mainloop()
