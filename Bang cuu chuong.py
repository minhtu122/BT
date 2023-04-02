n = int(input('Nhập n: '))
m = int(input('Nhập m: '))
for i in range (1,11,1):
    for j in range (n,m+1,1):
        print (f'{j}*{i}={i*j}', end='\t')
    print('')
