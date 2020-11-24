import os
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import io
#from webdriver_manager.chrome import ChromeDriverManager
from twilio.rest import Client

DRIVER_PATH = 'C:\\Users\\thano\\chromedriver'
ACCOUNT_SID = 'AC036c032f9041a70fc94fcea7012c2a13'
AUTH_TOKEN = '0e437fb716f470d68a8af34ad67c2d87'

#array of numbers go in here as strings
PHONE_NUMBERS = []

#this is gui; actually opens the browser
#driver.get('https://google.ca')

#headless mode
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
options.add_argument('--disable-notifications')

driver = webdriver.Chrome(options = options,executable_path=DRIVER_PATH)
driver.get('https://covid-19.ontario.ca/data')

tableButton = driver.find_element_by_xpath('//*[@id="CasesDaily"]/div/div[1]/button[2]')
tableButton.click()

#dateElement = driver.find_element_by_xpath('//*[@id="CasesDaily"]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[1]')
casesTodayElement = driver.find_element_by_xpath('//*[@id="CasesDaily"]/div/div[2]/div/div/div/div/div/table/tbody/tr[2]/td[2]')
casesToday = casesTodayElement.get_attribute('innerHTML')

client = Client(ACCOUNT_SID, AUTH_TOKEN)

#The twilio number goes in from and to is the number that is wanted to receive msg
#Loop through array of numbers to send numbers
for i in range (len(PHONE_NUMBERS)):
    message = client.messages \
        .create(
            body = casesToday + ' Cases Today.',
            from_ = '+14305411019',
            to = PHONE_NUMBERS[i]
        )

print(message.sid)
driver.quit()
