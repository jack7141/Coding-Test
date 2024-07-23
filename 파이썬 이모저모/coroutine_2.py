import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(1)
    print("Data fetched")
    return "Some data"

async def main():
    data = await fetch_data()
    print(f"Received: {data}")



asyncio.run(main())

