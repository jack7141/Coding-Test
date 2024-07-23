import asyncio
import aiohttp


async def fetch_data_from_api_1():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://jsonplaceholder.typicode.com/posts/1") as response:
            return await response.json()

async def fetch_data_from_api_2():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://jsonplaceholder.typicode.com/posts/2") as response:
            return await response.json()

async def async_api():
    task1 = asyncio.create_task(fetch_data_from_api_1())
    task2 = asyncio.create_task(fetch_data_from_api_2())
    data1 = await task1
    data2 = await task2
    return {"data1": data1, "data2": data2}

# 코루틴 실행
a = asyncio.run(async_api())
print(a)