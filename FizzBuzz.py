text = input('Nhập số: ')
num = text.split()
num1 = int(num[0])
num2 = int(num[1])
if num1>num2:
    print ('Nhập lại num2>num1')
else:
    for i in num:
        if (int(i)%3==0 and int(i)%5==0):
            print ('FizzBuzz')
        elif int(i)%3==0:
            print ('Fizz')
        elif int(i)%5==0:
            print ('Buzz')
        else:
            print (i)
