num = float(input('Số tiền đã chi: '))
if num<75:
    total = num
elif num<100:
    total = num-15
elif num<150:
    total = num-25
else:
    total = num-50
print ('Tổng tiền mà người đó thanh toán là: ',total)
