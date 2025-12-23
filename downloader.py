import asyncio
import aiofiles

from aiohttp import ClientSession


async def download_file(url: str, filename: str, session: ClientSession):
    async with session.get(url) as response:
        response.raise_for_status()
        content = await response.read()
        async with aiofiles.open(filename, 'wb') as f:
            await f.write(content)


async def download_all(urls: list[str]) -> list[str]:
    async with ClientSession() as session:
        tasks = []
        filenames = []

        for i, url in enumerate(urls, start=1):
            filename = f'file_{i}.json'
            filenames.append(filename)
            tasks.append(download_file(url, filename, session))

        await asyncio.gather(*tasks)
        return filenames
