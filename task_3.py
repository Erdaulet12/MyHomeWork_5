"""task_3.py"""

import time
import asyncio
import aiohttp


# код подсмотрел, но вроде понял


class Downloader:
    """downloader class"""
    async def fetch_url(self, url):
        """fetch url method

        Args:
            url (_type_): URL

        Returns:
            _type_: information
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()

    async def fetch_all_urls(self, urls):
        """fetch all urls

        Args:
            urls (_type_): URL

        Returns:
            _type_: information
        """
        start_time = time.time()
        tasks = [self.fetch_url(url) for url in urls]
        results = await asyncio.gather(*tasks)
        end_time = time.time()
        print(f"Время выполнения синхронного кода: {end_time - start_time}")
        return results


if __name__ == "__main__":

    downloader = Downloader()

    # Синхронный запуск
    urls = ["https://google.com", "https://yahoo.com", "https://bing.com"] * 33
    results = downloader.fetch_all_urls(urls)

    # Асинхронный запуск
    async def main():
        """main method"""
        start_time = time.time()
        tasks = [downloader.fetch_url(url) for url in urls]
        results = await asyncio.gather(*tasks)
        end_time = time.time()
        print(f"Время выполнения асинхронного кода: {end_time - start_time}")

    asyncio.run(main())
