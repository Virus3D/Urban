import asyncio

async def start_strongman(name: str, power: int):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep(10/power)
        print(f'Силач {name} поднял {i} шар.')
    print(f'Силач {name} закончил соревнование.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Василий', 2))
    task2 = asyncio.create_task(start_strongman('Вася', 3))
    task3 = asyncio.create_task(start_strongman('Петя', 4))

    await asyncio.gather(task1, task2, task3)

asyncio.run(start_tournament())