import aiohttp
import asyncio
import json
import time

start = time.time()


async def posts_data(i, session):
    url = f'https://jsonplaceholder.typicode.com/posts/{i}'
    async with session.get(url) as response:
        post = await response.json()
        with open('data.json', 'a') as f:
            json.dump(post, f)
            f.write(',')


async def main():
    with open('data.json', 'a') as f:
        f.write('[')

    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1,78):
            tasks.append(posts_data(i, session))
        await asyncio.gather(*tasks)

    with open('data.json', 'rb+') as f:
        f.seek(-1, 2)
        f.truncate()
        f.write(b']')


asyncio.run(main())

end = time.time()
runtime = end - start
print(runtime)