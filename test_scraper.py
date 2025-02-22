#!/usr/bin/python3
"""A unittest module for testing the ebay scraper"""
import jsoni
import unittest
from unittest.mock import patch

from scrape import scrape_ebay, save_to_json, save_to_csv

MOCK_SCRAPE_DATA = [
    {
        "name": "Mock Laptop",
        "price": 500.0,
        "url": "http://example.com/mock-laptop",
        "rating": "4.5",
    },
    {
        "name": "Mock Phone",
        "price": 300.0,
        "url": "http://example.com/mock-phone",
        "rating": None,
    },
]


class TestEbayScraper(unittest.TestCase):
    """All test cases for scrape_ebay module"""
    @patch("scrape.scrape_ebay", return_value=MOCK_SCRAPE_DATA)
    def test_scrape_ebay(self, mock_scraper):
        """Test scrape_ebay function using mocked data"""
        results = scrape_ebay("laptop", max_products=5)
        self.assertEqual(results, MOCK_SCRAPE_DATA)
        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)

        for product in results:
            self.assertIn("name", product)
            self.assertIn("price", product)
            self.assertIn("url", product)
            self.assertIsInstance(product["name"], str)
            self.assertIsInstance(product["url"], str)
            self.assertTrue(
                isinstance(product["price"],
                           float) or product["price"] is None)

    def test_save_to_json(self):
        """Tests save_to_json function"""
        save_to_json(MOCK_SCRAPE_DATA, "test.json")
        with open("test.json", "r", encoding="utf-8") as f:
            loaded_data = json.load(f)
        self.assertEqual(loaded_data, MOCK_SCRAPE_DATA)

    def test_save_to_csv(self):
        """Tests save_to_csv function"""
        save_to_csv(MOCK_SCRAPE_DATA, "test.csv")
        with open("test.csv", "r", encoding="utf-8") as f:
            lines = f.readlines()
        self.assertGreater(len(lines), 1)  # Header + 2 rows


if __name__ == "__main__":
    unittest.main()
