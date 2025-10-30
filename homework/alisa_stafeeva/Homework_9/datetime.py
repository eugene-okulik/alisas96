import datetime

my_date = 'Jan 15, 2023 - 12:05:33'

python_date = datetime.datetime.strptime(my_date, '%b %d, %Y - %H:%M:%S')
human_date = datetime.datetime.strftime(python_date, '%d.%m.%Y, %H:%M')
human_month = datetime.datetime.strftime(python_date, '%B')

print(human_month)
print(human_date)
