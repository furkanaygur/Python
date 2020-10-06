from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# *************** Classes ***********************

class Twitter:
    def __init__(self):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en, en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)

    def searchHashtage(self, word):
        self.browser.get("https://twitter.com/twitter")
        time.sleep(1)
        searchInput = self.browser.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input')
        searchInput.send_keys(word)
        time.sleep(1)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(1)
        self.browser.maximize_window()
        time.sleep(1)

        # scroll with js
        loopCounter = 0
        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")
        while True:
            if loopCounter > 3:
                break
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(2)
            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            loopCounter += 1
            self.getTweet()

    def getTweet(self):
        list = self.browser.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]")

       # File
        with open("tweets.txt", "w", encoding="UTF-8") as file:
            for tweet in list:
                file.write(" Tweet Start ".center(50, '*'))
                file.write("\n")
                file.write(tweet.text + '\n')
                file.write(" Tweet End ".center(50, '*'))
                file.write("\n \n")

        for item in list:
            print(' Tweet Start '.center(50, '*'))
            print(item.text)
            print(' Tweet End '.center(50, '*'))
            print("\n")


# ********************* Main ******************************

word = input("word : ")
twitter = Twitter()
twitter.searchHashtage(word)
