from selenium import webdriver
from selenium.webdriver.common.by import By
import json

driver = webdriver.Firefox()

search_product_name = input("Search product: ")
# search_product_name = 'iphone'
driver.get("https://www.amazon.in/")

search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys(search_product_name)

search_button = driver.find_element(By.XPATH, "//input[@value='Go']")
search_button.click()

links = []
product_list = []

page = driver.find_elements(By.XPATH, "//span[@data-component-type ='s-result-info-bar']")

for i in page:

    """Get all product links"""
    product_links = driver.find_elements(
        By.XPATH, "//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'][@href]")

    for product_link in product_links:
        links.append(product_link.get_attribute('href'))


for link in links:

    product_dict = {}
    """Get link one by one"""
    driver.get(link)

    try:
        """Get title of product"""
        title = driver.find_element(
            By.XPATH, "//span[@class='a-size-large product-title-word-break']").text
        product_dict["title"] = title
        if not title:
            title = driver.find_element(By.TAG_NAME, "h1").text
            product_dict["title"] = title
    except:
        pass
    
    try:
        """Get price of product"""
        price = driver.find_element(
            By.XPATH, ".//span[@class='a-price-whole']").text
        product_dict["price"] = price
    except:
        pass
    
    try:
        """Get discount of product"""
        discount = driver.find_element(
            By.XPATH, "//span[@class='a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage']").text
        product_dict["discount"] = discount
    except:
        pass
    
    try:
        """Get brand title and name of product"""
        brand_title = driver.find_element(
            By.XPATH, "//tr[@class='a-spacing-small po-brand']//td[@class='a-span3']").text
        brand_name = driver.find_element(
            By.XPATH, "//tr[@class='a-spacing-small po-brand']//td[@class='a-span9']").text
        product_dict[brand_title] = brand_name
    except:
        pass
    
    try:
        """Get model title and name of project """
        model_title = driver.find_element(
            By.XPATH, "//tr[@class='a-spacing-small po-model_name']//td[@class='a-span3']").text
        model_name = driver.find_element(
            By.XPATH, "//tr[@class='a-spacing-small po-model_name']//td[@class='a-span9']").text
        product_dict[model_title] = model_name
    except:
        pass
    
    try:
        """Get service title and name of product"""
        service_title = driver.find_element(
            By.XPATH, "//tr[@class='a-spacing-small po-wireless_provider']//td[@class='a-span3']").text
        service_provider_name = driver.find_element(
            By.XPATH, "//tr[@class='a-spacing-small po-wireless_provider']//td[@class='a-span9']").text
        product_dict[service_title] = service_provider_name
    except:
        pass
    
    try:
        """Get os title and name of product"""
        os_title = driver.find_element(
            By.XPATH, "//tr[@class='a-spacing-small po-operating_system']//td[@class='a-span3']").text
        os_name = driver.find_element(
            By.XPATH, "//tr[@class='a-spacing-small po-operating_system']//td[@class='a-span9']").text
        product_dict[os_title] = os_name
    except:
        pass
    
    try:
        """Get cellular_technology title and name of product"""
        cellular_technology_title = driver.find_element(
            By.XPATH, "//tr[@class='a-spacing-small po-cellular_technology']//td[@class='a-span3']").text
        cellular_technology_name = driver.find_element(
            By.XPATH, "//tr[@class='a-spacing-small po-cellular_technology']//td[@class='a-span9']").text
        product_dict[cellular_technology_title] = cellular_technology_name
    except:
        pass
    
    try:
        """Get memory title and name of product"""
        memory_title = driver.find_element(
            By.XPATH, "//tr[@class='a-spacing-small po-memory_storage_capacity']//td[@class='a-span3']").text
        memory_capacity = driver.find_element(
            By.XPATH, "//tr[@class='a-spacing-small po-memory_storage_capacity']//td[@class='a-span9']").text
        product_dict[memory_title] = memory_capacity
    except:
        pass
    
    try:
        """Get connectivity_technology title and name of product"""
        connectivity_technology_title = driver.find_element(
            By.XPATH, "//tr[@class='a-spacing-small po-connectivity_technology']//td[@class='a-span3']").text
        connectivity_technology_name = driver.find_element(
            By.XPATH, "//tr[@class='a-spacing-small po-connectivity_technology']//td[@class='a-span9']").text
        product_dict[connectivity_technology_title] = connectivity_technology_name
    except:
        pass
    
    try:
        """Get color title and name of product"""
        color_title = driver.find_element(
            By.XPATH, "//tr[@class='a-spacing-small po-color']//td[@class='a-span3']").text
        color_name = driver.find_element(
            By.XPATH, "//tr[@class='a-spacing-small po-color']//td[@class='a-span9']").text
        product_dict[color_title] = color_name
    except:
        pass
    
    try:
        """Get screen_size title and name of product"""
        screen_size_title = driver.find_element(
            By.XPATH, "//tr[@class='a-spacing-small po-display.size']//td[@class='a-span3']").text
        screen_size_name = driver.find_element(
            By.XPATH, "//tr[@class='a-spacing-small po-display.size']//td[@class='a-span9']").text
        product_dict[screen_size_title] = screen_size_name
    except:
        pass
    
    try:
        """Get wireless title and name of product"""
        wireless_title = driver.find_element(
            By.XPATH, "//tr[@class='a-spacing-small po-wireless_network_technology']//td[@class='a-span3']").text
        wireless_name = driver.find_element(
            By.XPATH, "//tr[@class='a-spacing-small po-wireless_network_technology']//td[@class='a-span9']").text
        product_dict[wireless_title] = wireless_name
    except:
        pass
    
    try:
        """Get about_title title and name of product"""
        about_title = driver.find_element(
            By.XPATH, "//h1[@class='a-size-base-plus a-text-bold']").text
        about_name = driver.find_element(
            By.XPATH, "//ul[@class='a-unordered-list a-vertical a-spacing-mini']").text
        product_dict[about_title] = about_name
    except:
        pass
    
    try :
        delivery = driver.find_element(
            By.XPATH, "//a[@class='a-size-small a-link-normal a-text-normal']").text
        product_dict["delivery"] = delivery
    except:
        pass
    
    try :
        payment = driver.find_element(
            By.ID, "PAY_ON_DELIVERY").text
        product_dict["payment"] = payment
    except:
        pass
        
    product_list.append(product_dict)

    with open('amazon/products.json', 'w') as file:
        json.dump(product_list, file, indent=4)
        
print(product_list)
