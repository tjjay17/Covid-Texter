import os
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import io
import requests
#from webdriver_manager.chrome import ChromeDriverManager
from twilio.rest import Client

DRIVER_PATH = 'C:\\Users\\thano\\chromedriver'


#driver = webdriver.Chrome(executable_path=DRIVER_PATH)

#this is gui; actually opens the browser
#driver.get('https://google.ca')

#headless mode
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
options.add_argument('--disable-notifications')

driver = webdriver.Chrome(options = options,executable_path=DRIVER_PATH)
driver.get('https://covid-19.ontario.ca/data')

tableButton = driver.find_element_by_xpath('//*[@id="CasesDaily"]/div/div/div[1]/button[2]')
tableButton.click()

dateElement = driver.find_element_by_xpath('//*[@id="CasesDaily"]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[1]')
casesTodayElement = driver.find_element_by_xpath('//*[@id="CasesDaily"]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[2]')

date = dateElement.get_attribute('innerHTML')
casesToday = casesTodayElement.get_attribute('innerHTML')

client = Client(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages \
    .create(
         body=date + " " + casesToday + ' Cases Today.',
         from_='twilio number here',
         to='put recepient phone number here'
     )

print(message.sid)

driver.quit()
