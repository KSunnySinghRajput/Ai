from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pickle

import time
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
driver = webdriver.Chrome(executable_path='driver/chromedriver.exe' ,options=chrome_options)
url = 'https://web.whatsapp.com'
driver.get(url)

time.sleep(30)




#for cookie in pickle.load(open("QuoraCookies.pkl", "rb")):
    #driver.add_cookie(cookie)


#session_url = driver.command_executor._url  
#session_id = driver.session_id
#print (session_id)
#print (session_url)
#driver = webdriver.Remote(command_executor=session_url,desired_capabilities={})

#pickle.dump(driver.get_cookies() , open("QuoraCookies.pkl","wb"))