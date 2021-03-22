mail_address = ''
password = ''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

  
'''UA = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:25.0) Gecko/20100101 Firefox/25.0'
PHANTOMJS_ARG = {'phantomjs.page.settings.userAgent': UA}
driver = webdriver.PhantomJS(desired_capabilities=PHANTOMJS_ARG)'''

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
driver = webdriver.Chrome(executable_path='driver/chromedriver.exe' ,options=chrome_options)
url = 'https://accounts.google.com/'
driver.get(url)
#driver.find_element_by_id("Email").send_keys(mail_address)
#driver.find_element_by_id("next").click()
#driver.find_element_by_id("Passwd").send_keys(password)
#driver.find_element_by_id("signIn").click()


driver.get("https://accounts.google.com/signin")
new WebDriverWait(driver, 10).until(ExpectedConditions.elementToBeClickable(By.xpath("//input[@id='identifierId']"))).sendKeys("emailID");
driver.findElement(By.id("identifierNext")).click();

new WebDriverWait(driver, 10).until(ExpectedConditions.elementToBeClickable(By.xpath("//input[@name='password']"))).sendKeys("password");
driver.findElement(By.id("passwordNext")).click();