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
options.add_argument('headless')
options.add_argument('--no-sandbox') # Bypass OS security model
# options.add_argument('start-maximized') # 
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
options.add_argument('--window-size=1280x1696')

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

        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Runnnig...")
    parser.add_argument(
        "--url-page", 
        "-U",
        default="", 
        help="Enter the name of the page that you wanna scrap !!")

    args = parser.parse_args()
    images = Myrobot(args.url_page)
    images.start_connection()
