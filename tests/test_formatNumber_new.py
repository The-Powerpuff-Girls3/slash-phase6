import os
import sys
import inspect
import math
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import src.formattr as formatter


def test_getNumbers_special_chars():
    """Checks getNumbers with special characters surrounding the number"""
    assert formatter.getNumbers("### $15.75 !!!") == 15.75
    assert formatter.getNumbers("@@ $$12.50 %%") == 12.50


def test_getNumbers_no_numeric_value():
    """Checks getNumbers with text but no numeric value"""
    assert formatter.getNumbers("Price is $") == math.inf


def test_getNumbers_large_number():
    """Checks getNumbers with a large dollar amount"""
    assert formatter.getNumbers("Cost is $1000000.99") == 1000000.99


def test_getNumbers_decimal_without_zero():
    """Checks getNumbers with a decimal amount lacking leading zero"""
    assert formatter.getNumbers("Amount is $.99") == 0.99


def test_getNumbers_no_spaces():
    """Checks getNumbers with no spaces between text and dollar amount"""
    assert formatter.getNumbers("Amount:$25.50") == 25.50
