n = int(input('Введите длину шоколадки:'))
m = int(input('Введите ширину шоколадки:'))
k = int(input('Введите количество долек:'))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('Можно')
else:
    print('Нельзя')
