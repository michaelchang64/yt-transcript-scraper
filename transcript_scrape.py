import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# import pandas as pd

url = 'https://www.youtube.com/watch?v=iLMF6Dyd4GU'

options = webdriver.ChromeOptions()
# options.add_argument('-headless')
# driver = webdriver.Firefox(firefox_options=options)
driver = webdriver.Chrome('./chromedriver')
driver.get(url)

driver.implicitly_wait(3)

htmltag = driver.find_element(By.TAG_NAME, 'html')
# click_menu = driver.findElement(By.linkText)
menu_path = "//div[@id='menu-container']/div[@id='menu']/ytd-menu-renderer[1]/yt-icon-button[@id='button']"
click_menu = driver.find_element(By.XPATH, menu_path)

actions = ActionChains(driver)
actions.move_to_element(click_menu)
actions.click(click_menu)
actions.perform()

print("click_menu got clicked")

driver.implicitly_wait(10)

transcript_path = "//*[contains(text(), 'Open transcript')]"
click_transcript = driver.find_elements(By.XPATH, transcript_path)
actions.move_to_element(click_transcript[0])
print("moved")
actions.click(click_transcript[0])
actions.perform()
print("click_transcript got clicked")

# soup = BeautifulSoup(response.text, 'lxml')
# 
# results = soup.findAll("div", {"class": "cue style-scope ytd-transcript-body-renderer"})
# 
# print(results)
# print(soup)
