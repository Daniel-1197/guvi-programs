from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Define a class for the automation task
class SauceDemoAutomation:
    def __init__(self):
        #Setup Chrome browser using WebDriver Manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def login_and_extract(self):
        try:
            # Navigate to the SauceDemo login page
            self.driver.get("https://www.saucedemo.com/")

            # Enter username
            user_name = self.driver.find_element(By.ID, 'user-name')
            user_name.send_keys('standard_user')

            # Enter password
            password = self.driver.find_element(By.ID, 'password')
            password.send_keys('secret_sauce')

            # Click login button
            self.driver.find_element(By.ID, 'login-button').click()

            sleep(3)  # Wait for the page to load

            # Print title and current URL
            print("Page Title:", self.driver.title)                  # 1. Title of the page
            print("Current URL:", self.driver.current_url)          # 2. Current URL of the page

            # Extract entire body text and save to a file
            page_content = self.driver.find_element(By.XPATH, '/html/body').text
            with open('webpage_task_11.txt', 'w') as file:
                file.write(page_content)                            # 3. Write content to a text file
            print("Webpage content saved to 'webpage_task_11.txt' file!")

        except Exception:
            print("An error occurred")

        finally:
            # Close the browser after a short wait
            sleep(2)
            self.driver.quit()

# Create object for the class
automation = SauceDemoAutomation()
automation.login_and_extract()
