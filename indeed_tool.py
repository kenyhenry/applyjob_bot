#unused
from logging import NullHandler
from os import system
import webbrowser
import urllib3
import re

#used
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from random import randrange

indeed_home = "https://fr.indeed.com/jobs?q=nodejs&l=France&vjk=e6c0ee2350ed43f0"

# connect with profil indeed
# fp = webdriver.FirefoxProfile('/Users/kenyhenry/Library/Application Support/Firefox/Profiles/ci67x9ed.default-release')
# driver = webdriver.Firefox(fp)

driver = webdriver.Firefox()

driver.get(indeed_home)
time.sleep(randrange(5))

input("connect to indeed then press enter")

#applications
main_window = driver.execute_script('return window.name')

watchdog = True

while watchdog:

    # go to the next page
    # retrive nav element list
    next_page = ""
    nav_list = driver.find_elements(by=By.TAG_NAME, value="nav")
    for nav in nav_list:
        # if element is navigation bar
        if nav.get_attribute("class") == "css-jbuxu0 ecydgvn0":
            next_page_list = nav.find_elements(by=By.XPATH, value="./child::*")
            # retrieve child of nav list
            for e in next_page_list:
                a_list = e.find_elements(by=By.XPATH, value="./child::*")
                # iterate on element in each nav button
                for a in a_list:
                    # if element is next page
                    if a.get_attribute("aria-label"):
                        if a.get_attribute("aria-label") == "Next Page":
                            next_page = a.get_attribute("href")
    # stop script if no page left
    if next_page == "":
        watchdog = False

    # delete cookies window
    # all_buttons = driver.find_elements(by=By.TAG_NAME, value="button")
    # for button in all_buttons:
    #     if (button.get_attribute("id")) == "onetrust-reject-all-handler":
    #         button.click()
    #         break

    # go to connexion page
    # connexion = driver.find_element(by=By.XPATH, value="//a[text()='Connexion']")
    # connexion.click()

    # input("Press Enter to continue...")


    # get list of offer
    offer_div = driver.find_element(by=By.ID, value="mosaic-provider-jobcards")
    offer_table = offer_div.find_element(by=By.TAG_NAME, value="ul")
    offers = offer_table.find_elements(by=By.XPATH, value="./child::*")

    # iterate in offer list
    for offer in offers:
        # retrieve all link into offer element
        clickables = offer.find_elements(by=By.TAG_NAME, value="a")
        # iterate into all link element
        for clickable in clickables:
            if clickable.get_attribute("href"):
                # check if link element is job link
                if clickable.get_attribute("class") == "jcs-JobTitle css-jspxzf eu4oa1w0":
                    # open link in a new tab
                    driver.execute_script("window.open('"+clickable.get_attribute("href")+"');")
                    child = driver.window_handles[1]
                    driver.switch_to.window(child)
                    time.sleep(3)
                    # TODO: apply
                    all_buttons = driver.find_elements(by=By.TAG_NAME, value="a")
                    all_buttons += driver.find_elements(by=By.TAG_NAME, value="button")
                    for button in all_buttons:
                        # click on apply button
                        try:
                            if "postuler" in str(button.get_attribute("aria-label")).casefold():
                                try:
                                    # driver.execute_script("window.scrollTo(0, 500)")
                                    driver.execute_script("arguments[0].scrollIntoView(true);", button)
                                    time.sleep(2)
                                    if button.tag_name == "a":
                                        driver.get(button.get_attribute("href"))
                                    elif button.tag_name == "button":
                                        button.click()
                                        break
                                except:
                                    print("cannot postule button not handle")
                        except:
                            print("")
                    # click on continue button
                    time.sleep(randrange(5))
                    has_continue = True
                    timeout = 0
                    while has_continue is True and timeout != 5:
                        print("try: ", timeout, " continue: ", has_continue)
                        time.sleep(randrange(5))
                        try:
                            all_input = driver.find_elements(by=By.TAG_NAME, value="input")
                            print(all_input)
                            for input in all_input:
                                if input.get_attribute("class") == "css-anc3lu e1jgz0i3" and input.get_attribute("type") == "number":
                                    input.send_keys("10")
                                if input.get_attribute("name") == "jobTitle":
                                    input.send_keys("software engineer")
                                if input.get_attribute("name") == "companyName":
                                    input.send_keys("gearo")
                            all_continue_buttons = driver.find_elements(by=By.TAG_NAME, value="button")
                            all_continue_buttons += driver.find_elements(by=By.TAG_NAME, value="a")
                            has_continue = False
                            for continue_button in all_continue_buttons:
                                if "continue" in continue_button.get_attribute("class").casefold() or "candidature" in continue_button.get_attribute("class").casefold():
                                    driver.execute_script("window.scrollTo(0, 500)")
                                    has_continue = True
                                    if continue_button.tag_name == "a":
                                        driver.get(continue_button.get_attribute("href"))
                                    elif continue_button.tag_name == "button":
                                        continue_button.click()
                                    break
                        except:
                            print("cannot continue button not handle")
                            # driver.close()
                        timeout += 1
                        time.sleep(randrange(5))
                    driver.close()
                    # return to main window
                    driver.switch_to.window(driver.window_handles[0])
        # /!\ web site detect scraping bot if each action is seperate by same time /!\
        time.sleep(randrange(5))
    # go to next page
    driver.get(next_page)