"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
my_list = ['разработка', 'администрирование', 'protocol', 'standart']
my_encoded_list = []
my_decoded_list = []
for i in my_list:
    a = i.encode('utf-8')
    my_encoded_list.append(a)
print(f'Байтовый формат: {my_encoded_list}')
for i in my_encoded_list:
    b = i.decode('utf-8')
    my_decoded_list.append(b)
print(f'Обратно преобразованный список: {my_decoded_list}')
