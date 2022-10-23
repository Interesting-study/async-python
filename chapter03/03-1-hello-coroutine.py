import asyncio
from datetime import time


async def hello_world():
    print("hello world")
    return 123


async def delivery(name, mealtime):
    print(f"{name}에게 배달 완료!")
    await asyncio.sleep(mealtime)
    print(f"{name} 식사 완료, {mealtime}시간 소요...")
    print(f"{name} 그룻 수거 완료")


async def main():
    task1 = asyncio.create_task(delivery("A", 2))
    task2 = asyncio.create_task(delivery("B", 1))

    await task1
    await task2

    await delivery("A", 2)


if __name__ == "__main__":
    # asyncio.run(hello_world())
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)
