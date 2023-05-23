from selenium import webdriver
from selenium.webdriver.common.by import By

"""user give brand name as a input"""
name = input("enter brand name:   ")

driver = webdriver.Chrome()

source = "https://www.amazon.in/"

driver.get(source)

final_data =[]
links = []

"""find id of search bar"""
search_bar = driver.find_element(By.ID, "twotabsearchtextbox")

"""insert brand name in search bar by send_keys"""
search_bar.send_keys(name)

"""find id of search button"""
serach_button = driver.find_element(By.ID,"nav-search-submit-button")

"""click search button"""
serach_button.click()

products = driver.find_elements(By.XPATH, "//div[@class ='s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis s-latency-cf-section s-card-border']")

for pr in products:
    
    """to get product name """
    productname =  pr.find_element(By.TAG_NAME, "h2").text

    """to filter products according to brand name"""
    user_input = str(name).lower()
    product_name = productname.lower()

    if user_input in product_name:
        
        """check price is present or not"""

        try:
            product_price = pr.find_element(By.CLASS_NAME, 'a-price').text

        except:
            product_price = "not found"     

        """store data in dictionary"""
        final_data.append({
            "phone_name":product_name,
            "phone_price":product_price  
        })

"""find next button """
link = driver.find_element(By.XPATH,"//a[@class = 's-pagination-item s-pagination-next s-pagination-button s-pagination-separator']").get_attribute('href')

links.append(link)


"""to scrape next pages"""

for i in links:

    """take next page url as a new source"""
    new_source = link

    driver.get(new_source)

    products = driver.find_elements(By.XPATH, "//div[@class ='s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis s-latency-cf-section s-card-border']")

    for pr in products:
        """to get product name """
        productname =  pr.find_element(By.TAG_NAME, "h2").text

        user_input = str(name).lower()
        product_name = productname.lower()

        if user_input in product_name:
            
            """to get product price"""

            try:
                product_price = pr.find_element(By.CLASS_NAME, 'a-price').text

            except:
                product_price = "not found"     

            """store data in dictionary"""
            final_data.append({
                "phone_name":product_name,
                "phone_price":product_price  
            })

    """try to find next button class and if did not found it , it will break the loop"""        
    try:
        link = driver.find_element(By.XPATH,"//a[@class = 's-pagination-item s-pagination-next s-pagination-button s-pagination-separator']").get_attribute('href')
        links.append(link)
    except:

        break

for data in final_data:

    print(data)

while True:

    pass












# page = []
# links = []
# product_list = []

# pages = driver.find_elements(
#     By.XPATH, "//span[@class ='s-pagination-item s-pagination-selected'][@href]")

# for i in pages:
#     breakpoint()
#     page.append(i.get_attribute('href'))

# for i in page:
    
#     driver.get(i)
    
#     """Get all links"""
#     product_links = driver.find_elements(
#         By.XPATH, "//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'][@href]")
    
#     for product_link in product_links:
#         links.append(product_link.get_attribute('href'))