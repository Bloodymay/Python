'''
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх
одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
'''
ins_num = int(input())
tail = 0
head = 0
for i in range(ins_num):

    if head == 0:
        tail += 1
else:
    head += 1
if head > tail:
    print(tail)
else:
    print(head)