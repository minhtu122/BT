n = int(input('Số phần tử nhập vào: '))
numbers = []
for i in range(1,n+1):
    num = input()
    numbers.append(num)
print('Chuỗi gồm: ', numbers)
min = int(numbers[0])
for nu in numbers:
    if int(min) > int(nu):
        min = nu
print ('Số nhỏ nhất là: ',min)
    
