import math

class Figure:
    __sides = []
    __color = []
    filled: bool = False

    def __init__(self, color, *sides) -> None:
        self.set_color(*color)
        self.set_sides(*sides)

    def get_color(self) -> list:
        return self.__color
    
    def __is_valid_color(self, r:int, g: int, b: int) -> bool:
        return r >= 0 and r <= 255 and g >= 0 and g <= 255 and b >= 0 and b <= 255
    
    def set_color(self, r:int, g: int, b: int) -> None:
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides) -> bool:
        count = 0;
        for side in sides:
            if side < 0:
                return False
            count += 1
        if count != self.sides_count:
            return False
        return True
    
    def get_sides(self) -> list:
        return self.__sides
    
    def __len__(self) -> int:
        area = 0
        for side in self.__sides:
            area += side
        return side
    
    def set_sides(self, *new_sides) -> None:
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
    

class Circle(Figure):
    sides_count = 1

    def __radius(self) -> float:
        return self.__sides[0] / (2*math.pi)
    
    def get_square(self) -> float:
        return math.pi * (self.__radius() ** 2)
    

class Triangle(Figure):
    sides_count = 3
    def get_square(self) -> float:
        p = len(self) / 2
        result = 0
        for side in self.__sides:
            result *= p - side
        return math.sqrt(p * result)
    

class Cube(Figure):
    sides_count = 12
    
    def __init__(self, color, *sides) -> None:
        sides = [sides[0]] * 12
        super().__init__(color, *sides)
        
    def get_volume(self) -> float:
        return self.get_sides()[0] ** 3
    
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())