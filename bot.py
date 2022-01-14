from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#import time

# settings
options = Options()
# options.add_argument('headless')
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('start-maximized') # 
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")

driver = webdriver.Chrome(options=options)

driver.get('https://www.amazon.com.br/')

#time.sleep(10)

#driver.find_element_by_xpath('/html/body/div[1]/div[3]/main/div/div/div[1]/div[1]/div[2]/ul/a[1]').click() 
#driver.find_element_by_xpath('/html/body/div[1]/div[3]/main/div/div/div[1]/div[1]/div[2]/ul/a[2]').click() 
#driver.find_element_by_xpath('/html/body/div[1]/div[3]/main/div/div/div[2]/div[3]/div/div[1]/div/div/button[1]').click() 

#driver.find_element_by_xpath('').send_keys("")

#driver.find_element_by_xpath('').send_keys("")

#time.sleep(2)

#driver.get_screenshot_as_file("images/capture.png")

#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time, urllib.request
import os 
import sys
import logging
import argparse

#settings 
options = Options()
# options.add_argument('headless')
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('start-maximized') # 
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
options.add_argument('--window-size=2130x1080')


driver = webdriver.Chrome(options=options)

class Myrobot:

    global driver
    
    def __init__(self, page_name):
        self.page_name = page_name
        self.driver = driver

    def start_connection(self):
        
        # steps 
        driver.get("http://google.com.br")
        time.sleep(5)

        items = driver.execute_script("return [...document.querySelectorAll('button')].map(item => item.innerText)")
        print(items)

        items = driver.execute_script("return [...document.querySelectorAll('button')].filter(item => !!item.innerText)")

        for i in items:
            print(i.click()) #open another browser


        # time.sleep(3)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Runnnig...")

    parser.add_argument(
        "--url-page", 
        "-U",
        default="", 
        help="Enter the name of the page that you wanna scrap !!")
    
    # parser.add_argument(
    #     "--url-page", 
    #     "-U",
    #     default="", 
    #     help="Enter the name of the page that you wanna scrap !!")

    args = parser.parse_args()
    images = Myrobot(args.url_page)
    images.start_connection()

driver.quit()
