from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

from .models import CrawledData


driver = webdriver.Firefox()
list_of_products = []

url = "https://store.flokk.com/sweden/en-gb/products"

def scraping_bot(url, domain):
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[text()="Go"]'))
    )

    soup = BeautifulSoup(driver.page_source, features="html.parser")

    product_list = soup.find_all(
        "li", class_="js-product-item"
    )
    for product in product_list:
        product_dict = {
            "title": product.find("h3", class_="title").text,
            "description": product.find("p", class_="description").text,
            "image_link": product.find("img", class_="img-responsive")["src"],
            "product_link": f"https://{domain}" + product.find("a", class_="js-product-link")["href"],
        }
        list_of_products.append(product_dict)


print(f"Scrapping data from {url}")
scraping_bot(url, "store.flokk.com")

driver.close()

# Loading data into the database
def load_data_to_database(organization):
    bridge = CrawledData.objects.bulk_create(
        [
            CrawledData(
                title=item["title"],
                description=item["description"],
                image_link=item["image_link"],
                product_link=item["product_link"],
                organization=organization
            )
            for item in list_of_products
        ]
    )

print("Loading scraped data into the database")
load_data_to_database(1)

print("Scraping Complete!")



# v2
import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
list_of_products = []

url = "https://store.flokk.com/sweden/en-gb/products"
domain = "store.flokk.com"

def scraping_bot(url, domain):
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[text()="Go"]'))
    ).click()

    # number of time website should scroll down to load data
    scroll = 20
    while scroll >= 0:
        try:
            # Action scroll down
            scrolling = driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )
            time.sleep(3)
        except:
            print("Couldn't Scroll the page!")
        scroll -= 1

    soup = BeautifulSoup(driver.page_source, features="html.parser")

    product_list = soup.find_all(
        "div", class_="product-card"
    )
    for product in product_list:
        product_dict = {
            "title": product.find("a", class_="product-card__title").text,
            "description": product.find("p", class_="product-card__description").text,
            "image": product.find("img", class_="product-card__image").get("src"),
            "price": product.find("span", class_="product-card__price").text,
        }
        list_of_products.append(product_dict)

print(f"Scrapping data from {domain}")
scraping_bot(url, domain)

driver.close()

print("Scraped data: ", list_of_products)