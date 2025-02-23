import asyncio


database = 0


lock = asyncio.Lock()


async def modify_shared_resource():
    global database
    async with lock:
        print(f"Resource before modification: {database}")
        database += 1
        await asyncio.sleep(5)
        print(f"After modification resource: {database}")


async def main():
    await asyncio.gather(*(modify_shared_resource() for _ in range(5)))  




asyncio.run(main())

