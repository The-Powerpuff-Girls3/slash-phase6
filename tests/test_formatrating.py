import pytest
from datetime import datetime
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from src.formattr import formatResult  # 确保导入的是函数而不是模块

def formatTitle(title):
    return title.strip()

def test_formatResult():
    website = "walmart"
    titles = [type('obj', (object,), {'get_text': lambda: "Test Product"})()]
    prices = "$19.99"
    links = [type('obj', (object,), {'href': "/test-product"})()]
    img_link = [type('obj', (object,), {'src': "http://example.com/image.jpg"})()]
    rating = "4.5"

    result = formatResult(website, titles, prices, links, img_link, rating)

    assert result['title'] == "Test Product"
    assert result['price'] == "$19.99"
    assert result['link'] == "www.walmart.com/test-product"
    assert result['img_link'] == "http://example.com/image.jpg"
    assert result['website'] == "walmart"
    assert result['rating'] == "4.5"
    assert 'timestamp' in result

def test_formatResult_no_titles():
    website = "walmart"
    titles = []
    prices = "$19.99"
    links = [type('obj', (object,), {'href': "/test-product"})()]
    img_link = [type('obj', (object,), {'src': "http://example.com/image.jpg"})()]
    rating = "4.5"

    result = formatResult(website, titles, prices, links, img_link, rating)

    assert result['title'] == ""
    assert result['price'] == "$19.99"
    assert result['link'] == "www.walmart.com/test-product"
    assert result['img_link'] == "http://example.com/image.jpg"
    assert result['website'] == "walmart"
    assert result['rating'] == "4.5"
    assert 'timestamp' in result

def test_formatResult_no_prices():
    website = "walmart"
    titles = [type('obj', (object,), {'get_text': lambda: "Test Product"})()]
    prices = ""
    links = [type('obj', (object,), {'href': "/test-product"})()]
    img_link = [type('obj', (object,), {'src': "http://example.com/image.jpg"})()]
    rating = "4.5"

    result = formatResult(website, titles, prices, links, img_link, rating)

    assert result['title'] == "Test Product"
    assert result['price'] == ""
    assert result['link'] == "www.walmart.com/test-product"
    assert result['img_link'] == "http://example.com/image.jpg"
    assert result['website'] == "walmart"
    assert result['rating'] == "4.5"
    assert 'timestamp' in result

def test_formatResult_no_links():
    website = "walmart"
    titles = [type('obj', (object,), {'get_text': lambda: "Test Product"})()]
    prices = "$19.99"
    links = []
    img_link = [type('obj', (object,), {'src': "http://example.com/image.jpg"})()]
    rating = "4.5"

    result = formatResult(website, titles, prices, links, img_link, rating)

    assert result['title'] == "Test Product"
    assert result['price'] == "$19.99"
    assert result['link'] == ""
    assert result['img_link'] == "http://example.com/image.jpg"
    assert result['website'] == "walmart"
    assert result['rating'] == "4.5"
    assert 'timestamp' in result

def test_formatResult_no_img_link():
    website = "walmart"
    titles = [type('obj', (object,), {'get_text': lambda: "Test Product"})()]
    prices = "$19.99"
    links = [type('obj', (object,), {'href': "/test-product"})()]
    img_link = []
    rating = "4.5"

    result = formatResult(website, titles, prices, links, img_link, rating)

    assert result['title'] == "Test Product"
    assert result['price'] == "$19.99"
    assert result['link'] == "www.walmart.com/test-product"
    assert result['img_link'] == ""
    assert result['website'] == "walmart"
    assert result['rating'] == "4.5"
    assert 'timestamp' in result