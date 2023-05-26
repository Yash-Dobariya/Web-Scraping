"""from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

driver = Firefox()

driver.get("https://www.mca.gov.in/mcafoportal/viewCompanyMasterData.do")

driver.find_element(By.ID, "imgSearchIcon").click()

a = driver.find_element(By.NAME, "searchcompanyname").screenshot
# a.screenshot("REJOICEHUB LLP")
# driver.find_element(By.ID, "findcindata").click()
"""

from scrapy.selector import Selector
body = "<html><body><span>good</span><span>person</span><span>bad</span></body></html>"
print(Selector(text=body).xpath("//span/text()").getall())

