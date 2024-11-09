from threading import Thread, Lock
from random import randint
from time import sleep
from queue import Queue


class Table:
    def __init__(self, number:int):
        self.number = number
        self.guest = None
        

class Guest(Thread):
    def __init__(self, name:str):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3,10))


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()
    
    def guest_arrival(self, *guests):
        for guest in guests:
            free_table = next((table for table in self.tables if table.guest is None), None)
            if free_table:
                free_table.guest = guest
                print(f'{guest.name} сел(-а) за стол номер {free_table.number}')
                guest.start()
            else:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None:
                    if not table.guest.is_alive():
                        print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {table.number} свободен")
                        table.guest = None
                    else:
                        continue

                # Если очередь не пуста
                if not self.queue.empty():
                    guest_from_queue = self.queue.get()
                    table.guest = guest_from_queue
                    print(f"{guest_from_queue.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                    guest_from_queue.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()