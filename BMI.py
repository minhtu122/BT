h= float(input('Chiều cao= '))
w= float(input('Cân nặng = '))
bmi = w/(h*2)
if bmi<16:
    print ('Gầy cấp độ III ')
elif bmi<17:
    print ('Gầy cấp độ II ')
elif bmi<18.5:
    print ('Gầy cấp độ I ')
elif bmi<25:
    print ('Bình thường ')
elif bmi<30:
    print ('Thừa cân ')
elif bmi<35:
    print ('Béo phì cấp độ I ')
elif bmi<40:
    print ('Béo phì cấp độ II ')
else:
    print ('Béo phì cấp độ III ')
