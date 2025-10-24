number = 7
guess = int(input('Угадайте число:\n'))
while guess != number:
    guess = int(input('Попробуйте еще раз:\n'))
print('Поздравляю! Вы угадали!')
