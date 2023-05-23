from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.divyabhaskar.co.in/")

link_elements = driver.find_elements(By.XPATH, '//div[@class="b7418040"]//li[@class="c7ff6507 db9a2680"]')
links = [link for link in link_elements]
print(links)
print(link_elements)
for link in link_elements:
    driver.get(link)
    print(link)
    break
