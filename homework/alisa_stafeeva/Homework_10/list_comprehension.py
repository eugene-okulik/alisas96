PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

PRICE_LIST = PRICE_LIST.split()
prices = list(filter(lambda x: PRICE_LIST.index(x) % 2 != 0, PRICE_LIST))
prices = list(map(lambda x: int(x.strip('р')), prices))
words = list(filter(lambda x: PRICE_LIST.index(x) % 2 == 0, PRICE_LIST))

print(dict(zip(words, prices)))
