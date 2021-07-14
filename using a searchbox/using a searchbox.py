from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "U:\Selenium\one1\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com/")
print(driver.title)

search = driver.find_element_by_name("q")
search.send_keys("Search using google!")
search.send_keys(Keys.RETURN)


time.sleep(5)

driver.quit()