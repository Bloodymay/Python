'''
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
'''
my_list = input('Введите список чисел через пробел: ').split(' ')
my_int_list = list(map(int, my_list))
min_value = int(input('Введите заданный минимум для поиска: '))
max_value = int(input('Введите заданный максимум для поиска: '))
index_list = list()
for index, i in enumerate(my_int_list):
    if i >= min_value and i <= max_value:
        index_list.append((index, i))

print(f'Значения в заданном диапазоне в формате индекс-значение: {index_list}')