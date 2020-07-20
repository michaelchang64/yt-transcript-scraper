# import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from youtube_transcript_api import YouTubeTranscriptApi

videos_list = []

urls = ["https://www.youtube.com/playlist?list=PLMBTl5yXyrGQfhjt0Efk3LWo7cmxk41n9",
        "https://www.youtube.com/playlist?list=PLMBTl5yXyrGSa67JeYb6ctt1gCvL9BdEX",
        "https://www.youtube.com/playlist?list=PLMBTl5yXyrGQ68Ny1mXCAaSwbjpcVwm49",
        ]

user_agent = {'User-agent': 'Mozilla/5.0'}

for url in urls:
    driver.webdriver.Chrome('./chromedriver')
#     options = webdriver.ChromeOptions()
#     options.add_argument('-headless')
#     driver = webdriver.Chrome('./chromedriver', options=options)
    driver.get(url)

    time.sleep(1)
#     response = requests.get(url, headers = user_agent)
    elem = driver.find_element_by_tag_name("body")

    no_of_pagedowns = 10
    
    while no_of_pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
        no_of_pagedowns-=1

    for video in driver.find_elements(By.TAG_NAME, 'tr'):
        videos_list.append(video['data-video-id'])

# videos_list = list(dict.fromkeys(videos_list))
print(len(videos_list))
print(videos_list)
# raw_transcript = YouTubeTranscriptApi.get_transcript("iLMF6Dyd4GU")
# 
# for line in raw_transcript:
#     print(line["text"])
