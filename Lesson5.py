# Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
#     - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания значений этого атрибута
#     нужно использовать методы get и set
class Automobile:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def runing(self):
            return 'Wrum-Wrum'

class Bus(Automobile):
    def __init__(self, brand, model, year, sits, __color,__fuel):
        super().__init__(brand, model, year)
        self.sits = sits
        self.__color = __color
        self.__fuel = __fuel

    def runing(self):
            return 'Tr-tr-tr'
    def refeul(self, newfuel):
        self.__fuel = newfuel


camry70 = Automobile('Toyota', '70', 2020)
print(camry70.runing())

hiace = Bus('Toyota', 'hiace', 2015, 16, 'blue', 'gasoline')
print(hiace.__dict__)
try:
    print(hiace.__fuel)
except AttributeError: print('No fuel')

hiace.__fuel = 'Oil'
print(hiace.__fuel)
print(hiace.__dict__)

Bus.refeul(Bus, 'Mazut')
print(hiace.__dict__)

couster = Bus('Toyota', 'couster', 2015, 16, 'blue', 'gasoline')
print(couster.__dict__)