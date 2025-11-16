import os
import datetime


base_path = os.path.dirname(__file__)
homework_path  = os.path.dirname(os.path.dirname(base_path))
okulik_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')
print(okulik_file_path)


def read_file():
    with open(okulik_file_path, 'r', encoding='utf-8') as okulik_file:
        for line in okulik_file.readlines():
            yield line


def date_list():
    new_list = []
    for data_line in read_file():
        data_line = data_line[3:]
        data_line = data_line.split(' - ')
        data_line.pop()
        data_str = data_line[0]
        new_list.append(data_str)
    return new_list


def date_format(my_date):
    return datetime.datetime.fromisoformat(my_date)


date1, date2, date3 = date_list()

new_date1 = date_format(date1)
new_date2 = date_format(date2)
new_date3 = date_format(date3)
time_now = datetime.datetime.now()

print(new_date1 + datetime.timedelta(days=7))
print(new_date2.weekday())
print((time_now - new_date3).days)
