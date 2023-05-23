import json
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

state_list = ["Maharashtra ","Rajasthan","Uttar Pradesh","Madhya Pradesh","Haryana","Delhi","Chandigarh","Jammu & Kashmir","Punjab",
            "Himachal Pradesh", "Tamil Nadu", "Kerala", "Karnataka", "Andhra Pradesh", "Telangana", "Odisha", "West Bengal",
            "Jharkhand", "Chhattisgarh", "Sikkim", "Gujarat", "Goa", "Arunachal Pradesh", "Bihar", "Mizoram", "Meghalaya",
            "Uttarakhand","Tripura", "Manipur", "Assam", "Nagaland", "Pondicherry", "Daman & Diu", "Lakshadweep", "Dadar and Nagar Haveli",
            "Andaman & Nicobar"]

company_data_list = []
for state in state_list:
    driver.get(f"https://www.tofler.in/companylist/{state}")
    
    company_link_list = []
    company_links = driver.find_elements(By.CLASS_NAME, "complink")
    for company_link in company_links:
        company_link_list.append(company_link.get_attribute('href'))
    
    for company_link in company_link_list:
        company_data = {}
        company_overview = driver.find_element(By.ID, "overview").text
        company_data["company_overview"] = company_overview

        company_data_list.append(company_data)
        with open("tofier.json", "w") as file:
            json.dump(company_data_list, file, indent=4)
        
