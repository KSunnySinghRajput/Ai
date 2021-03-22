mail_address = 'ksunnysingh4295@gmail.com'
password = 'KSan#4Google'

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time 

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
driver = webdriver.Chrome(executable_path='driver/chromedriver.exe' ,options=chrome_options)
url = 'https://accounts.google.com/'
driver.get(url)

driver.find_element_by_name('email').send_keys(mail_address)
#driver.find_element_by_id("Cwak9").click()
#time.sleep(5)
#driver.find_element_by_id("Passwd").send_keys(password)
#driver.find_element_by_id("signIn").click()