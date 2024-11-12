import time
import asyncio


async def start_strongman(name, power):
    balls = 5
    balls_number = 0
    print(f'Силач {name} начал соревнования.')
    while balls > 0:
        await asyncio.sleep(1 / power)
        balls -= 1
        balls_number += 1
        print(f'Силач {name} поднял шар №{balls_number}')
        if balls == 0:
            print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3


start = time.time()
asyncio.run(start_tournament())
finish = time.time()
print(f'Совернование длилось {round(finish - start, 2)} мин.')