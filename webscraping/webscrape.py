# Program: webscrape.py
# Author: Jacob Storer
# Last Reviewed: 03/01/2021

# Libraries
import pandas # Pretty format
import requests
from time import sleep
from selenium import webdriver # Need because javascript populates the web page
from selenium.webdriver.common.keys import Keys # Keys
from selenium.webdriver.common.by import By     # Find 'by'
from selenium.webdriver.support.ui import WebDriverWait # Wait for elements to load
from selenium.webdriver.support import expected_conditions as EC # Expected conditions

from selenium.webdriver.firefox.options import Options  
options = Options()
options.set_headless(True) # newer webdriver versions
#############
# DEBUG
############
# options.set_headless(False) # newer webdriver versions

browser = webdriver.Firefox(options=options) # Firefox 

# Global Configuration
# Below is target web page for testing collection of data use cases.
# url = "https://www.auction.com/residential/Michigan/active_lt/auction_date_order,resi_sort_v2_st/y_nbs/"
url = 'https://www.auction.com/'
print("Booting up browser...")
# browser = webdriver.Firefox()   # Configure web driver
browser.get(url)                # Start browser

# Website Index 
print("Keying in state to search in... (MI)")
search_bar = browser.find_element_by_class_name('prompt')
search_bar.send_keys('MI' + Keys.RETURN)

list_dataset = []

# Capture main window frame
# main_window = browser.current_window_handle

# Main body loop
while(True):
    # Houses in Michigan
    print("Waiting until web links load on page...")
    try:
        houses = WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'root_link_1AwM'))
        )
    finally:
        # Make list page's links to houses
        house_urls = [
            elem.get_attribute('href') for elem in houses
        ]

    # print(len(houses))
    # print(houses)

    print("Iterating through web links...")
    for x in houses:
        dict_pandas = {}
        x.send_keys(Keys.CONTROL + Keys.RETURN)
        print("Pausing 2-seconds for window to load...")
        sleep(2)
        session_windows = browser.window_handles
        browser.switch_to_window(session_windows[1])
        print("grabbing info on active page...")
        tableArr = browser.find_elements_by_xpath(".//tr[@class='']")
        # print(tableArr)
        # print(type(tableArr))
        for w in tableArr:
            # print(x.text)
            # print(x.text.split('\n'))
            # print()
            tmp = "" # Clear
            tmp = w.text.split('\n')
            try:
                dict_pandas[tmp[0]] = tmp[1]
            except:
                pass

            try:
                dict_pandas[tmp[2]] = tmp[3]
            except:
                pass
                    
        # dict_pandas['Url'] = str(x.get_attribute('href'))
        # URL use browser.current_url
        print("Append list")
        list_dataset.append(dict_pandas)
        df = pandas.DataFrame(list_dataset)
        print(df)
        browser.close()
        browser.switch_to_window(session_windows[0]) # Redundancy
        # print(session_windows)

    # Get bottom navigation bar
    bot_navi = browser.find_element_by_class_name('index__pagination-container--f_38U') # Grabs bottom navigation bar
    valueArr = bot_navi.find_elements_by_xpath(".//a[@class='item']")
    pages_count = [
        elem.get_attribute('value') for elem in valueArr
    ]

    # print(bot_navi)
    # print(valueArr)
    # print(pages_count[-2])

    # Exit loop condition, grabbed every piece of data from houses
    if pages_count[-1] == pages_count[-2]:
        break
    else: 
        valueArr[-1].click()
        df = pandas.DataFrame(list_dataset)
        print(df)

print("Creating file...")
df.to_csv('output.csv')
print("Program finished...")
browser.quit()

##############
# LEGACY CODE
##############
'''
# Capture house list page
house_list_view = browser.current_url

for newLink in house_urls:
    # Open Link in new tab
    #browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + "t")
    browser.get(newLink)
    # Move to new tab
    #browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
    print("sleeping...")
    print("Grabbing relevant information...")
    sleep(0.5)
    print('NEXT!')
    print("page loaded")

# Open house list page
print("Opening house list page")
browser.get(house_list_view)

# Next page
'''
# browser.close()
    # browser.quit()

# Web driver configuration
# driver = webdriver.Firefox()
# html = driver.get(url) # Waits for 'onload' event, then continues program

# r = requests.get(url, headers = { 'User-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
# c = r.content

# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify())
# print("End test")
