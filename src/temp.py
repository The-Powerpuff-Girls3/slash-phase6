from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys  # Import Keys to simulate key presses
import random
from bs4 import BeautifulSoup
import re

driver = webdriver.Edge()
# get
driver.get('https://www.target.com/')
time.sleep(3 + random.random() - 0.5)
searchInput = driver.find_element("xpath", "/html/body/div[1]/div[2]/div[2]/div/div[1]/div[6]/form/input")
searchInput.send_keys("laptop")
time.sleep(3 + random.random() - 0.5)  # Replace with your actual search term
searchInput.send_keys(Keys.ENTER)
host = 'www.target.com'
page = driver.page_source
#
# soup = BeautifulSoup(page, "html.parser")
# items = soup.find_all('div', 'sc-11955945-6 oqRHV')
names = []
prices = []
# links = []
nums = 9
tempPrices = re.findall('\$\d*\.\d{2}', page)
tempNames = re.findall(pattern=r'\w{10}', string=page)
for i in range(nums):
    names.append(tempNames[i])
    prices.append(tempPrices[i + 3])

print(names)
