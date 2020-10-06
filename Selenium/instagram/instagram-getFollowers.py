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
        self.browser.get("https://www.instagram.com")
        time.sleep(1)
        usernameInput = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        passwordInput = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)

    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(1)
        self.browser.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(2)
        self.loadFollowers()

    def loadFollowers(self):
        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        followersCount = len(dialog.find_elements_by_css_selector("li"))

        action = webdriver.ActionChains(self.browser)

        # Scrolling
        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)
            newCount = len(dialog.find_elements_by_css_selector("li"))

            if followersCount != newCount:
                followersCount = newCount
                print(f"Count = {followersCount}")
                time.sleep(1)
            else:
                break

        followers = dialog.find_elements_by_css_selector("li")

        followerList = []
        for user in followers:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            followerList.append(link)
            print(link)

        # File
        with open("followers.txt", "w", encoding="UTF-8") as file:
            for item in followerList:
                file.write(item + "\n")


# ******************** Main **************************


username = input("Username: ")
password = input("Password: ")

instagram = Instagram(username, password)
instagram.signIn()
instagram.getFollowers()
