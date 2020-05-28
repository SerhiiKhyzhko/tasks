import asyncio
from aiohttp import ClientSession
from time import time


async def request(url):
    session = ClientSession()
    local_start = time()
    async with session.get(url) as req:
        print(f"Resource '{url}', request took {time() - local_start:.3f}, response status - {req.status}")
    await session.close()

urls = [
    "http://docs.python-requests.org/",
    "https://httpbin.org/get",
    "https://httpbin.org/",
    "https://api.github.com/",
    "https://example.com/",
    "https://www.python.org/",
    "https://www.google.com.ua/",
    "https://regex101.com/",
    "https://docs.python.org/3/this-url-will-404.html",
    "https://www.nytimes.com/guides/",
    "https://www.mediamatters.org/",
    "https://1.1.1.1/",
    "https://www.politico.com/tipsheets/morning-money",
    "https://www.bloomberg.com/markets/economics",
    "https://www.ietf.org/rfc/rfc2616.txt"
]

futures = [request(url) for url in urls]
loop = asyncio.get_event_loop()
start = time()
loop.run_until_complete(asyncio.wait(futures))
print(f"Full fetching got {time() - start:.3f} seconds.")
