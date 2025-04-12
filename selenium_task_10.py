from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class InstagramGuvi:

    def __init__(self):
        # Initialize Chrome browser
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def open_profile(self, url):

        # Navigates to the given Instagram profile URL.
        self.driver.get(url)
        sleep(5)  # Allow time for page to load

    def get_stats(self):

        try:
            # Locate and extract the number of followers
            followers_text = self.driver.find_element(By.XPATH, "//*[contains(text(),' followers')]").text
            print(f"GUVI Followers: {followers_text}")

            sleep(2)  # wait before the next element

            # Locate and extract the number of following
            following_text = self.driver.find_element(By.XPATH, "//*[contains(text(),' following')]").text
            print(f"GUVI Following: {following_text}")

        except Exception as e:
            print("An error occurred while fetching stats:", e)

        finally:
            self.driver.quit()    #close the browser



# Create object of the class
guvi_stats = InstagramGuvi()
guvi_stats.open_profile("https://www.instagram.com/guviofficial/")

 # Fetch followers and following
guvi_stats.get_stats()
