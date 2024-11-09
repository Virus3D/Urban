from time import sleep
from threading import Thread

class Knight(Thread):
    def __init__(self, name:str, power:int) -> None:
        super().__init__()
        self.name = name
        self.power = power
        
    def run(self) -> None:
        print(f'{self.name}, на нас напали!')
        day = 0
        Enemy = 100
        while Enemy:
            day += 1
            Enemy -= self.power
            sleep(1)
            print(f'{self.name} сражается {day} день(дня)..., осталось {Enemy} воинов.')
            
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')
                

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились!')