import asyncio


async def fetch_data(id,sleep_time):
    print(f"Coroutine {id} starting to fetch data")
    await asyncio.sleep(sleep_time)
    return {"id":id,"DATA": f"Sample data from coroutine {id}"}



async def main():
    results = await asyncio.gather(fetch_data(1,2),fetch_data(5,6),fetch_data(7,8))

    for relut in results:
        print(f"Recieved result {relut}")

    print(results)


asyncio.run(main())        

