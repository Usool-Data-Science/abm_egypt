import json
import unittest

from scrape import scrape_ebay, save_to_json, save_to_csv


class TestEbayScraper(unittest.TestCase):
    def test_scrape_ebay(self):
        results = scrape_ebay("laptop", max_products=5)
        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)
        for product in results:
            self.assertIn("name", product)
            self.assertIn("price", product)
            self.assertIn("url", product)
            self.assertIsInstance(product["name"], str)
            self.assertIsInstance(product["url"], str)
            self.assertTrue(
                isinstance(product["price"], float
                           ) or product["price"] is None)

    def test_save_to_json(self):
        test_data = [
            {"name": "Test Product",
             "price": 10.0,
             "url": "http://example.com",
             "rating": None}]
        save_to_json(test_data, "test.json")
        with open("test.json", "r", encoding="utf-8") as f:
            loaded_data = json.load(f)
        self.assertEqual(loaded_data, test_data)

    def test_save_to_csv(self):
        test_data = [
            {"name": "Test Product",
             "price": 10.0,
             "url": "http://example.com",
             "rating": None}]
        save_to_csv(test_data, "test.csv")
        with open("test.csv", "r", encoding="utf-8") as f:
            lines = f.readlines()
        self.assertGreater(len(lines), 1)  # Header + 1 row
