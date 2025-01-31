from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep        

driver = webdriver.Chrome()                    #chosen chrome driver to test
driver.get("https://www.instagram.com/guviofficial/")                               #guvi instagram url
sleep(5)                                   
guvi_followers = driver.find_element(By.XPATH,"//*[contains(text(),' followers')]").text    #text is the only unique thing to fetch followers & following
sleep(5)                                                                                  
print(guvi_followers)
guvi_following = driver.find_element(By.XPATH,"//*[contains(text(),' following')]").text
sleep(5) 
print(guvi_following)
