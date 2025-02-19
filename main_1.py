import asyncio


async def fetch_data(delay):
    print("Fetching data ....")
    await asyncio.sleep(delay)
    print("data fetched")
    return {"data_1":"1"}




async def main():
    print("Start of main coroutine....")
    task = fetch_data(2)
    print("end of main coroutine")
    result = await task
    print(f"Received result :{result}")


asyncio.run(main())    
# asyncio.run(fetch_data(5))    