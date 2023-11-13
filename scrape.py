import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import pandas as pd
import os
import shutil
import tkinter as tk
from tkinter import messagebox

options = webdriver.ChromeOptions()
prefs = {'download.default_directory': 'Default Download Location'}
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('prefs', prefs)

# Provide the correct path to the ChromeDriver executable
chrome_driver_path = '/Users/thomaswu/Documents/chromedriver-mac-x64/chromedriver'  
service = Service(chrome_driver_path)
service.start()
driver = webdriver.Remote(service.service_url, options=options)  # Pass options here

driver.get("https://www.usaswimming.org/times/individual-times-search")
df = pd.read_csv('100FREESCY.csv')



# adv = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Times_TimesSearchDetail_Index_Div-1-Advanced-Search"]')))
# print("found")
# driver.execute_script("arguments[0].click();", adv)

#changing year to ALL
dropdown = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='k-widget k-dropdown' and @aria-owns='Times_TimesSearchDetail_Index_Div-1-ReportingYearKey_listbox']")))
dropdown.click()
for _ in range(2):
    dropdown.send_keys(Keys.UP)
dropdown.send_keys(Keys.RETURN)


for index, row in df.iterrows():
    # Going through list of top times and searching US swimmers
    if row['="IsForeign"'] == '="False"':
        name = row['="FullName"'].split(", ")
        firstname_real = name[1]
        lastname_real = name[0]



        firstname = driver.find_element(By.XPATH, '//*[@id="Times_TimesSearchDetail_Index_Div-1-FirstName"]')
        firstname.send_keys(firstname_real)

        lastname = driver.find_element(By.XPATH, '//*[@id="Times_TimesSearchDetail_Index_Div-1-LastName"]')
        lastname.send_keys(lastname_real)

        

        # event = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='k-widget k-dropdown' and @aria-owns='Times_TimesSearchDetail_Index_Div-1-SwimEventKey_listbox']")))
        # event.click()
        # for _ in range(2):
        #     dropdown.send_keys(Keys.DOWN)
        # dropdown.send_keys(Keys.RETURN)


        findtimes = driver.find_element(By.XPATH, '//*[@id="Times_TimesSearchDetail_Index_Div-1-Search"]')
        findtimes.click()

        WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.CLASS_NAME, "k-loading-image")))
    
        try:
            download = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Times_TimesSearchDetail_Index_Div-1-DownloadButton"]')))
            download.click()
            
            firstname.clear()
            lastname.clear()
        except:
            # # error = driver.find_element(By.XPATH, '//*[@id="Times_TimesSearchDetail_Index_Div-1-Times"]/p')
            # error = driver.find_element(By.XPATH, '//*[@id="Times_TimesSearchDetail_Index_Div-1-DownloadButton"]')
            # # erorr_2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Times_TimesSearchDetail_Index_Div-1-Times"][contains(text(), "No times found")]')))
            firstname.clear()
            lastname.clear()
            continue