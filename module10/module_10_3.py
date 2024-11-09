
from random import randint
from threading import Thread, Lock
from time import sleep

lock = Lock()


class Bank:
    def __init__(self):
        self.balance = 0 # начальный баланс
        

    def deposit(self):
        transaction = 100
        while transaction:
            trans = randint(50, 500)
            self.balance += trans
            if (self.balance >= 500 and lock.locked()):
                lock.release()
            print(f'Пополнение: {trans}. Баланс: {self.balance}')
            sleep(0.01)
            transaction -= 1
        
    def take(self):
        transaction = 100
        while transaction:
            trans = randint(50, 500)
            print(f'Запрос на {trans}')
            if (self.balance >= trans):
                self.balance -= trans
                print(f'Снятие: {trans}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                lock.acquire()
            sleep(0.01)
            transaction -= 1
                

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
