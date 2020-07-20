# import requests
import time
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from youtube_transcript_api import YouTubeTranscriptApi

videos_list = []

urls = ["https://www.youtube.com/playlist?list=PLRD7N-Zrj2DMOLTG7t9E-vJo35BzeTwVG",
        "https://www.youtube.com/playlist?list=PLRD7N-Zrj2DNUHnLq67aStjGGCy3p0VgC",
        "https://www.youtube.com/playlist?list=PLRD7N-Zrj2DNE6S2AsY71GuuFgkRuzpWw",
        "https://www.youtube.com/playlist?list=PLRD7N-Zrj2DNrib0vUkSdWfSGFlzd3zua"
        ]

user_agent = {'User-agent': 'Mozilla/5.0'}

for url in urls:
    options = webdriver.ChromeOptions()
    options.add_argument('-headless')
    driver = webdriver.Chrome('./chromedriver', options=options)
    driver.get(url)

    time.sleep(1)
#     response = requests.get(url, headers = user_agent)
    elem = driver.find_element_by_tag_name("body")

    no_of_pagedowns = 50

    while no_of_pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.4)
        no_of_pagedowns-=1

    soup = BeautifulSoup(driver.page_source, 'html.parser')
#     print(soup)

    for video in soup.find_all('div', {'class': "style-scope ytd-playlist-video-renderer"}, id='content'):
        title = video.find('span', id='video-title')['title']
        id = video.find('a', {'class': 'yt-simple-endpoint style-scope ytd-playlist-video-renderer'})['href'][9:20]
        videos_list.append({'title': title, 'id': id})

videos_list = list({v['id']:v for v in videos_list}.values())


os.system('osascript -e beep')

no_transcript = ['pKYeAN-_wFI', 'kpIIBH5jEGs', 'mGLMi9kXTRI', 'aaLiLRVeaZA', 'waXb8QGdEYQ', '9g3CjQv5yec', 'NZ83rfAqWMw', 'PttKq0GcnoQ', 'GGEGF7cHmMU', 'ms5a_C7EeNk']

i=0

for video in videos_list:
    if video['id'] in no_transcript:
        continue
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video['id'])
    except:
        continue
    divide = "="
    for i in range(0, 10):
        divide = divide + "="
    print(divide)
    print("<|startoftext|>")
    print(video['title'])
    for line in transcript:
        print(line['text'])

    print("\n<|endoftext|>")
    i += 1
    os.system('osascript -e beep')
