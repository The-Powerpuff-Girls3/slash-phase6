from currency_converter import CurrencyConverter


def extractValue(price):
    return price.replace("$", "")


def convert(new_currency, price_list):
    c = CurrencyConverter()
    updatedList = []
    new_symbol, new_name = new_currency[4], new_currency[:3]
    for price in price_list:
        price = extractValue(price)
        updatedList.append(new_symbol + str(round(c.convert(price, 'USD', new_name), 2)))
    return updatedList
