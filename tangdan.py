x = int(input('nhập số thứ 1: '))
y = int(input('nhập số thứ 2: '))
z = int(input('nhập số thứ 3: '))
gia = ''
if y<x and y<z:
    gia = x
    x = y
    y = gia
elif z<x and z<y:
    gia = x
    x = z
    z = gia
if z<y:
    gia = y
    y = z
    z = gia
print ('Dãy số tăng dần : ', x, y,z)
