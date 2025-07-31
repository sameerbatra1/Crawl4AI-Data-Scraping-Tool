import re
import sys
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlResult
from scrapper import run_crawler_sync
import streamlit as st

# if __name__ == "__main__":
# raw_markdown = asyncio.run(run_crawler_sync())
# print(raw_markdown)
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
st.set_page_config(page_title="🕸️ Web Scraper with Crawl4AI", layout="wide")
st.title("🕸️ Web Scraper UI")

default_url = "https://my.gwu.edu/mod/pws/subjects.cfm?campId=1&termId=202503"
url_input = st.text_input("Enter URL to scrape:", value=default_url)
if st.button("Run Crawl"):
    with st.spinner("Scraping in progress..."):
        # try:
        markdown_result = run_crawler_sync(url_input)
# print(markdown_result)
        st.success("Scraping Complete!")
        st.markdown(markdown_result, unsafe_allow_html=True)
        # except Exception as e:
        #     st.error(f"⚠️ Error: {e}")