import re
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlResult

async def basic_crawl(url: str) -> str:
    async with AsyncWebCrawler() as crawler:
        results: list[CrawlResult] = await crawler.arun(url=url)
        for result in results:
            if result.success:
                return result.markdown.raw_markdown
    return "❌ No successful result found." 

def run_crawler_sync(url: str) -> str:
    return asyncio.run(basic_crawl(url))