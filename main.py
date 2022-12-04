from selenium import webdriver
import time

PROMISED_DOWN = 50
PROMISED_UP = 50
CHROME_DRIVER_PATH = "C:/Users/adity/Development/chromedriver.exe"
TWITTER_EMAIL = "narutofromdbz@gmail.com"
TWITTER_PASSWORD = "NarutoisfromDBZ"

class InternetSpeedTwitterBot():
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        # go_button = self.driver.find_element_by_css_selector(".start-button a")
        go_button = self.driver.find_element_by_xpath('// *[ @ id = "container"] / div / div[3] / div / div / div / div[2] / div[3] / div[1] / a')
        go_button.click()
        time.sleep(50)
        self.up = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"Upload Speed is {self.up}\n Download Speed is {self.down}")
    def tweet_at_provider(self):
        pass

bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()