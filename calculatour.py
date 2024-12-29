from tkinter import Tk , Button , StringVar ,Entry
class Calculatour:
    def __init__(self,master) :
        master.title("Calculatour")
        master.geometry("357x420")
        master.config(bg='gray')
        master.resizable(False,False)
        self.equictoin=StringVar()
        self.entry_value=""
        Entry(width=17,bg='lightblue',font=('Arial Blod',28),textvariable=self.equictoin).place(x=0,y=0)#1
        Button(width=11,height=4,text="(",activebackground="#F5E216",relief="flat",bg="white",command=lambda:self.show('(')).place(x=0,y=50)#1
        Button(width=11,height=4,text=")",activebackground="#F5E216",relief="flat",bg="white",command=lambda:self.show(')')).place(x=90,y=50)#2
        Button(width=11,height=4,text="%",activebackground="#F5E216",relief="flat",bg="white",command=lambda:self.show('%')).place(x=180,y=50)#3
        Button(width=11,height=4,text="1",activebackground="#F5E216",relief="flat",bg="white",command=lambda:self.show(1)).place(x=0,y=125)#4
        Button(width=11,height=4,text="2",activebackground="#F5E216",relief="flat",bg="white",command=lambda:self.show(2)).place(x=90,y=125)#5
        Button(width=11,height=4,text="3",activebackground="#F5E216",relief="flat",bg="white",command=lambda:self.show(3)).place(x=180,y=125)#6
        Button(width=11,height=4,text="4",activebackground="#F5E216",relief="flat",bg="white",command=lambda:self.show(4)).place(x=0,y=200)#7
        Button(width=11,height=4,text="5",activebackground="#F5E216",relief="flat",bg="white",command=lambda:self.show(5)).place(x=90,y=200)#8
        Button(width=11,height=4,text="6",activebackground="#F5E216",relief="flat",bg="white",command=lambda:self.show(6)).place(x=180,y=200)#9
        Button(width=11,height=4,text="7",activebackground="#F5E216",relief="flat",bg="white",command=lambda:self.show(7)).place(x=0,y=275)#10
        Button(width=11,height=4,text="8",activebackground="#F5E216",relief="flat",bg="white",command=lambda:self.show(8)).place(x=180,y=275)#11
        Button(width=11,height=4,text="9",activebackground="#F5E216",relief="flat",bg="white",command=lambda:self.show(9)).place(x=90,y=275)#12
        Button(width=11,height=4,text="0",activebackground="#F5E216",relief="flat",bg="white",command=lambda:self.show(0)).place(x=90,y=350)#13
        Button(width=11,height=4,text=".",activebackground="#F5E216",relief="flat",bg="white",command=lambda:self.show('.')).place(x=180,y=350)#14
        Button(width=11,height=4,text="+",activebackground="#F5E216",relief="flat",bg="white",command=lambda:self.show('+')).place(x=270,y=275)#15
        Button(width=11,height=4,text="-",activebackground="#F5E216",relief="flat",bg="white",command=lambda:self.show('-')).place(x=270,y=200)#16
        Button(width=11,height=4,text="/",activebackground="#F5E216",relief="flat",bg="white",command=lambda:self.show('/')).place(x=270,y=50)#17
        Button(width=11,height=4,text="x",activebackground="#F5E216",relief="flat",bg="white",command=lambda:self.show('*')).place(x=270,y=125)#18
        Button(width=11,height=4,text="=",activebackground="#F5E216",relief="flat",bg="lightblue",command=self.solve).place(x=270,y=350)#19
        Button(width=11,height=4,text="c",activebackground="#F5E216",relief="flat",command=self.clear).place(x=0,y=350)#20
    def show(self,valu):
       self.entry_value+=str(valu)
       self.equictoin.set(self.entry_value)
    def clear(self):
       self.entry_value=""
       self.equictoin.set(self.entry_value)
    def solve(self):
        result=eval(self.entry_value)
        self.equictoin.set(result)  
root=Tk()
calculatour1=Calculatour(root)
root.mainloop()    