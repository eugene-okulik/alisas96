string_1 = 'результат операции: 42'
string_2 ='результат операции: 514'
string_3 = 'результат работы программы: 9'
string_1_index = string_1.index(':') + 2
string_2_index = string_2.index(':') + 2
string_3_index = string_3.index(':') + 2
print(int(string_1[string_1_index:]) + 10)
print(int(string_2[string_2_index:]) + 10)
print(int(string_3[string_3_index:]) + 10)
