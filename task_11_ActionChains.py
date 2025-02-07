from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service

service = Service("E:/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://jqueryui.com/droppable/")
sleep(3)

print(driver.current_url)

driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))

actions = ActionChains(driver)                    #for mouse actions we use ActionChains class
drag_element = driver.find_element(By.CSS_SELECTOR, "div[id='draggable']")
drop_element = driver.find_element(By.CSS_SELECTOR, "div[id='droppable']")
actions.drag_and_drop(source=drag_element, target=drop_element).perform()

driver.get_screenshot_as_file("draggable_droppable.png")
sleep(3)

driver.switch_to.default_content()
