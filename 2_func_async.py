import time
import asyncio


async def func1(x):
    print(x ** 2)
    await asyncio.sleep(3) # запрос удаленному серверу
    print("func1 finished/сервер ответил")


async def func2(x):
    print(x ** 0.5)
    await asyncio.sleep(3)
    print("func2 finished")


async def main():
    task1 = asyncio.create_task(func1(4))
    task2 = asyncio.create_task(func2(4))

    print(type(task1))
    print(task1.__class__.__bases__)

    await task1
    await task2


if __name__ == '__main__':
    print(time.strftime('%X'))
    asyncio.run(main())
    print(time.strftime('%X'))
    print(12 * "-+-")
    print(type(func1)) # функция
    print(type(func1(3))) # корутина

