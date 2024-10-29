import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from src.main_streamlit import search_items_API

def test_api_walmart_minimal_title_length():
    """Assert that each title has a minimum length of 3 characters"""
    product = 'laptop'
    site = 'wm'
    results = search_items_API(site, product)
    for item in results:
        assert len(item['title']) >= 3

def test_api_walmart_price_without_special_chars():
    """Assert that prices do not contain characters other than digits and decimal point after dollar sign"""
    product = 'laptop'
    site = 'wm'
    results = search_items_API(site, product)
    for item in results:
        price = item['price'].replace('$', '')
        assert price.replace('.', '').isdigit()


def test_api_walmart_price_greater_than_zero():
    """Assert that each price is greater than zero"""
    product = 'laptop'
    site = 'wm'
    results = search_items_API(site, product)
    for item in results:
        price = float(item['price'].replace('$', ''))
        assert price > 0

def test_api_walmart_unique_img_links():
    """Assert that all img_links are unique"""
    product = 'laptop'
    site = 'wm'
    results = search_items_API(site, product)
    img_links = [item['img_link'] for item in results]
    assert len(img_links) == len(set(img_links))

def test_api_walmart_price_no_trailing_zero():
    """Assert that prices do not have trailing zeros beyond two decimal places"""
    product = 'laptop'
    site = 'wm'
    results = search_items_API(site, product)
    for item in results:
        price = item['price'].replace('$', '')
        if '.' in price:
            assert len(price.split('.')[1]) <= 2

def test_api_walmart_link_does_not_end_with_slash():
    """Assert that each item link does not end with a trailing slash"""
    product = 'laptop'
    site = 'wm'
    results = search_items_API(site, product)
    for item in results:
        assert not item['link'].endswith('/')

def test_api_walmart_all_titles_not_empty():
    """Assert that no title is an empty string"""
    product = 'laptop'
    site = 'wm'
    results = search_items_API(site, product)
    for item in results:
        assert item['title'] != ""

def test_api_walmart_price_is_positive_float():
    """Assert that each price is a positive float"""
    product = 'laptop'
    site = 'wm'
    results = search_items_API(site, product)
    for item in results:
        price = float(item['price'].replace('$', ''))
        assert isinstance(price, float) and price > 0

def test_api_walmart_img_link_has_valid_prefix():
    """Assert that img_link starts with 'http://' or 'https://'"""
    product = 'laptop'
    site = 'wm'
    results = search_items_API(site, product)
    for item in results:
        img_link = item['img_link']
        assert img_link.startswith('http://') or img_link.startswith('https://')


def test_api_walmart_titles_unique():
    """Assert that all item titles are unique"""
    product = 'laptop'
    site = 'wm'
    results = search_items_API(site, product)
    titles = [item['title'] for item in results]
    assert len(titles) == len(set(titles))

def test_api_walmart_non_zero_prices():
    """Assert that no price is zero"""
    product = 'laptop'
    site = 'wm'
    results = search_items_API(site, product)
    for item in results:
        price = float(item['price'].replace('$', ''))
        assert price != 0

def test_api_walmart_valid_currency_format():
    """Assert that prices follow the currency format '$X.XX'"""
    product = 'laptop'
    site = 'wm'
    results = search_items_API(site, product)
    for item in results:
        price = item['price']
        assert price.startswith('$') and len(price.split('.')[1]) == 2

def test_api_walmart_valid_title_content():
    """Assert that each title contains letters or numbers"""
    product = 'laptop'
    site = 'wm'
    results = search_items_API(site, product)
    for item in results:
        title = item['title']
        assert any(char.isalnum() for char in title)

def test_api_walmart_img_links_unique():
    """Assert that all img_links are unique"""
    product = 'laptop'
    site = 'wm'
    results = search_items_API(site, product)
    img_links = [item['img_link'] for item in results]
    assert len(img_links) == len(set(img_links))
