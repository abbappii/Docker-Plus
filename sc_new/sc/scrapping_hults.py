from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

from .models import CrawledData


driver = webdriver.Firefox()
list_of_products = []

url = "https://www.lammhults.se/products"

def scraping_bot(url, domain):
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[text()="Go"]'))
    ).click()

    soup = BeautifulSoup(driver.page_source, features="html.parser")

    product_list = soup.find_all(
        "div", class_="product-item-content"
    )
    for product in product_list:
        product_dict = {
            "title": product.find("a", class_="product-title").text,
            "description": product.find("p", class_="product-description").text,
            "image_link": product.find("img", class_="img-responsive")["src"],
            "product_link": f"https://{domain}" + product.find("a", class_="product-title")["href"],
            "category": product.find("a", class_="category").text
        }
        list_of_products.append(product_dict)


print(f"Scrapping data from {url}")
scraping_bot(url, "www.lammhults.se")

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
                category=item["category"],
                organization=organization
            )
            for item in list_of_products
        ]
    )

print("Loading scraped data into the database")
load_data_to_database(1)

print("Scraping Complete!")