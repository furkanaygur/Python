from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# *********************** Classes *************************************
class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://instagram.com")
        time.sleep(1)
        usernameInput =self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        passwordInput = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)

# ******************** Main **************************

username = input("Username: ")
password = input("Password: ")

instagram = Instagram(username, password)
instagram.signIn()
