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


def test_getNumbers_no_dollar_sign():
    """Checks getNumbers with a number but no dollar sign"""
    assert formatter.getNumbers("Price 19.99") == 19.99


def test_getNumbers_only_cents():
    """Checks getNumbers with only cents and no dollar sign"""
    assert formatter.getNumbers("Amount: 0.99") == 0.99


def test_getNumbers_multiple_dollars():
    """Checks getNumbers with multiple dollar signs"""
    assert formatter.getNumbers("Amount: $$$25.75") == 25.75


def test_getNumbers_spaces_in_between():
    """Checks getNumbers with spaces around the number"""
    assert formatter.getNumbers("The cost is $ 50.99 ") == 50.99


def test_getNumbers_edge_case_empty_string():
    """Checks getNumbers with an empty string"""
    assert formatter.getNumbers("") == math.inf


def test_getNumbers_large_decimal():
    """Checks getNumbers with a large decimal number"""
    assert formatter.getNumbers("Price is $1234567.89") == 1234567.89


def test_getNumbers_comma_in_number():
    """Checks getNumbers with commas in the number"""
    assert formatter.getNumbers("Total amount: $1,000.50") == 1000.50



def test_getNumbers_text_before_and_after():
    """Checks getNumbers with text both before and after the number"""
    assert formatter.getNumbers("Total: $30 and that's it") == 30.00


def test_getNumbers_non_number_in_string():
    """Checks getNumbers with non-numeric characters in the string"""
    assert formatter.getNumbers("Amount to pay: abc$100.50xyz") == 100.50


def test_getNumbers_zero_as_value():
    """Checks getNumbers with zero value"""
    assert formatter.getNumbers("The cost is $0") == 0.00


def test_getNumbers_no_decimal():
    """Checks getNumbers with a whole number without a decimal"""
    assert formatter.getNumbers("Amount: $50") == 50.00


def test_getNumbers_large_integer():
    """Checks getNumbers with a very large integer"""
    assert formatter.getNumbers("Amount: $99999999999") == 99999999999.00



def test_getNumbers_currency_with_space_after_symbol():
    """Checks getNumbers with currency symbol and space between number"""
    assert formatter.getNumbers("Amount: $ 99.99") == 99.99


def test_getNumbers_currency_symbol_with_text_after():
    """Checks getNumbers when currency symbol is followed by text"""
    assert formatter.getNumbers("Amount: $10 plus tax") == 10.00