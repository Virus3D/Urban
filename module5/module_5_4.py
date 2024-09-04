import sys

class House:
    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors) -> None:
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def is_house(other: object) -> None:
        if not isinstance(other, House):
            raise BaseException('Правый операнд должен быть типом House')

    def is_int(value, pref: str) -> None:
        if not isinstance(value, int):
            raise ArithmeticError(pref, "операнд должен быть типом int")

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
        self.is_house(other)
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other: object) -> bool:
        self.is_house(other)
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other: object) -> bool:
        self.is_house(other)
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other: object) -> bool:
        self.is_house(other)
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other: object) -> bool:
        self.is_house(other)
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other: object) -> bool:
        self.is_house(other)
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value) -> object:
        self.is_int(value, 'Правый')
        self.number_of_floors += value
        return self

    def __radd__(self, value) -> object:
        self.is_int(value, 'Левый')
        return self.__add__(value)

    def __iadd__(self, value) -> object:
        self.is_int(value, 'Правый')
        return self.__add__(value)
    

hh1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)