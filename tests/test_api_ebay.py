# -*- coding: utf-8 -*-
"""
Created on Tue Oct. 01 17:17:17 2024

@author: Sen Fng
"""
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from src.main_streamlit import search_items_API


def check_price(price):
    # Removes the dollar sign and commas from the price string and converts it to a float
    # Returns True if conversion is successful, False if it raises a ValueError (indicating invalid format)
    price = price.replace('$', '').replace(',', '')
    try:
        price = float(price)
        return True
    except ValueError:
        return False


def test_api_ebay():
    # Verifies that the search_items_API function returns a result (non-None) when querying 'lenovo' on eBay ('eb')
    product = 'lenovo'
    site = 'eb'
    results = search_items_API(site, product)
    assert results is not None


def test_api_ebay1():
    # Checks that the search_items_API function returns a non-empty list of results for 'lenovo' from eBay
    product = 'lenovo'
    site = 'eb'
    results = search_items_API(site, product)
    assert len(results) > 0


def test_api_ebay2():
    # Ensures that the specified number of results (9) is returned by search_items_API for 'lenovo' from eBay
    product = 'lenovo'
    site = 'eb'
    num = 9
    results = search_items_API(site, product, listLengthInd=num)
    assert len(results) == num


def test_api_ebay3():
    # Confirms that the results returned by search_items_API are in list format
    product = 'lenovo'
    site = 'eb'
    results = search_items_API(site, product)
    assert isinstance(results, list)


def test_api_ebay4():
    # Checks that each item in the result list is a dictionary
    product = 'lenovo'
    site = 'eb'
    results = search_items_API(site, product)
    assert isinstance(results[0], dict)


def test_api_ebay5():
    # Verifies that each result dictionary contains a 'price' key
    product = 'lenovo'
    site = 'eb'
    results = search_items_API(site, product)
    for result in results:
        assert 'price' in result


def test_api_ebay6():
    # Ensures that each result dictionary contains a 'link' key
    product = 'lenovo'
    site = 'eb'
    results = search_items_API(site, product)
    for result in results:
        assert 'link' in result


def test_api_ebay7():
    # Verifies that each result dictionary contains an 'img_link' key for the product image URL
    product = 'lenovo'
    site = 'eb'
    results = search_items_API(site, product)
    for result in results:
        assert 'img_link' in result


def test_api_ebay8():
    # Confirms that each result dictionary includes a 'title' key
    product = 'lenovo'
    site = 'eb'
    results = search_items_API(site, product)
    for result in results:
        assert 'title' in result


def test_api_ebay9():
    # Checks that each result dictionary contains a 'timestamp' key
    product = 'lenovo'
    site = 'eb'
    results = search_items_API(site, product)
    for result in results:
        assert 'timestamp' in result


def test_api_ebay_collected_produce_price():
    # Validates that each result's 'price' field has a valid numeric format
    product = 'lenovo'
    site = 'eb'
    results = search_items_API(site, product)
    prices = [result['price'] for result in results]

    for price in prices:
        assert check_price(price)


def test_api_ebay_collected_produce_title():
    # Ensures that each result's 'title' field is not an empty string
    product = 'lenovo'
    site = 'eb'
    results = search_items_API(site, product)
    titles = [result['title'] for result in results]

    for title in titles:
        assert title != ''


def test_api_ebay_collected_produce_link():
    # Verifies that each result's 'link' field is a valid URL starting with 'http', 'https', or 'www'
    product = 'lenovo'
    site = 'eb'
    results = search_items_API(site, product)
    links = [result['link'] for result in results]

    for link in links:
        # assert is a link
        assert link.startswith('http') or link.startswith('https') or link.startswith('www')


def test_api_ebay_collected_produce_img_link():
    # Ensures that each result's 'img_link' field is a valid URL starting with 'http', 'https', or 'www'
    product = 'lenovo'
    site = 'eb'
    results = search_items_API(site, product)
    img_links = [result['img_link'] for result in results]

    for img_link in img_links:
        # assert is a link
        assert img_link.startswith('http') or img_link.startswith('https') or img_link.startswith('www')


def test_api_ebay_collected_produce_timestamp():
    # Confirms that each result's 'timestamp' field is not an empty string
    product = 'lenovo'
    site = 'eb'
    results = search_items_API(site, product)
    timestamps = [result['timestamp'] for result in results]

    for timestamp in timestamps:
        assert timestamp != ''
