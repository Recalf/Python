from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


url = r"https://orteil.dashnet.org/cookieclicker/"
driver = webdriver.Chrome()
driver.get(url)

WebDriverWait(driver,60).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'English')]"))
)

product = driver.find_element(By.XPATH, "//*[contains(text(),'English')]")
product.click()

WebDriverWait(driver,60).until(
    EC.presence_of_element_located((By.ID, "bigCookie"))
)
cookie = driver.find_element(By.ID, "bigCookie")

while True:
    cookie.click()
    counter = driver.find_element(By.ID, "cookies").text.split()[0]
    counter = int(counter.replace(",",""))
    # transform it into int for comparison
    

    for i in range(4):
        product_price = driver.find_element(By.ID, ("productPrice" + str(i))).text
        print(product_price)               

        if not product_price.isdigit():
            continue
        
        product_price = int(product_price.replace(",",""))
        print(counter)

        
        if counter >= product_price:
            print(counter)
            print(product_price)
            product = driver.find_element(By.CSS_SELECTOR, "#product" + str(i))
            product.click()
            break
        

    