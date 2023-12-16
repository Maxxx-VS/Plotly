from die import Die

# создаем кубик
die = Die()
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# анализ результатов
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)