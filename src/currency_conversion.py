from currency_converter import CurrencyConverter


def extractValue(price):
    # Removes the dollar sign from the price string and returns the cleaned value
    return price.replace("$", "")


def convert(new_currency, price_list):
    # Converts a list of prices from USD to the specified new currency
    c = CurrencyConverter()
    updatedList = []
    new_symbol, new_name = new_currency[4], new_currency[:3]
    for price in price_list:
        price = extractValue(price)
        updatedList.append(new_symbol + str(round(c.convert(price, 'USD', new_name), 2)))
    return updatedList
