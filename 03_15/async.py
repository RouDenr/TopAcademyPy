import asyncio

async def do_something():
    print("Hi!")
    await asyncio.sleep(3)
    print("Bay!")

async def do_good():
    print("Im Good!")
    await asyncio.sleep(2)
    print("I done((")

async def do_bad():
    print("Im Bad!")
    await asyncio.sleep(1)
    print("Im GONE!!")

loop = asyncio.get_event_loop()

# for i in range(0, 10):
#     loop.create_task(do_something())

loop.create_task(do_something())
loop.create_task(do_bad())
loop.create_task(do_good())

loop.run_until_complete(asyncio.gather(do_something()))
