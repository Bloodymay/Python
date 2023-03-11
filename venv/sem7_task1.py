"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

import time
import colorama
from colorama import Fore, Style

class TrafficLight:
    __color1 = 'red'
    __color2 = 'yellow'
    __color3 = 'green'

a = TrafficLight()

def running(self, *args):
    print(Fore.RED + a._TrafficLight__color1)
    time.sleep(7)
    print(Fore.YELLOW + a._TrafficLight__color2)
    time.sleep(2)
    print(Fore.GREEN + a._TrafficLight__color3)
    time.sleep(10)
    print(Style.RESET_ALL + 'Done!')

print(running(a._TrafficLight__color1, a._TrafficLight__color2, a._TrafficLight__color3))