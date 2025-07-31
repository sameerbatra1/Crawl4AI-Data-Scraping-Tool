import re
import sys
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlResult
from scrapper import basic_crawl

if __name__ == "__main__":
    raw_markdown = asyncio.run(basic_crawl("https://psychology.columbian.gwu.edu/ms-applied-psychology"))
    print(raw_markdown)
