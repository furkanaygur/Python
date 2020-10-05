# if you dont have selenium packages, you have to install
# pip install selenium
from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/furka/Desktop/Python-Ornekleri/Selenium/chromedriver.exe')

url = "https://furkanaygur.netlify.app"
driver.get(url)

print(driver.title)
driver.maximize_window()
time.sleep(1)
driver.save_screenshot("ss.png")

url = "https://github.com/furkanaygur"

driver.get(url)
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()

driver.close()
