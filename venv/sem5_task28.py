"""
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

*Пример:*

2 2
    4
"""
from timeit import timeit

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
if a >= 0 and b >= 0:
    def sum_function(a, b):

        if a == 0:
            return b
        return sum_function(a-1, b+1)
    print(timeit("sum_function(a, b)", globals=globals()))
    print(f"Сумма чисел '{a}' и '{b}' равно: {sum_function(a, b)}")

else: print("Вы ввели отрицательное число. Введите другое. ")




