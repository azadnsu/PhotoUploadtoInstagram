#import mysql.connector as mysql
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random
import re
import datetime
import pyautogui

RandomTime = random.randrange(4, 10)

mobile_emulation = {"deviceName": "Nexus 5"}
options = Options()
options.add_experimental_option("mobileEmulation", mobile_emulation)

browser = webdriver.Chrome('/Users/azad/Desktop/ForAlex/chromedriver', options=options)


def signIn(email, password):
    browser.get('https://www.instagram.com/accounts/login/')

    time.sleep(7)

    emailInput = browser.find_elements_by_css_selector('form input')[0]
    passwordInput = browser.find_elements_by_css_selector('form input')[1]

    emailInput.send_keys(email)
    passwordInput.send_keys(password)
    time.sleep(RandomTime)
    passwordInput.send_keys(Keys.ENTER)
    time.sleep(5)


def posting():
    browser.get('https://www.instagram.com/')
    time.sleep(3)
    try:
        browser.find_element_by_class_name("_8-yf5").click()
    except:
        pass
    time.sleep(3)
    try:
        browser.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
        print("annulation OK")
    except:
        print("pas trouvé le bouton annuler")
    try:
        browser.find_element_by_css_selector('[data-testid="new-post-button"]').click()
        time.sleep(1)
        pyautogui.write('/Users/azad/Desktop/ForAlex/Azad.jpeg', interval=0.1)
        #pyautogui.write('C:\Users\Azad\Dropbox\PythonDev\Instagram\image_name.jpg', interval=0.1)
        #pyautogui.write('C:\\Users\Azad\Dropbox\PythonDev\Instagram\image_name.jpg', interval=0.1)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('enter')
        print("click ok")
    except:
        "pas trouvé le bonton +"

    # complete how to give a path to the file and validate


# fill the signin part
signIn('azadhusen', 'Tester1234')
posting()



