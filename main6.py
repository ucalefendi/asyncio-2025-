import asyncio


async def set_future_result(future,value):
    await asyncio.sleep(2)
    future.set_result(value)
    print(f"set future relut value {value}")
    



async def main():
    loop = asyncio.get_running_loop()
    future = loop.create_future()
    

    asyncio.create_task(set_future_result(future,"Future result is ready"))


    result = await future
    print(F'Futures resilt {result}')


asyncio.run(main())
