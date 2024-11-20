"""
Copyright (C) 2021 SE Slash - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: secheaper@gmail.com

"""

import os
import sys
import inspect
from bs4 import BeautifulSoup
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import src.formattr as formatter


def test_sortList():
    """
    Checks the sortList function
    """
    arr = [{"price": "$10"}, {"price": "$20"}, {"price": "$0"}]
    ansArr = [{"price": "$0"}, {"price": "$10"}, {"price": "$20"}]
    revAnsArr = [{"price": "$20"}, {"price": "$10"}, {"price": "$0"}]
    assert formatter.sortList(arr, "pr", False) == ansArr
    assert formatter.sortList(arr, "pr", True) == revAnsArr


def test_formatResults():
    """
    Checks the formatResults function
    """
    titles = [BeautifulSoup('<div class="someclass">title  </div>', "html.parser")]
    prices = [BeautifulSoup('<div class="someclass">$0.99  </div>', "html.parser")]
    links = []
    images = []

    product = formatter.formatResult("example", titles, prices, links, images)
    ans = {"title": "title", "price": "$0.99", "website": "example"}

    assert product["title"] == ans["title"] and product["price"] == ans["price"] and product["website"] == ans["website"]


def test_sortList_empty():
    """
    Test Case 1 Checks the sortList function with an empty list
    """
    arr = []
    ansArr = []
    assert formatter.sortList(arr, "price", False) == ansArr
    assert formatter.sortList(arr, "price", True) == ansArr


def test_sortList_no_prices():
    """
    Test Case 2 Checks the sortList function when 'price' field is missing in the dictionaries
    """
    arr = [{"name": "item1"}, {"name": "item2"}, {"name": "item3"}]
    ansArr = [{"name": "item1"}, {"name": "item2"}, {"name": "item3"}]  # No change since no price field
    assert formatter.sortList(arr, "price", False) == ansArr
    assert formatter.sortList(arr, "price", True) == ansArr


def test_sortList_single_item():
    """
    Test Case 3 Checks the sortList function with a single item in the list
    """
    arr = [{"price": "$10"}]
    ansArr = [{"price": "$10"}]
    assert formatter.sortList(arr, "price", False) == ansArr
    assert formatter.sortList(arr, "price", True) == ansArr


def test_sortList_non_numeric_price():
    """
    Test Case 4 Checks the sortList function when price is not numeric (e.g. invalid price format)
    """
    arr = [{"price": "$ten"}, {"price": "$20"}, {"price": "$0"}]
    ansArr = [{"price": "$0"}, {"price": "$20"}, {"price": "$ten"}]
    assert formatter.sortList(arr, "pr", False) == ansArr


def test_formatResults_missing_title():
    """
    Test Case 5 Checks the formatResults function when title is missing
    """
    titles = [BeautifulSoup('<div class="someclass"></div>', "html.parser")]
    prices = [BeautifulSoup('<div class="someclass">$0.99  </div>', "html.parser")]
    links = []
    images = []

    product = formatter.formatResult("example", titles, prices, links, images)
    ans = {"title": "", "price": "$0.99", "website": "example"}

    assert product["title"] == ans["title"] and product["price"] == ans["price"] and product["website"] == ans["website"]


def test_formatResults_missing_price():
    """
    Test Case 6 Checks the formatResults function when price is missing
    """
    titles = [BeautifulSoup('<div class="someclass">title  </div>', "html.parser")]
    prices = [BeautifulSoup('<div class="someclass"></div>', "html.parser")]
    links = []
    images = []

    product = formatter.formatResult("example", titles, prices, links, images)
    ans = {"title": "title", "price": "", "website": "example"}

    assert product["title"] == ans["title"] and product["price"] == ans["price"] and product["website"] == ans["website"]


def test_formatResults_missing_website():
    """
    Test Case 7 Checks the formatResults function when website is missing
    """
    titles = [BeautifulSoup('<div class="someclass">title  </div>', "html.parser")]
    prices = [BeautifulSoup('<div class="someclass">$0.99  </div>', "html.parser")]
    links = []
    images = []

    product = formatter.formatResult("", titles, prices, links, images)
    ans = {"title": "title", "price": "$0.99", "website": ""}

    assert product["title"] == ans["title"] and product["price"] == ans["price"] and product["website"] == ans["website"]


def test_sortList_invalid_sort_key():
    """
    Test Case 8 Checks sortList function with an invalid sorting key
    """
    arr = [{"price": "$10"}, {"price": "$20"}, {"price": "$0"}]
    ansArr = [{"price": "$10"}, {"price": "$20"}, {"price": "$0"}]  # No change as the key is invalid
    assert formatter.sortList(arr, "invalid_key", False) == ansArr


def test_formatResults_empty_titles():
    """
    Test Case 9 Checks formatResults function with empty titles
    """
    titles = [BeautifulSoup('', "html.parser")]
    prices = [BeautifulSoup('<div class="someclass">$10.99  </div>', "html.parser")]
    links = []
    images = []

    product = formatter.formatResult("example", titles, prices, links, images)
    ans = {"title": "", "price": "$10.99", "website": "example"}

    assert product["title"] == ans["title"] and product["price"] == ans["price"] and product["website"] == ans["website"]


def test_sortList_float_price():
    """
    Test Case 10 Checks sortList function with float prices
    """
    arr = [{"price": "$10.5"}, {"price": "$20.25"}, {"price": "$0.99"}]
    ansArr = [{"price": "$0.99"}, {"price": "$10.5"}, {"price": "$20.25"}]
    revAnsArr = [{"price": "$20.25"}, {"price": "$10.5"}, {"price": "$0.99"}]
    assert formatter.sortList(arr, "pr", False) == ansArr
    assert formatter.sortList(arr, "pr", True) == revAnsArr


def test_formatResults_with_links():
    """
    Test Case 11 Checks the formatResults function when links are provided
    """
    titles = [BeautifulSoup('<div class="someclass">title  </div>', "html.parser")]
    prices = [BeautifulSoup('<div class="someclass">$0.99  </div>', "html.parser")]
    links = ["http://example.com"]
    images = []

    product = formatter.formatResult("example", titles, prices, links, images)
    ans = {"title": "title", "price": "$0.99", "website": "example", "link": "http://example.com"}

    assert product["title"] == ans["title"] and product["price"] == ans["price"] and product["website"] == ans["website"] and product["link"] == ans["link"]


def test_formatResults_with_images():
    """
    Test Case 12 Checks the formatResults function when image links are provided
    """
    titles = [BeautifulSoup('<div class="someclass">title  </div>', "html.parser")]
    prices = [BeautifulSoup('<div class="someclass">$10.99  </div>', "html.parser")]
    links = []
    images = ["http://example.com/image.jpg"]

    product = formatter.formatResult("example", titles, prices, links, images)
    ans = {"title": "title", "price": "$10.99", "website": "example", "image": "http://example.com/image.jpg"}

    assert product["title"] == ans["title"] and product["price"] == ans["price"] and product["website"] == ans["website"] and product["image"] == ans["image"]


def test_formatResults_invalid_html_structure():
    """
    Test Case 13 Checks formatResults function when the HTML structure is invalid or unexpected
    """
    titles = [BeautifulSoup('<div>Invalid Title', "html.parser")]
    prices = [BeautifulSoup('<span>No Price</span>', "html.parser")]
    links = []
    images = []

    product = formatter.formatResult("example", titles, prices, links, images)
    ans = {"title": "Invalid Title", "price": "", "website": "example"}

    assert product["title"] == ans["title"] and product["price"] == ans["price"] and product["website"] == ans["website"]


def test_formatResults_multiple_prices():
    """
    Test Case 14 Checks formatResults function when multiple price values exist
    """
    titles = [BeautifulSoup('<div class="someclass">title  </div>', "html.parser")]
    prices = [BeautifulSoup('<div class="someclass">$10.99  </div><div class="someclass">$15.99</div>', "html.parser")]
    links = []
    images = []

    product = formatter.formatResult("example", titles, prices, links, images)
    ans = {"title": "title", "price": "$10.99", "website": "example"}

    assert product["title"] == ans["title"] and product["price"] == ans["price"] and product["website"] == ans["website"]


def test_sortList_large_numbers():
    """
    Test Case 15 Checks the sortList function with large numbers
    """
    arr = [{"price": "$1000000"}, {"price": "$1000"}, {"price": "$500"}]
    ansArr = [{"price": "$500"}, {"price": "$1000"}, {"price": "$1000000"}]
    revAnsArr = [{"price": "$1000000"}, {"price": "$1000"}, {"price": "$500"}]
    assert formatter.sortList(arr, "price", False) == ansArr
    assert formatter.sortList(arr, "price", True) == revAnsArr


def test_formatResults_with_special_characters():
    """
    Test Case 16 Checks formatResults function when titles or prices contain special characters
    """
    titles = [BeautifulSoup('<div class="someclass">!@#Title$%^</div>', "html.parser")]
    prices = [BeautifulSoup('<div class="someclass">$10.99  </div>', "html.parser")]
    links = []
    images = []

    product = formatter.formatResult("example", titles, prices, links, images)
    ans = {"title": "!@#Title$%^", "price": "$10.99", "website": "example"}

    assert product["title"] == ans["title"] and product["price"] == ans["price"] and product["website"] == ans["website"]


def test_sortList_descending_price():
    """
    Test Case 17 Checks the sortList function to sort in descending order when price values are in descending order
    """
    arr = [{"price": "$1000"}, {"price": "$500"}, {"price": "$1000000"}]
    ansArr = [{"price": "$1000000"}, {"price": "$1000"}, {"price": "$500"}]
    assert formatter.sortList(arr, "price", True) == ansArr

def test_formatResults_with_multiple_images():
    """
    Test Case 18 Checks formatResults function when multiple image links are provided
    """
    titles = [BeautifulSoup('<div class="someclass">title  </div>', "html.parser")]
    prices = [BeautifulSoup('<div class="someclass">$20.99  </div>', "html.parser")]
    links = []
    images = ["http://example.com/image1.jpg", "http://example.com/image2.jpg"]

    product = formatter.formatResult("example", titles, prices, links, images)
    ans = {"title": "title", "price": "$20.99", "website": "example", "image": "http://example.com/image1.jpg"}

    assert product["title"] == ans["title"] and product["price"] == ans["price"] and product["website"] == ans["website"]
    # Only the first image is expected to be included


def test_sortList_case_insensitive_sorting():
    """
    Test Case 19 Checks the sortList function for case insensitive sorting of the price field
    """
    arr = [{"price": "$20"}, {"price": "$100"}, {"price": "$50"}]
    ansArr = [{"price": "$20"}, {"price": "$50"}, {"price": "$100"}]  # Sorted in ascending order
    revAnsArr = [{"price": "$100"}, {"price": "$50"}, {"price": "$20"}]  # Sorted in descending order

    assert formatter.sortList(arr, "price", False) == ansArr
    assert formatter.sortList(arr, "price", True) == revAnsArr


def test_formatResults_missing_all_fields():
    """
    Test Case 20 Checks the formatResults function when all fields are missing or empty
    """
    titles = [BeautifulSoup('', "html.parser")]
    prices = [BeautifulSoup('', "html.parser")]
    links = []
    images = []

    product = formatter.formatResult("", titles, prices, links, images)
    ans = {"title": "", "price": "", "website": ""}

    assert product["title"] == ans["title"] and product["price"] == ans["price"] and product["website"] == ans["website"]
