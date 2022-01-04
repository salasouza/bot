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
driver.quit()
