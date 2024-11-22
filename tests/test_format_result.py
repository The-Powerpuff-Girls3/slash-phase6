import pytest
from datetime import datetime
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from src.formattr import formatResult  

import unittest
from unittest.mock import patch

class TestFormatResult(unittest.TestCase):
    @patch('your_module.datetime')  # Mock datetime to ensure consistent timestamps
    def test_format_result_general(self, mock_datetime):
        # Mock current datetime
        mock_datetime.now.return_value = datetime(2024, 11, 21, 10, 0, 0)
        
        website = "amazon"
        titles = [MockElement("Product Title")]
        prices = [MockElement("$19.99")]
        links = [{"href": "/product-link"}]
        img_link = [{"src": "http://image-link.com"}]
        rating = 4

        result = formatResult(website, titles, prices, links, img_link, rating)

        expected = {
            "timestamp": "21/11/2024 10:00:00",
            "title": "Product Title",
            "price": "$19.99",
            "link": "www.amazon.com/product-link",
            "img_link": "http://image-link.com",
            "website": "amazon",
            "rating": 5  # rating + 1
        }

        self.assertEqual(result, expected)

    def test_format_result_walmart(self):
        website = "walmart"
        titles = [MockElement("Walmart Product")]
        prices = "$29.99"
        links = [{"href": "http://walmart.com/product"}]
        img_link = [{"src": "http://walmart-image.com"}]
        rating = 3

        result = formatResult(website, titles, prices, links, img_link, rating)

        expected = {
            "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "title": "Walmart Product",
            "price": "$29.99",
            "link": "http://walmart.com/product",
            "img_link": "http://walmart-image.com",
            "website": "walmart",
            "rating": 4
        }

        self.assertEqual(result, expected)

    def test_format_result_missing_values(self):
        website = "ebay"
        titles = []
        prices = "$49.99"
        links = []
        img_link = []
        rating = 2

        result = formatResult(website, titles, prices, links, img_link, rating)

        expected = {
            "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "title": "",
            "price": "$49.99",
            "link": "www.ebay.com",
            "img_link": "",
            "website": "ebay",
            "rating": 3
        }

        self.assertEqual(result, expected)

class MockElement:
    """
    Mock class to simulate elements with get_text and attributes.
    """
    def __init__(self, text):
        self.text = text

    def get_text(self):
        return self.text

if __name__ == "__main__":
    unittest.main()