import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

element_list = []

# chrome-Optionen
options = Options()
# options.binary_location = "/usr/lib64/chromium-browser/chromium-browser"
options.add_argument("--headless=new")  # headless mode

# GeckoDriver automatisch managen
service = Service()

for page in range(1, 3):
    driver = webdriver.Chrome(service=service, options=options)

    url = f"https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={page}"
    driver.get(url)
    time.sleep(2)

    titles = driver.find_elements(By.CLASS_NAME, "title")
    prices = driver.find_elements(By.CLASS_NAME, "price")
    descriptions = driver.find_elements(By.CLASS_NAME, "description")
    ratings = driver.find_elements(By.CLASS_NAME, "ratings")

    for i in range(len(titles)):
        element_list.append([
            titles[i].text,
            prices[i].text,
            descriptions[i].text,
            ratings[i].text
        ])

    driver.quit()

for row in element_list:
    print(row)
