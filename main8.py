import asyncio


async def access_resource(semaphore,recource_id):
    async with semaphore:
        print(f"Accessing resource {recource_id}")
        await asyncio.sleep(5)
        print(f"Releasing resource {recource_id}")



async def main():
    semaphore = asyncio.Semaphore(2)  
    await asyncio.gather(*(access_resource(semaphore,i) for i in range(5))) 


asyncio.run(main())         

