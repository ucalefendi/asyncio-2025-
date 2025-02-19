import asyncio



async def fetch_data(delay,id):
    print("Fetching data...id.",id)
    await asyncio.sleep(delay)
    print("data fetched ,id:",id)
    return {"data": "data1","id":id}


async def main():
    
    task1 = fetch_data(2,1)
    task2 = fetch_data(2,5)
    

    result1 = await task1
    print(f"recieved results: {result1}")

    result2 = await task2
    print(f"recieved results: {result2}")



asyncio.run(main())
asyncio.run(fetch_data(4,5))





