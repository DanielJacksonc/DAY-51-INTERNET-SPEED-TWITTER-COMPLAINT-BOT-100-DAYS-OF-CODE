#import all neccessary modules
import time
import os
XFINITY = "@Xfinity"
CONSTANT = "400download/10up?"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


TWITTER_URL = "https://twitter.com/login"
common_option = webdriver.ChromeOptions()
common_option.add_experimental_option("detach", True)

# create a class for the internet speed and the twitter
class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=common_option)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(url="https://www.highspeedinternet.com/tools/speed-test")
        time.sleep(7)
        self.driver.find_element(By.XPATH,"//span[@class='start-button-text']").click()


        download = self.driver.find_element(By.XPATH, "//strong[@class='speed-download font-medium']")

        upload = self.driver.find_element(By.XPATH, "//*[@id='speed-test-banner']/div[1]/div/div/div/div[2]/div[2]/div/div[2]/strong")
        time.sleep(25)
        down = download.text.split(",")
        self.down = float(down[0].split()[0])
        up = upload.text.split(",")
        self.up = float(up[0].split()[0])
        print(f"Up is: {self.up}, down is: {self.down}")


    def tweet_at_provider(self,LOG,PASS):
        self.driver.get(url=TWITTER_URL)
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@name='text']").send_keys(LOG, Keys.ENTER)

        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@name='text']").send_keys(PATH, Keys.ENTER)
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(PASS, Keys.ENTER)

        print("completed")

        self.driver.implicitly_wait(6)

        (self.driver.find_element(By.XPATH,
                                 "//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']")
         .send_keys(f"Hey Internet Provider! {XFINITY} , Why is my internet speed {self.down}"
                    f"down/{self.up}up, when i paid for {CONSTANT} from Codedchild"))

        self.driver.close()






