from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# ************************* Classes ****************************

class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []

    def SignIn(self):
        self.browser.get("https://github.com/login")
        self.browser.maximize_window()
        time.sleep(2)
        self.browser.find_element_by_xpath('//*[@id="login_field"]').send_keys(self.username)
        self.browser.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)
        time.sleep(1)
        self.browser.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[12]').click()

    def LoadFollowers(self):
        items = self.browser.find_elements_by_css_selector(".d-table.table-fixed")
        for i in items:
            name = i.find_element_by_css_selector(".link-gray.pl-1").text
            self.followers.append(name)

    def GetFollowers(self):

        self.browser.get(f"https://github.com/{self.username}?tab=followers")
        while True:
            links = self.browser.find_element_by_class_name("BtnGroup").find_elements_by_tag_name("a")
            if links == []:
                self.LoadFollowers()
                break
            else:
                if len(links) == 1:
                    if links[0].text == 'Next':
                        links[0].click()
                        time.sleep(1)
                        self.LoadFollowers()
                    else:
                        break
                else:
                    for link in links:
                        if link.text == 'Next':
                            link.click()
                            time.sleep(1)
                            self.LoadFollowers()
                        else:
                            continue


# ************************ Main ********************************

username = input("Username: ")
password = input("password: ")

github = Github(username, password)
github.SignIn()
github.GetFollowers()
print("Followers: ",len(github.followers))
for i in github.followers:
    print(i)
