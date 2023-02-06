Import necessary libraries:
python
Copy code
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

from selenium import webdriver: Imports the webdriver module from the selenium library, which allows us to interact with a web browser programmatically.

from selenium.webdriver.common.by import By: Imports the By class from the common.by module, which allows us to specify the locator strategy to find elements on a web page.

from selenium.webdriver.support.ui import WebDriverWait: Imports the WebDriverWait class from the support.ui module, which allows us to wait for a condition to be satisfied before moving forward with the scraping process.

from selenium.webdriver.support import expected_conditions as EC: Imports the expected_conditions module as EC, which provides methods for defining conditions that we want to wait for.

from bs4 import BeautifulSoup: Imports the BeautifulSoup class from the bs4 library, which allows us to parse HTML and XML documents and extract data from them.

from .models import CrawledData: Imports the CrawledData model from the current package (.), which represents the database table where the scraped data will be saved.

driver = webdriver.Firefox(): Instantiates a new instance of the Firefox web driver, which is the actual browser that will be controlled by the script.

list_of_products = []: Creates an empty list to store the scraped product data.

url = "https://www.lammhults.se/products": Specifies the URL of the website to be scraped.

def scraping_bot(url, domain):: Defines a function named scraping_bot that takes two arguments: url and domain. The function will be responsible for performing the actual scraping process.

driver.get(url): Uses the web driver to load the specified URL in the browser.

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Go"]'))): Uses WebDriverWait to wait for a button element with the text "Go" to be clickable, as specified by the XPATH locator //button[text()="Go"]. The driver and 10 arguments specify the web driver instance and the timeout in seconds, respectively.

.click(): Clicks the button that was found using the previous line of code.

soup = BeautifulSoup(driver.page_source, features="html.parser"): Parses the HTML source code of the page using the BeautifulSoup library, and assigns the result to the variable soup. The features argument specifies that the HTML parser should be used.

product_list = soup.find_all("div", class_="product-item-content"): Searches for all <div> elements with the class product-item-content in the parsed HTML document, and assigns the result to the variable product_list.

webdriver is a package that provides a uniform interface to control different browsers. Here, we use the Firefox web driver.
By is an enumeration used to specify the method by which elements are located.
WebDriverWait is a utility class that allows to wait for a certain condition to be met before proceeding with the execution.
expected_conditions is a module that provides methods to wait for certain conditions to be met.
BeautifulSoup is a library for pulling data out of HTML and XML files.

driver = webdriver.Firefox()
Here, we create an instance of the Firefox web driver.

list_of_products = []
This list will store dictionaries, each containing product details scraped from the website.

url = "https://www.lammhults.se/products"
This URL is the one where the products are displayed.


def scraping_bot(url, domain):
    driver.get(url)
This line uses the get method of the webdriver to open the URL in the browser.


 WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[text()="Go"]'))
    ).click()
This line uses WebDriverWait method of the selenium.webdriver.support.ui module to wait until the button with text "Go" is clickable.
Once it is clickable, we use the click method of the button to click it.


soup = BeautifulSoup(driver.page_source, features="html.parser")
This line creates an object of the BeautifulSoup class from the HTML content of the page.
The driver.page_source property is used to get the HTML source of the page, and the features parameter is set to "html.parser" to indicate that we want to use the built-in HTML parser of the beautifulsoup4 library.


product_list = soup.find_all(
        "div", class_="product-item-content"
    )
This line finds all the <div> elements with the class "product-item-content" in the HTML content using the find_all method of the soup object.
The result is stored in the product_list variable.



for product in product_list:
        product_dict = {
            "title": product.find("a", class_="product-title").text,
            "description": product.find("p", class_="product-description").text,
            "image_link": product.find("img", class_="img-responsive")["src"],
            "product_link": f"https://{domain}" + product.find("a", class_="product-title")["href"],
            "category": product.find("a", class_="category").text
        }
This block of code iterates over the elements in the product_list and creates a dictionary product_dict for each product.
The find method of the product element is used to extract the information of the product, such as the title, description, image link, product link, and category, from the HTML content.

        list_of_products.append(product_dict)
Finally, the product_dict is added to the list_of_products list.


The next function is load_data_to_database. This function loads the scraped data into the database. The function takes an argument organization which is an integer value representing the organization for which the data is being scraped.

The function does the following:

It uses the bulk_create method of Django's ORM to create multiple instances of the CrawledData model in a single query, instead of creating a separate query for each instance.
It uses a list comprehension to create a list of instances of the CrawledData model. The values for each instance are taken from the list_of_products list, which was populated with the scraped data in the previous function scraping_bot.
The bulk_create method takes the list of instances and inserts them into the database all at once, which is much more efficient than inserting each instance one by one.
The result of the bulk_create method is stored in a variable bridge.
The function ends by printing a message indicating that the data has been loaded into the database.