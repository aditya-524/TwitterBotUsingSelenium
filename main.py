from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

PROMISED_DOWN = 50  # Promised Download Speed
PROMISED_UP = 50  # Promised Upload Speed
CHROME_DRIVER_PATH = "C:/Users/adity/Development/chromedriver.exe"  # Path of the Chrome Driver
TWITTER_EMAIL = "narutofromdbz@gmail.com"  # Bot Email
TWITTER_USER = "NarutoFromDBZ"  # Bot Username, Used cause multiple logins
TWITTER_PASSWORD = "NarutoisfromDBZ"  # Bot Password


class InternetSpeedTwitterBot():
    ''' Class for the Internet Speed checking and tweeting bot
    Methods
    ------------
    __init__(self, driver_path)
    ------------
    self.driver To initialise the selenium drive using the chromium path to driver_path
    ------------
    get_internet_speed(self)
    ------------
    Method to get internet speed from speedtest.net website
    ------------
    tweet_at_provider(self)
    ------------
    Method to log into Twitter account, copy the tweet with current net speed and promised tweet and tweeting,
    can be altered for a specific vendor of wifi to complain about low internet speeds.
    '''
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/") #Open the speedtest webpage
        time.sleep(3)
        go_button = self.driver.find_element_by_xpath(
            '// *[ @ id = "container"] / div / div[3] / div / div / div / div[2] / div[3] / div[1] / a')
        go_button.click() # start the test by pressing the Go Button
        time.sleep(50) # Wait for test to complete
        # Grabbing the Dowwnload speed and Upload speed
        self.up = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        # Grabbing the Dowwnload speed and Upload speed
        print(f"Upload Speed is {self.up}\n Download Speed is {self.down}")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login") #Twitter Log in Page
        time.sleep(15)
        # Entering the Email for login page
        email = self.driver.find_element(By.NAME, "text")
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)
        time.sleep(5)

        # Entering the Username for login page
        user_bkup = self.driver.find_element(By.NAME, "text")
        user_bkup.send_keys(TWITTER_USER)
        user_bkup.send_keys(Keys.ENTER)
        time.sleep(5)

        # Entering the Password for login page
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(4)

        # Entering the Tweet and Posting it
        tweet_f_button = self.driver.find_element_by_xpath(
            '// *[ @ id = "react-root"] / div / div / div[2] / header / div / div / div / div[1] / div[3] / a')
        tweet_f_button.click()
        time.sleep(2)
        tweet_compose = self.driver.find_element_by_xpath(
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hello World The current Internet Download Speed is {self.down} and upload speed is {self.up}, it should have been  {PROMISED_DOWN} down & {PROMISED_UP}up "
        tweet_compose.send_keys(tweet)
        time.sleep(3)
        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
        tweet_button.click()
        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
