# Homework


print("3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3")

my_list = ['a', 'b', [1, 2, 3], 'd']
print(my_list[2][0])
print(my_list[2][1])
print(my_list[2][2])

# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'

list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
print(sum(filter(lambda x: isinstance(x, int), list_1)))
print([x for x in list_1 if isinstance(x, str) and 'a' in x])


# 3.3. Превратите лист ['cat', 'dog', 'horse, 'cow'] в кортеж
list_3 = ['cat', 'dog', 'horse', 'cow']
tuple_3=tuple(list_3)
print(tuple_3)
print(type(tuple_3))

#
# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')

family_1 = list(input('Enter names of first family over ",": ').split(','))
family_2 = list(input('Enter names of second family over ",": ').split(','))
print(family_1)
print(type(family_1))
print(family_2)
print(type(family_2))
if len(family_1) > len(family_2):
    print('First family is bigger')
elif len(family_2) > len(family_1):
    print('Second family is bigger')
else: print('Families is equal')


# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение
dict_home_alone={
    "title": 'Home Alone',
    'director':'Silvestor Stolone',
    'year': 2000,
    'budget': 1500,
    'main_actor': 'Ben Aflick',
    'slogan': "I'l be back"
}
print(type(dict_home_alone))
print(dict_home_alone.values())
print(dict_home_alone.items())


# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
#
# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
#
# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга
#
