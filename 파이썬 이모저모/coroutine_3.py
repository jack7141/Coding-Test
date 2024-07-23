import asyncio
import aiohttp


async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        urls = [
            "http://example.com",
            "http://example.org",
            "http://example.net",
        ]
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

        for result in results:
            print(result)


# 코루틴 실행
asyncio.run(main())