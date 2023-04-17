#used
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from random import randrange

indeed_home = "https://fr.indeed.com/jobs?q=nodejs&l=France&vjk=e6c0ee2350ed43f0"

#indeed search by word
binary = FirefoxBinary("/Applications/Firefox.app/Contents/MacOS/firefox-bin")
driver = webdriver.Firefox(firefox_binary = binary)
driver.get(indeed_home)
time.sleep(randrange(5))

# delete cookies window
all_buttons = driver.find_elements(by=By.TAG_NAME, value="button")
for button in all_buttons:
    if (button.get_attribute("id")) == "onetrust-reject-all-handler":
        button.click()
        break

# go to connexion page
connexion = driver.find_element(by=By.XPATH, value="//a[text()='Connexion']")
connexion.click()

input("Press Enter to continue...")

# code below is not necessary because connexion will be manually set (captcha), we are waiting for 

# push email
all_inputs = driver.find_elements(by=By.TAG_NAME, value="input")
for input in all_inputs:
    if str(input.get_attribute("type")) == "email":
        # enter email into input
        input.send_keys("henry.keny@outlook.fr")

# click to submit
submit_span = driver.find_element(by=By.XPATH, value="//span[text()='Continuer']")
submit_button = submit_span.find_element(by=By.XPATH, value="./..")
submit_button.click()

# push password
all_inputs = driver.find_elements(by=By.TAG_NAME, value="input")
for input in all_inputs:
    if str(input.get_attribute("type")) == "password":
        # enter password into input
        input.send_keys("Invisible901!")

# click to submit
submit_span = driver.find_element(by=By.XPATH, value="//span[text()='Connexion']")
submit_button = submit_span.find_element(by=By.XPATH, value="./..")
submit_button.click()