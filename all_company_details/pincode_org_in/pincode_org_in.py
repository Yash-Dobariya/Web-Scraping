import json
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

state_list = ["gujarat", "andaman-and-nicobar-islands", "bihar", "daman-and-diu", "haryana", "karnataka", "maharashtra",
            "nagaland", "rajasthan", "tripura", "andhra-pradesh", "chandigarh", "delhi", "himachal-pradesh", "kerala", "manipur",
            "orissa", "sikkim", "uttar-pradesh", "arunachal-pradesh", "chattisgarh", "goa", "jammu-and-kashmir", "lakshadweep",
            "meghalaya", "pondicherry", "tamil-nadu", "uttarakhand", "assam", "dadra-and-nagar-haveli", "jharkhand", "madhya-pradesh",
            "mizoram", "punjab", "telangana", "west-bengal"]


for state in state_list:
    driver.get(f"https://pin-code.org.in/companies/listing/{state}")

    state_links_list = []
    state_links = driver.find_elements(By.XPATH, "//div[@class='listWrap mt-2']//a[@href]")
    for state_link in state_links:
        state_links_list.append(state_link.get_attribute("href"))
    company_link_list = []
    for state_link in state_links_list:
        driver.get(state_link)
        company_links = driver.find_elements(By.XPATH, "//div[@class='boxDetails bg-white p-3 mt-3']//a[@href]")
        for company_link in company_links:
            company_link_list.append(company_link.get_attribute("href"))

    company_data_list = []
    temp=0
    for company_link in  company_link_list:
        driver.get(company_link)
        temp+=1
        print(temp)
        print(company_link)

        company_data = {}

        company_name = driver.find_element(By.XPATH, "//p/strong[contains(text(), 'Name:')]/following-sibling::a").text
        company_data["company_name"] = company_name

        cin_no = driver.find_element(By.XPATH, "//p[strong[text()='CIN No:']]").text.split(":")[1].strip()
        company_data["cin_no."] = cin_no

        status = driver.find_element(By.XPATH, "//p[strong[text()='Status:']]").text.split(":")[1].strip()
        company_data["status"] = status

        class_name = driver.find_element(By.XPATH, "//p[strong[text()='Class:']]").text.split(":")[1].strip()
        company_data["class"] = class_name

        category = driver.find_element(By.XPATH, "//p[strong[text()='Category:']]").text.split(":")[1].strip()
        company_data["category"] = category

        authorize_capital = driver.find_element(By.XPATH, "//p[strong[text()='Authorize Capital:']]").text.split(":")[1].strip()
        company_data["authorize_capital"] = authorize_capital

        paid_up_capital = driver.find_element(By.XPATH, "//p[strong[text()='Paid-up Capital:']]").text.split(":")[1].strip()
        company_data["paid_up_capital"] = paid_up_capital

        registration_date = driver.find_element(By.XPATH, "//p[strong[text()='Registration Date:']]").text.split(":")[1].strip()
        company_data["registration_date"] = registration_date

        business_activity = driver.find_element(By.XPATH, "//p[strong[text()='Business Activity:']]").text.split(":")[1].strip()
        company_data["business_activity"] = business_activity

        state = driver.find_element(By.XPATH, "//p[strong[text()='State:']]").text.split(":")[1].strip()
        company_data["state"] = state

        district = driver.find_element(By.XPATH, "//p[strong[text()='District:']]").text.split(":")[1].strip()
        company_data["district"] = district

        address = driver.find_element(By.XPATH, "//p[strong[text()='Address:']]").text.split(":")[1].strip()
        company_data["address"] = address

        register = driver.find_element(By.XPATH, "//div[@class='col-md-9 col-12']//p").text.split(".")[-2].strip()
        company_data["register"] = register

        try:
            directors_list = []
            directors_info = driver.find_elements(By.XPATH, "//div[@class='row']//div[@class='col-md-10 col-12']//h3")

            for director in directors_info:
                directors_dict = {}
                info = director.text.split()
                directors_dict["DIN"] = info[-1]
                directors_dict["direct_name"] = ' '.join(info[:-1])
                directors_list.append(directors_dict)

            company_data["director_details"] = directors_list
        except:
            pass

        company_data_list.append(company_data)

        with open(f"{state}.json", "w") as file:
            json.dump(company_data_list, file, indent=4)