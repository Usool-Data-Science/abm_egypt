#!/usr/bin/python3
"""Scrapes ebay platform for object in the search query e.g. Laptop"""

import time
import json
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


def setup_driver():
    """Initialize and return a Selenium WebDriver instance."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options)
    return driver


def scroll_to_bottom(driver):
    """Scroll to the bottom of the page to load more products."""
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  # Wait for content to load
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def scrape_ebay(search_query, max_products=50):
    """Scrape product listings from eBay based on the search query."""
    url = f"https://www.ebay.com/sch/i.html?_nkw={search_query}"
    driver = setup_driver()
    driver.get(url)
    scroll_to_bottom(driver)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    products = []
    listings = soup.find_all("li", class_="s-item")

    for item in listings[:max_products]:
        try:
            name = item.find("h3", class_="s-item__title").text.strip()
            price = item.find(
                "span", class_="s-item__price"
                ).text.strip().replace("$", "").replace(",", "")
            link = item.find("a", class_="s-item__link")["href"]
            rating_tag = item.find("div", class_="x-star-rating")
            rating = rating_tag.text.strip() if rating_tag else "N/A"

            products.append({
                "name": name,
                "price": float(
                    price) if price.replace(
                        '.', '', 1).isdigit() else None,
                "url": link,
                "rating": rating if rating != "N/A" else None
            })
        except AttributeError:
            continue

    return products


def save_to_json(data, filename="ebay_products.json"):
    """Save scraped data to a JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def save_to_csv(data, filename="ebay_products.csv"):
    """Save scraped data to a CSV file."""
    keys = data[0].keys() if data else []
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    query = "laptop"
    results = scrape_ebay(query)
    save_to_json(results)
    save_to_csv(results)
    print(f"Scraped {len(results)} products from eBay.")
