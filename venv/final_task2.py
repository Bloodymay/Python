"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""
my_list = ['class', 'function', 'method']
my_bytes_list = [b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0',
                 b'\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82',
                 b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80']
for i in my_list:
    print(f'Тип переменной: {type(i)}')
    print(f'Содержимое переменной: {i}')
    print(f'Длина переменной: {len(i)}')

for i in my_bytes_list:
    print(f'Тип переменной: {type(i)}')
    print(f'Содержимое переменной: {i}')
    print(f'Длина переменной: {len(i)}')




