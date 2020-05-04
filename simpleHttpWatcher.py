#! /usr/bin/env python3

# import webbrowser
# from time import sleep

# url = input("https://www.google.com")

# while True:
#     print("refreshing...")
#     webbrowser.open(url, new=0)
#     sleep(10)


# url = "https://www.google.com"


# Open url in a new window of the default browser, if possible
# webbrowser.open_new(url)

# while True:
#     print("refreshing...")
#     webbrowser.open(url, new=0)
#     sleep(10)

import time
from selenium import webdriver

driver = webdriver.Firefox()
url = "https://www.google.com"
driver.get(url)
while True:
    time.sleep(5)
    driver.refresh()
driver.quit()