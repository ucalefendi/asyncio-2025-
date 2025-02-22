import asyncio


async def fetch_data(id,sleep_time):
    print(f"Coroutine {id} starting to fetch data")
    await asyncio.sleep(sleep_time)
    return {"id":id,"DATA": f"Sample data from coroutine {id}"}


async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i,sleep_time in enumerate([2,1,3],start=1):
            task = tg.create_task(fetch_data(i,sleep_time))
            tasks.append(task)

        results = [task.result for task in tasks]    


    for result in results:
        print(f"received result {result}")   


asyncio.run(main())         