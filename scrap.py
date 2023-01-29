import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

def extract(link):
    url = link
    driver_path = "./chromedriver.exe"
    browser = Chrome(executable_path = driver_path)
    browser.get(url)
    data = browser.find_element(By.ID,"aplus_feature_div")
    data = data.text
    data = data.split("\n")
    time.sleep(1)
    return data

# data = extract("https://www.amazon.com/dp/B09B9TB61G")
# print("Raw Scrapted data: ")
# data = " ".join(data)
# print(data)

