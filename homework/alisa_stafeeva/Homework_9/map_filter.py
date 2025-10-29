temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
    22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]

hot_temperatures = list(filter(lambda x: x > 28, temperatures))
average_temperatures = sum(hot_temperatures) / len(hot_temperatures)

print(max(hot_temperatures))
print(min(hot_temperatures))
print(average_temperatures)
