import json
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://www.ambitionbox.com/list-of-companies")


links = driver.find_elements(By.CSS_SELECTOR, 'meta[itemprop="url"]')

links_list = []
company_data_list = []

for link in links:
    links_list.append(link.get_attribute("content"))


for link in links_list[1:]:
    driver.get(link)
    
    company_data = {}
    breakpoint()
    founding_year = driver.find_element(
        By.XPATH, '//li[@class="aboutItem"]/p[@class="aboutItem__name"][contains(text(), "Founded in")] \
        /following-sibling::p[@class="textItem__val aboutItem__value"]').text
    company_data["founding_year"] = founding_year
    
    ownership = driver.find_element(By.XPATH, '//li[@class="aboutItem"]/p[@class="aboutItem__name"][contains(text(), "Ownership")] \
        /following-sibling::div[@class="textItem__val aboutItem__value"]/a').text
    company_data["ownership"] = ownership
    
    india_employee = driver.find_element(By.XPATH, '//li[@class="aboutItem"]/p[@class="aboutItem__name"][contains(text(), "India Employee count")] \
                                            /following-sibling::p[@class="textItem__val aboutItem__value"]').text
    company_data["india_employee"] = india_employee

    global_employee = driver.find_element(By.XPATH, '//li[@class="aboutItem"]/p[@class="aboutItem__name"][contains(text(), "Global Employee count")] \
                                        /following-sibling::div[@class="suggest aboutItem__value"]/div[@class="suggestBtn"]/following-sibling::div[@class="modal-mask"]').text
    company_data["global_employee"] = global_employee
    
    headquarters = driver.find_element(By.XPATH, '//li[@class="aboutItem"]/p[@class="aboutItem__name"][contains(text(), "Headquarters")] \
        /following-sibling::div[@class="textItem__val aboutItem__value"]/a').text
    company_data["headquarters"] = headquarters
    
    office_locations = driver.find_elements(By.XPATH, '//li[@class="aboutItem"]/p[@class="aboutItem__name"][contains(text(), "Office Locations")] \
        /following-sibling::div[@class="aboutItem__value flex-row"]/div[@class="textItem__val"]/a')
    
    location_list = []
    for location in office_locations:
        location_list.append(location.text)
    company_data["office_locations"] = location_list
    
    ceo = driver.find_element(By.XPATH, '//li[@class="aboutItem"]/p[@class="aboutItem__name"][contains(text(), "CEO")] \
        /following-sibling::p[@class="textItem__val aboutItem__value"]').text
    company_data["ceo"] = ceo
    
    company_type = driver.find_element(By.XPATH, '//li[@class="aboutItem"]/p[@class="aboutItem__name"][contains(text(), "Type of Company")] \
        /following-sibling::div[@class="textItem__val aboutItem__value"]/a').text
    company_data["company_type"] = company_type
    
    company_data_list.append(company_data)
    
    with open("ambition_box.json", "w") as file:
        json.dump(company_data_list, file, indent=4)
    
