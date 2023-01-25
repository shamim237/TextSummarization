import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

def extract(link):
    url = link
    driver_path = "chromedriver.exe"
    browser = Chrome(executable_path = driver_path)
    browser.get(url)
    data = browser.find_element(By.ID,"aplus_feature_div")
    data = data.text
    data = data.split("\n")
    time.sleep(2)
    return data

# ss = extract("https://www.amazon.com/dp/B09B9TB61G?th=1")
# print(ss)