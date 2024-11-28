import aiohttp
import asyncio
import time

async def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()
        
async def main():
    start_time = time.time()
    results = await asyncio.gather(*(fetch_users() for _ in range(5)))
    users = results[0]
    
    names = [user['name'] for user in users]
    emails = [user['email'] for user in users]
    usernames = [user['username'] for user in users]

    print(names)
    print(emails)
    print(usernames)

    end_time = time.time()
    print(f"Vrijeme izvodenja programa je {end_time - start_time}")

if __name__ == "__main__":
    asyncio.run(main())