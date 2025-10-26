import random

salary = int(input('Enter salary: '))
bonus = random.randrange(1, 1000001)

if random.choice([True, False]):
    print(f'{salary}, True - "${salary + bonus}"')
else:
    print(f'{salary}, False - "${salary}"')
