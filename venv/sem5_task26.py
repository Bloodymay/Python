"""
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
"""


from timeit import timeit

a = int(input('Введите число: '))
b = int(input('Введите степень, в которую вы хотите его возвести: '))

def pow_function(a, b):
    if b == 0:
        return 1
    return a * pow_function(a, b - 1)

print(timeit("pow_function(a, b)", globals=globals()))
print(f"Число '{a}' в степени '{b}' равно: {pow_function(a, b)}")