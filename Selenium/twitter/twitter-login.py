from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# *************** Classes ***********************

class Twitter:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en, en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://twitter.com/login")
        time.sleep(1)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input').send_keys(self.username)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input').send_keys(self.password)
        self.browser.find_element_by_css_selector('div[role=button]').click()


# ********************* Main ******************************

username = input("Username: ")
password = input("Password: ")

twitter = Twitter(username, password)

twitter.signIn()
