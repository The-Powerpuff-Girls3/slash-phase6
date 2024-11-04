from threading import Thread
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

import time
import undetected_chromedriver as uc

import undetected_chromedriver as uc
try:
    import src.formattr as form # Avoid path error when testing the script by if __name__ == '__main__'
except ImportError:
    class form:
        @staticmethod
        def formatSearchQuery(query):
            # Basic query formatting (e.g., replace spaces with '+')
            return query.replace(' ', '+')

        @staticmethod
        def formatResultCostco(site, result):
            # Format the result dictionary as needed
            return {
                'site': site,
                'title': result['title'],
                'price': result['price'],
                'link': result['link'],
                'img_link': result['img_link']
            }


class search_target(Thread):
    def __init__(self, query, config):
        self.result: list = None
        self.query = query
        self.config = config
        super(search_target, self).__init__()

    # Setup Chrome driver with options
    def setup_driver(self):
        options = uc.ChromeOptions()
        # Remove '--headless' if you want to see the browser window
        # options.add_argument('--headless')
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        # Set a common user agent
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                            'AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/87.0.4280.88 Safari/537.36')
        driver = uc.Chrome(options=options)
        # Modify navigator.webdriver
        driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
            'source': '''
                Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
            '''
        })
        return driver

    def run(self):
        self.query = form.formatSearchQuery(self.query)
        URL = self.config['url'] + self.query

        # Fetch URL
        driver = self.setup_driver()
        driver.get(URL)
        time.sleep(5)  # Wait for the page to load

        self.result = self.scrape_products(driver)
        driver.quit()

    def load_full_page(self, driver):
        SCROLL_PAUSE_TIME = 2.5
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)

            # Check if we've reached the bottom
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def scrape_products(self, driver):
        results = []

        # Wait until the products are loaded
        try:
            WebDriverWait(driver, 30).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[data-test="@web/ProductCard/body"]'))
            )
        except TimeoutException:
            print("Products did not load in time.")
            return results

        self.load_full_page(driver)

        time.sleep(5)  # Wait for images to load
        # Find all product containers
        product_containers = driver.find_elements(By.CSS_SELECTOR, 'div[data-test="@web/ProductCard/body"]')

        for container in product_containers:
            # Initialize data variables
            title_text = 'N/A'
            price_text = 'N/A'
            product_link = 'N/A'
            image_link = 'N/A'

            # Scroll container into view
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", container)
            time.sleep(2)  # Wait for images to load

            # Extract product link and title
            try:
                link_element = container.find_element(By.CSS_SELECTOR, 'a.h-display-block')
                product_link = link_element.get_attribute('href')
                title_text = link_element.get_attribute('aria-label') or link_element.text.strip()
            except NoSuchElementException:
                print("No link or title found for this product.")
                continue  # Skip to the next product

            # Extract image link
            try:

                # Get the parent element that contains both the product info and image
                # parent_card = container.find_element(By.XPATH, "./..")
                image_link = container.find_element(By.XPATH, "./..").find_elements(By.CSS_SELECTOR, 'picture source')[0].get_attribute('srcset')

                if not image_link:
                    print(f"No image URL found for '{title_text}'")
            except NoSuchElementException:
                print(f"No image found for '{title_text}'")

            # Extract the current price
            try:
                price_element = container.find_element(By.CSS_SELECTOR, 'span[data-test="current-price"] > span')
                price_text = price_element.text.strip()
            except NoSuchElementException:
                print(f"No price found for '{title_text}'")

            # Append the product details to the list
            results.append({
                'title': title_text,
                'price': price_text,
                'link': product_link,
                'img_link': image_link
            })

            # Format the results
            products = [form.formatResultCostco(self.config['site'], result) for result in results]

        return products


if __name__ == '__main__':
    query = 'dell'
    config = {
        'url': 'https://www.target.com/s?searchTerm=',
        'site': 'target',
    }
    scraper = search_target(query, config)
    scraper.start()
    scraper.join()
    # Print the results
    # breakpoint()
    results = scraper.result[:10] if scraper.result else []
    for result in results:
        print(result)