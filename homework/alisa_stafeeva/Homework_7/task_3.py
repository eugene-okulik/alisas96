string_1 = 'результат операции: 42'
string_2 = 'результат операции: 54'
string_3 = 'результат работы программы: 209'
string_4 = 'результат: 2'

def get_number(string):
    return int(string.split()[-1]) + 10
    
print(get_number(string_1))
print(get_number(string_2))
print(get_number(string_3))
print(get_number(string_4))
