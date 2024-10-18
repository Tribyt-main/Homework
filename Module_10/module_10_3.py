from threading import Thread, Lock
from random import randint
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        self.balance = 0
        dep = randint(50, 500)
        self.balance += dep
        time.sleep(0.01)
        print(f'Баланс пополнился на {dep},\n'
              f'Текущий баланс {self.balance}')
        if self.balance >= 500 or self.lock.locked():
            self.lock.release()

    def take(self):
        take = randint(50, 500)
        print(f'Запрос на {take}')
        if self.balance >= take:
            self.balance -= take
            print(f'Снятие: {take}. Баланс: {self.balance}".')
        else:
            print(f'Запрос отклонён, недостаточно средств')
            self.lock.acquire()


bk = Bank()


def main():
    th1 = Thread(target=Bank.deposit, args=(bk,))
    th2 = Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    print(f'Итоговый баланс: {bk.balance}')


for i in range(100):
    main()
