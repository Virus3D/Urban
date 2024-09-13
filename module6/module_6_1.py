class Plant:
    edible = False
    name = ''
    def __init__(self, name:str) -> None:
        self.name = name

class Animal:
    alive = True
    fed = False
    name = ''
    def __init__(self, name:str) -> None:
        self.name = name
    def eat(self, food:Plant)  -> None:
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False
    
class Mammal(Animal):
    def about(self):
        print("I am Mammal")

class Predator(Animal):
    def about(self):
        print("I am Predator")

class Flower(Plant):
    def about(self):
        print("I am Flower")

class Fruit(Plant):
    edible = True
    def about(self):
        print("I am Fruit")

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)