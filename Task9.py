import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import service



driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(5)
page_content =driver.find_element(By.XPATH,'/html/body').text
file = open('webpage_txt11.txt','w')
file.write(page_content)
print(driver.title)
print(driver.current_url)
print("webpage content saved to 'webpage_txt11.txt'")
file.close()


