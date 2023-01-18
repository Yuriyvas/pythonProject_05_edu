import math
from functools import reduce


import my_calc


# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.

def square(a):

    return print(a*4, a*a, a*(math.sqrt(2)))

square(int(input('Введите размер стороны квадрата: ')))


# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer
def my_dict(**kwargs):
    for k, v in kwargs.items():
        red="\033[31m{}".format
        blue="\033[34m{}".format
        reset = "\033[0m{}".format('')
        print(red(f'{k}:'), (blue(f'{v}:')), reset)


my_dict(last_name='Popov', name='Max', age=40, position='web developer')

#
# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа
my_list = [20, -3, 15, 2, -1, -21]
print(list(filter(lambda x: x > 0, my_list)))
print(reduce(lambda x, y: x*y, my_list))


#
# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
# 4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.

print(my_calc.my_sum(6,7))
print(my_calc.my_minus(6,7))
print(my_calc.my_umn(6,7))
print(my_calc.my_stepen(6,7))