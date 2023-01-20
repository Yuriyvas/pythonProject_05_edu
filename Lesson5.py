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
    def __init__(self, brand, model, year, sits):
        super().__init__(brand, model, year)
        self.sits = sits
    def runing(self):
            return 'Tr-tr-tr'

camry70 = Automobile('Toyota', '70', 2020)
print(camry70.runing())

hiace = Bus('Toyota', 'hiace', 2015, 16)
print(hiace.__dict__)
