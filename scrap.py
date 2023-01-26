import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

def extract(link):
    url = link
    firefoxOptions = Options()
    firefoxOptions.add_argument("--headless")
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(
        options=firefoxOptions,
        service=service,
    )
    driver.get(url)
    data = driver.find_element(By.ID,"aplus_feature_div")
    data = data.text
    data = data.split("\n")
    time.sleep(2)
    return data

# ss = extract("https://www.amazon.com/dp/B09B9TB61G?th=1")
# print(ss)
