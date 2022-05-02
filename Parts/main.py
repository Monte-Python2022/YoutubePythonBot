from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import undetected_chromedriver as uc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains #Figure out how to use this
import requests
import base64
import random



def comment_and_like_video(driver,links, comment_list):
    for link in links:
        driver.get(link)
        time.sleep(5)
        like_button = driver.find_element(By.XPATH,'//*[@id="top-level-buttons-computed"]/ytd-toggle-button-renderer[1]').get_attribute("class")  # Looks at if like button has been pressed. If it has active in the name, then it is already liked.
        html_nightmare = like_button.split()
        if not "style-default-active" in html_nightmare:  # Likes the video if it has not already been liked.
            driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[6]/div[1]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div[1]/ytd-toggle-button-renderer[1]/a/yt-icon-button').click()  # This will click the like button for the video.
        driver.find_element(By.ID, "placeholder-area").click()  ##This selected youtube comment box, COMMENT BOX NEEDS TO BE CLICKED
        comment = random.choice(comment_paragraph)
        driver.find_element(By.ID, "contenteditable-root").send_keys(comment)  ##Types in Comment
        time.sleep(3)  ##Just tells system to wait a second, to aviod google bot dectections
        driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[1]/ytd-comments-header-renderer/div[5]/ytd-comment-simplebox-renderer/div[3]/ytd-comment-dialog-renderer/ytd-commentbox/div[2]/div/div[4]/div[5]/ytd-button-renderer[2]/a/tp-yt-paper-button').click()  # Clicks the post comment.

def file_to_comment_paragraph(nowner = "Monte-Python2022",nrepo = "YoutubePythonBot", npath = "Nice Comments File"):   #Lets user add their own github comment file. Leave blank for mine.
    owner = nowner
    repo = nrepo
    path = npath
    comment_list = []
    response = requests.get(f'https://api.github.com/repos/{owner}/{repo}/contents/{path}')
    data = response.json()
    b64_data = base64.b64decode(data['content'])
    final_decoded = b64_data.decode('ascii')
    for line in final_decoded.splitlines():
        nline = line
        comment_list.append(nline)
    return comment_list
#Begains of user input loop

links = ['https://youtu.be/qPfhp6jxMjA', 'https://youtu.be/shSb9B5K0KQ']
print("Please CopyPaste your Youtube links here (one link per line). Type DONE when complete. ")
#while True:
#    x = input()
#    if x == "DONE":
#        break
#    else:
#        links.append(x)
#print(links)

comment_paragraph = file_to_comment_paragraph()
comment = random.choice(comment_paragraph)
print(comment)

import requests
from IPython.display import display,HTML
from ipywidgets import interact_manual

subreddits=['ama','aww','news','worldnews', 'politics','todayilearned','explainlikeimfive','writingprompts','upliftingnews','wholesomememes','freecompliments','happy','financialadvice','breadit']
subreddits.sort()
# Step 2: Write code here

def title_graber(subreddit):
    string = ""
    url = f"https://www.reddit.com/r/{subreddit}.json"
    myheaders = {'User-Agent' : 'ist256.lesson10.homework:v1.0 (by /u/wjhiggin)'}
    response = requests.get(url, headers = myheaders)
    response.raise_for_status()
    data = response.json()
    for i in range(25):
        string = string + data['data']['children'][i]['data']['title'] + "\n"
    return string

def Sentiment_processer(text):
    url = 'http://text-processing.com/api/sentiment/'
    payload = {'text' : text}
    response = requests.post(url, data = payload)
    sentiment = response.json()
    return sentiment

@interact_manual(subreddit=subreddits)
def main(subreddit):
    titles = title_graber(subreddit)
    sentiment = Sentiment_processer(titles)
    print(f"Overall sentiment of {subreddit} is {sentiment['label']}")
