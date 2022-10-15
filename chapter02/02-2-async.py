import time
import asyncio


async def delivery(name, mealtime):
    print(f"{name}에게 배달 완료!")
    await asyncio.sleep(mealtime)
    print(f"{name} 식사 완료, {mealtime}시간 소요...")
    print(f"{name} 그룻 수거 완료")


async def main():
    await asyncio.gather(
        delivery("A", 10), delivery("B", 3), delivery("C", 4),
    )

    """
    await delivery("A", 3)
    await delivery("B", 3)
    await delivery("C", 3)
    동기방식
    """


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)