from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time, os, pyautogui

site = input('Enter site to visit: ')
osopen = os.system('start chrome /incognito '+ site)

#email = input("Enter your ID: ")
#password = input("Enter password: ")

#driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.get('https://facebook.com')
#mail = driver.find_element_by_xpath('//*[@id="email"]')
#mail.send_keys(email)
#pasd = driver.find_element_by_xpath('//*[@id="pass"]')
#pasd.send_keys(password)
#mail.submit()

time.sleep(15)
#driver.quit()
