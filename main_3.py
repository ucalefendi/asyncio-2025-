import asyncio




async def fetch_data(id,delay):
    print(f"Coroutine {id} starting to fetch data")
    await asyncio.sleep(delay)
    return {"id":id,"DATA": f"Sample data from coroutine {id}"}



async def main():

    task1 =  asyncio.create_task(fetch_data(1,2))
    task2 =  asyncio.create_task(fetch_data(3,4))
    task3 =  asyncio.create_task(fetch_data(5,6))


    result1 = await task1
    result2 = await task2
    result3 = await task3

    print("---->>>",result1,"---->>>",result2,"---->>>",result3)


asyncio.run(main())    