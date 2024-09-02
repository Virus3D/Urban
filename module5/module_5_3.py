import sys

class House:
    def __init__(self, name, number_of_floors) -> None:
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor) -> None:
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
            return
        for floor in range(1, new_floor+1):
            print(floor)
    def __len__(self) -> int:
        return self.number_of_floors
    def __str__(self) -> str:
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, House):
            raise BaseException('Правый операнд должен быть типом House')
        return self.number_of_floors == other.number_of_floors
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, House):
            raise BaseException('Правый операнд должен быть типом House')
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other: object) -> bool:
        if not isinstance(other, House):
            raise BaseException('Правый операнд должен быть типом House')
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other: object) -> bool:
        if not isinstance(other, House):
            raise BaseException('Правый операнд должен быть типом House')
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other: object) -> bool:
        if not isinstance(other, House):
            raise BaseException('Правый операнд должен быть типом House')
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other: object) -> bool:
        if not isinstance(other, House):
            raise BaseException('Правый операнд должен быть типом House')
        return self.number_of_floors != other.number_of_floors
    def __add__(self, value: int) -> object:
        if not isinstance(value, int):
            raise ArithmeticError("Правый операнд должен быть типом int")
        self.number_of_floors += value
        return self
    def __radd__(self, value: int) -> object:
        if not isinstance(value, int):
            raise ArithmeticError("Левый операнд должен быть типом int")
        return self.__add__(value)
    def __iadd__(self, value: int) -> object:
        if not isinstance(value, int):
            raise ArithmeticError("Правый операнд должен быть типом int")
        return self.__add__(value)
    

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__