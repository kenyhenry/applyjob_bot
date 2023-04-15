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
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from random import randrange

apply_nb = 0
page = 1
offer_nb = 1

# f = open('not_applied.txt', 'a')

indeed_home = "https://fr.indeed.com/jobs?q=nodejs&l=France&vjk=e6c0ee2350ed43f0"

#indeed search by word
binary = FirefoxBinary("/Applications/Firefox.app/Contents/MacOS/firefox-bin")
driver = webdriver.Firefox(firefox_binary = binary)
driver.get(indeed_home)
time.sleep(randrange(5))

#applications
main_window = driver.execute_script('return window.name')

# get list of offer
offer_div = driver.find_element(by=By.ID, value="mosaic-provider-jobcards")
offer_table = offer_div.find_element(by=By.TAG_NAME, value="ul")
offers = offer_table.find_elements(by=By.XPATH, value="./child::*")

# iterate in offer list
for offer in offers:
    # retrieve all link into offer element
    clickables = offer.find_elements(by=By.TAG_NAME, value="a")
    no_offer = True
    # iterate into all link element
    for clickable in clickables:
        if clickable.get_attribute("href"):
            # check if link element is job link
            if clickable.get_attribute("class") == "jcs-JobTitle css-jspxzf eu4oa1w0":
                # open link in a new tab
                driver.execute_script("window.open('"+clickable.get_attribute("href")+"');")
                child = driver.window_handles[1]
                print(child)
                driver.switch_to.window(child)
                driver.close()
                # TODO: apply
                offer_nb += 1
                page += 1
                no_offer = False
                # return to main window
                driver.switch_to.window(driver.window_handles[0])
    if no_offer is True:
        # find a way to push offer into a file it into file
        # no need because offer disappear when apply
        print("no offer link")
    # /!\ web site detect scraping bot if each action is seperate by same time /!\
    time.sleep(randrange(5))

# go to the next page

# retrive nav element list
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
                        # open link of element
                        next_page = a.get_attribute("href")
                        driver.get(next_page)