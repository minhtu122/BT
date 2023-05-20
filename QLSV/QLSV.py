from tkinter import *
from database import *

def add():
    line =code.get()+'-'+name.get()+'-'+year.get()+'-'+address.get()
    save(line)
    show()
def show():
    sv=read()
    listbox.delete(0,END)
    for i in sv:
        listbox.insert(END,i)
def sort():
    sv=read()
    for i in range(len(sv)):
        for j in range(len(sv)):
            x,y=sv[i], sv[j]
            if x[2]>y[2]:
                sv[i], sv[j]= y,x
    listbox.delete(0,END)
    for i in sv:
        listbox.insert(END,i)
def delete():
    listbox.delete(0,END)
              
root=Tk()
root.title('Quản lý sinh viên')

code=StringVar()
name=StringVar()
year=StringVar()
address=StringVar()

Label(root,text='ỨNG DỤNG QUẢN LÝ SINH VIÊN',fg='red', font=('cambria',16),width=25).grid(row=0)
listbox=Listbox(root,width=80, height=20)
listbox.grid(row=1,columnspan=2)
show()

label_MSV = Label(root,text='Mã sinh viên:')
label_MSV.grid(row=2,column=0)
Entry(root,width=40,textvariable=code).grid(row=2,column=1)

label_Name = Label(root,text='Tên sinh viên:')
label_Name.grid(row=3,column=0)
Entry(root,width=40,textvariable=name).grid(row=3,column=1)

label_year = Label(root,text='Năm sinh:')
label_year.grid(row=4,column=0)
Entry(root,width=40,textvariable=year).grid(row=4,column=1)

label_address = Label(root,text='Địa chỉ:')
label_address.grid(row=5,column=0)
Entry(root,width=40,textvariable=address).grid(row=5,column=1)

button=Frame(root)
Button(button,text='Thêm',command=add).pack(side=LEFT)
Button(button,text='Xoá',command=delete).pack(side=LEFT)
Button(button,text='Sắp xếp',command=sort).pack(side=LEFT)
Button(button,text='Thoát',command=root.destroy).pack(side=LEFT)
button.grid(row=6,column=1)

root.mainloop
