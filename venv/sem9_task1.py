#1) реализовать дескрипторы для любых двух классов
class NonNegative:

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class StringValidation:


    def __set__(self, instance, value):
        if isinstance(value, str) == False:
            raise ValueError('Аргумент может быть только строкой! Попробуйте иное значение')
        instance.__dict__[self.my_attr] = value
    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

class My_class:
    wage = NonNegative()
    bonus = NonNegative()
    def __init__(self, wage, bonus):
        self.wage = wage
        self.bonus = bonus

    def __add__(self, other):
        self.wage + other.bonus

    def income(self, wage, bonus):
        total_income = wage + bonus
        return total_income

class Position(My_class):
    name = StringValidation()
    surname = StringValidation()
    position = StringValidation()
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
    def get_full_name(self, name, surname, position):
        print(f'Сотрудник: {name} {surname}, должность: {position} ')

worker = Position(name = '', surname = '', position = '')
worker.name = 'Майя'
worker.surname = 'Матвеева'
worker.position = 'продавец'
worker.get_full_name(worker.name, worker.surname, worker.position)

salary = My_class(wage = 0, bonus = 0)
salary.wage = int(input('Введите оклад:'))
salary.bonus = int(input('Введите бонусную часть:'))
salary = My_class(salary.wage, salary.bonus)

print(f'Заработная плата сотрудника равна: {salary.income(salary.wage, salary.bonus)} рублей')