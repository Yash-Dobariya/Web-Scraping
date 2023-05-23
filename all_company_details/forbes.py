from selenium.webdriver import  Firefox
from selenium.webdriver.common.by import By
import json

driver = Firefox()

driver.get("https://www.forbes.com/lists/global2000/")

link_list = []
company_data_list = []

all_link = driver.find_elements(By.XPATH, "//div[@class='table-row-group']//a[@href]")
for link in all_link:
    link_list.append(link.get_attribute('href'))
    breakpoint()
    
for link in link_list:
    driver.get(link)
    print(link)
    company_data = {}
    
    company_name = driver.find_element(By.TAG_NAME, "h1").text
    company_data["company_name"] = company_name
    try:
        share_price = driver.find_element(By.CLASS_NAME, "profile-info__item-value").text
        company_data["share_price"] = share_price
    except:
        pass

    from bs4 import BeautifulSoup
    import requests
    
    response = requests.get(link)
    
    html_page = BeautifulSoup(response.content, 'html.parser')
    
    try:
        about_company = html_page.find('div', {'class': 'listuser-content__bio--expanded hidden'}).text.strip()
        company_data["about"] = about_company
        if not about_company:
            about_company = html_page.find('p', class_='listuser-content__bio--copy').text
            company_data["about"] = about_company
            print("done")
    except:
        print("not_print")
    
    try:
        industry = driver.find_element(By.XPATH, "//dt[contains(text(), 'Industry')]/following-sibling::dd/span").text
        company_data["industry"] = industry
    except:
        pass
    
    try:
        founded = driver.find_element(By.XPATH, "//dt[contains(text(), 'Founded')]/following-sibling::dd/span").text
        company_data["founded"] = founded
    except:
        pass
    
    try:
        headquarters = driver.find_element(By.XPATH, "//dt[contains(text(), 'Headquarters')]/following-sibling::dd/span").text
        company_data["headquarters"] = headquarters
    except:
        pass
        
    try:
        country = driver.find_element(By.XPATH, "//dt[contains(text(), 'Country')]/following-sibling::dd/span").text
        company_data["country"] = country
    except:
        pass
    
    try:
        ceo = driver.find_element(By.XPATH, "//dt[contains(text(), 'CEO')]/following-sibling::dd/span").text
        company_data["ceo"] = ceo
    except:
        pass

    try:
        employees = driver.find_element(By.XPATH, "//dt[contains(text(), 'Employees')]/following-sibling::dd/span").text
        company_data["employees"] = employees
    except:
        pass
    
    try:
        revenue = driver.find_element(
            By.XPATH, "//div[@class='listuser-financial-item__title' and text()='Revenue']/following-sibling::div").text
        company_data["revenue"] = revenue
    except:
        pass

    try:
        assets = driver.find_element(
            By.XPATH, "//div[@class='listuser-financial-item__title' and text()='Assets']/following-sibling::div").text
        company_data["Assets"] = assets
    except:
        pass
    
    try:
        profits = driver.find_element(
            By.XPATH, "//div[@class='listuser-financial-item__title' and text()='Profits']/following-sibling::div").text
        company_data["profits"] = profits
    except:
        pass
    
    company_data_list.append(company_data)
    
    with open("forbas_data.json", 'w') as file:
        json.dump(company_data_list, file, indent=4)


driver.close()