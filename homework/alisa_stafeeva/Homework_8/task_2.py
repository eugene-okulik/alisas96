def progression():
    num_1 = 0
    num_2 = 1
    count = 2
    while True:
        yield num_2
        num_1, num_2 = num_2, num_1 + num_2
        count += 1


targets = [5, 200, 1000, 100000]
count = 1

for number in progression():
    if count in targets:
        print(number)
    if count > 100000:
        break
    count +=1
