
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
  
# Replace below path with the absolute path 
# to chromedriver in your computer 
driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
driver.get("https://www.irctc.co.in/nget/train-search") 
wait = WebDriverWait(driver, 600) 

login = driver.find_element_by_class_name('ng-star-inserted')
login.click()
