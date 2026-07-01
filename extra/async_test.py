import asyncio
import time


async def greet():
    print("Hello")


async def make_coffee():
    print(f"[{time.strftime('%X')}] Starting the coffee machine...")
    await asyncio.sleep(4)  # It's a cooperative pause
    await greet()
    print(f"[{time.strftime('%X')}] Coffee is ready!")


async def brew(name, sec):
    print(f"{name}: brew started!")
    await asyncio.sleep(sec)
    print(f"{name}: Done!")
    return f"{name} ready"


async def main():
    task1 = asyncio.create_task(brew("Tea", 2))
    task2 = asyncio.create_task(brew("Coffee", 3))
    res1 = await task1
    res2 = await task2
    print(res1, res2)

    results = await asyncio.gather(
        brew("Idly", 3), brew("Sambar", 4), brew("Espresso", 5)
    )

    print(results)


async def main_wrong():
    res1 = await brew("Tea", 2)
    res2 = await brew("Coffee", 3)
    print(res1, res2)


asyncio.run(main())
