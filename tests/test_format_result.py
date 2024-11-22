import pytest
from datetime import datetime
import os
import sys
import inspect
import unittest
from unittest.mock import patch

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from src.formattr import formatResult


class TestFormatResult(unittest.TestCase):
    @patch('src.formattr.datetime')
    def test_format_result_general(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 11, 21, 10, 0, 0)

        website = "amazon"
        titles = [MockElement("Product Title")]
        prices = "$19.99"
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
            "rating": 4,
        }

        self.assertEqual(result, expected)

    @patch('src.formattr.datetime')
    def test_format_result_no_title(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 11, 21, 10, 0, 0)

        website = "ebay"
        titles = []
        prices = "$49.99"
        links = [{"href": "/product-link"}]
        img_link = [{"src": "http://image-link.com"}]
        rating = 3

        result = formatResult(website, titles, prices, links, img_link, rating)

        expected = {
            "timestamp": "21/11/2024 10:00:00",
            "title": "",
            "price": "$49.99",
            "link": "www.ebay.com/product-link",
            "img_link": "http://image-link.com",
            "website": "ebay",
            "rating": 3,
        }

        self.assertEqual(result, expected)

    @patch('src.formattr.datetime')
    def test_format_result_no_img_link(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 11, 21, 10, 0, 0)

        website = "walmart"
        titles = [MockElement("Walmart Product")]
        prices = "$29.99"
        links = [{"href": "/product-link"}]
        img_link = []  # No image link
        rating = 5

        result = formatResult(website, titles, prices, links, img_link, rating)

        expected = {
            "timestamp": "21/11/2024 10:00:00",
            "title": "Walmart Product",
            "price": "$29.99",  # Correct price value
            "link": "www.walmart.com/product-link",
            "img_link": "",  # Empty image link
            "website": "walmart",
            "rating": 5,
        }

        self.assertEqual(result, expected)

    @patch('src.formattr.datetime')
    def test_format_result_no_price(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 11, 21, 10, 0, 0)

        website = "costco"
        titles = [MockElement("Costco Product")]
        prices = []  # No price
        links = [{"href": "/product-link"}]
        img_link = [{"src": "http://image-link.com"}]
        rating = 4

        result = formatResult(website, titles, prices, links, img_link, rating)

        expected = {
            "timestamp": "21/11/2024 10:00:00",
            "title": "Costco Product",
            "price": "",  # Empty price
            "link": '/product-link',
            "img_link": "http://image-link.com",
            "website": "costco",
            "rating": 4,
        }

        self.assertEqual(result, expected)

    @patch('src.formattr.datetime')
    def test_format_result_no_link(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 11, 21, 10, 0, 0)

        website = "amazon"
        titles = [MockElement("Amazon Product")]
        prices = "$15.99"
        links = []  # No link
        img_link = [{"src": "http://image-link.com"}]
        rating = 2

        result = formatResult(website, titles, prices, links, img_link, rating)

        expected = {
            "timestamp": "21/11/2024 10:00:00",
            "title": "Amazon Product",
            "price": "$15.99",  # Correct price value
            "link": "www.amazon.com",  # Default link for missing href
            "img_link": "http://image-link.com",
            "website": "amazon",
            "rating": 2,  # No +1 here
        }

        self.assertEqual(result, expected)

    @patch('src.formattr.datetime')
    def test_format_result_missing_values(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 11, 21, 10, 0, 0)

        website = "ebay"
        titles = []  # No title
        prices = "$49.99"
        links = []  # No link
        img_link = []  # No image link
        rating = 1

        result = formatResult(website, titles, prices, links, img_link, rating)

        expected = {
            "timestamp": "21/11/2024 10:00:00",
            "title": "",  # No title
            "price": "$49.99",  # Correct price value
            "link": "www.ebay.com",  # Default link for missing href
            "img_link": "",  # Empty image link
            "website": "ebay",
            "rating": 1,  # No +1 here
        }

        self.assertEqual(result, expected)

    # Additional test cases for various scenarios can follow the same structure
    # Example of testing for specific websites:
    
    @patch('src.formattr.datetime')
    def test_format_result_walmart_link_https(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 11, 21, 10, 0, 0)

        website = "walmart"
        titles = [MockElement("Walmart Product")]
        prices = "$29.99"
        links = [{"href": "https://walmart.com/product"}]  # Full URL
        img_link = [{"src": "http://walmart-image.com"}]
        rating = 3

        result = formatResult(website, titles, prices, links, img_link, rating)

        expected = {
            "timestamp": "21/11/2024 10:00:00",
            "title": "Walmart Product",
            "price": "$29.99",  # Correct price value
            "link": "https://walmart.com/product",  # Keep full URL for Walmart
            "img_link": "http://walmart-image.com",
            "website": "walmart",
            "rating": 3,  # No +1 here
        }

        self.assertEqual(result, expected)

    @patch('src.formattr.datetime')
    def test_format_result_empty_prices(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 11, 21, 10, 0, 0)

        website = "bestbuy"
        titles = [MockElement("Best Buy Product")]
        prices = []  # No price
        links = [{"href": "/product-link"}]
        img_link = [{"src": "http://image-link.com"}]
        rating = 5

        result = formatResult(website, titles, prices, links, img_link, rating)

        expected = {
            "timestamp": "21/11/2024 10:00:00",
            "title": "Best Buy Product",
            "price": "",  # Empty price
            "link": "www.bestbuy.com/product-link",
            "img_link": "http://image-link.com",
            "website": "bestbuy",
            "rating": 5,
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
