# Import libraries
import os
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout
import time
import asyncio

SEASONS = list(range(2014,2023))
DATA_DIR = "data"
STANDINGS_DIR = os.path.join(DATA_DIR, "standings")
SCORES_DIR = os.path.join(STANDINGS_DIR, "scores")

async def get_html(url, selector, sleep=5, retries=3):
    html = None
    # Delayed retires to prevent throttling
    for i in range(1, retries+1):
        time.sleep(sleep * i)

        try:
            async with async_playwright () as p:
                browser = await p.chromium.launch()
                page = await browser.new_page()
                await page.goto(url)
                print(await page.title())
                html = await page.inner_html(selector)
        except PlaywrightTimeout:
            print(f"Timeout error on {url}")
            continue
        else:
            break
    return html
# Scraping the box scores 
season = 2017
url = f"https://www.basketball-reference.com/leagues/NBA_{season}_games.html"
html = asyncio.run(get_html(url, "#content .filter"))
print(html)

# Scrape NBA Standings with playwright

# Parsing NBA standings with BeautifulSoup

# Parsing box score links with BeautifulSoup

# Downloading box scores with playwright

# Parsing box scores with beautifulsoup

# Reading the line score with pandas

# Reading stats tables with pandas

# Getting stats ready for machine learning
