from tkinter import *

def add():
    line = id.get()+'-'+name.get()+'-'+year.get()
    save(line)
def show():
    sv=read()
    listbox.delete(0,END)
    for i in sv:
        listbox.insert(END,i)
        #đưa list sv vào listbox
def sort():
    sv=read()
    for i in range(len(sv)):
        for j in range(len(sv)):
            x,y = sv[i],sv[j]
            if x[2]>y[2]:
                sv[i],sv[j] = y,x
    listbox.delete(0,END)
    for i in sv:
        listbox.insert(END,i)
    
root = Tk()

#gọi biến:
id=StringVar()
name=StringVar()
year=StringVar()

root.title('Quản lý sinh viên')
Label(root, text='Ứng dụng quản lý sinh viên', fg='red', font=('cambria', 16), width=20).grid(row=0)
listbox = Listbox(root,width=80, height=20)
listbox.grid(row=1,columnspan=2)

label_MSV = Label(root, text='Mã Sinh viên:')
label_MSV.grid(row=2, column=0)
Entry(root,width=40, textvariable=id).grid(row=2,column=1)

label_name= Label(root, text='Tên Sinh viên:')
label_name.grid(row=3, column=0)
Entry(root,width=40, textvariable=name).grid(row=3,column=1)

label_year = Label(root, text='Năm sinh:')
label_year.grid(row=4, column=0)
Entry(root,width=40, textvariable=year).grid(row=4,column=1)

button = Frame(root)
Button(button,text='Thêm', command=add).pack(side=LEFT)
Button(button,text='Xem').pack(side=LEFT)
Button(button,text='Sắp xếp', command=sort).pack(side=LEFT)
Button(button,text='Thoát', command=root.quit).pack(side=LEFT)
button.grid(row=5,column=1)

root.mainloop()
