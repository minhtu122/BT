input_str = input('Your string: ')
def count_chart(txt):
    result = 0
    for char in txt:
        result += 1
    return result
print ('Length: ', count_chart(input_str))
