from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "..\using a searchbox\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com/")
print(driver.title)

search = driver.find_element_by_name("q")
search.send_keys("Search using google!")
search.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()
