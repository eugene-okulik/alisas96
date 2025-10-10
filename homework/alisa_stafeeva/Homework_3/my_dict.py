my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [1, 2, 3, 4, 5],
    'dict': {1: 1, 2: 2, 3: 3, 4: 4, 5: 5},
    'set': {1, 2, 3, 4, 5},
}

print(my_dict['tuple'][-1])

my_dict['list'].append(6)
my_dict['list'].pop(1)

my_dict['dict'][('i am a tuple',)] = 6
my_dict['dict'].pop(1)

my_dict['set'].add(6)
my_dict['set'].pop()

print(my_dict)
