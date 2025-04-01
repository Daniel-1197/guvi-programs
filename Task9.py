from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
user_name = driver.find_element(By.ID,'user-name')
user_name.send_keys('standard_user')
password = driver.find_element(By.ID,'password')
password.send_keys('secret_sauce')
driver.find_element(By.ID,'login-button').click()
sleep(5)
print(driver.title)            #1 Title of the page
print(driver.current_url)      #2 Current url of the page
page_content =driver.find_element(By.XPATH,'/html/body').text     #3
file_obj = open('webpage_task_11.txt', 'w')
file_obj.write(page_content)     #3. Extracting contents of the webpage and writing it in txt file
print("webpage content saved to 'webpage_task_11.txt' file!")
file_obj.close()

