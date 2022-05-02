from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import undetected_chromedriver as uc
import requests
import base64
import random


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

def intall_chrome_to_system():
    webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # -If you dont have it downloaded.
    print("Please restart the program if you have having issues. Once downloaded, you do not need to run again")

def run_uc_crhome():
    option = webdriver.ChromeOptions()
    option.add_argument('--disable-blink-features=AutomationControlled')
    option.add_argument("window-size=1280,800")
    option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = option)
    return driver

def login_into_youtube(driver, email_username = "iamnotarobotpython@gmail.com", email_password = "Python!Please_give_me_100_on_this_project@2022!YoutubeBot"):
    driver.get("https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin")  #Google Login Page
    driver.find_element(By.ID, "identifierId").send_keys(email_username)
    time.sleep(1.5)
    driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d" ).click()
    time.sleep(1)
    driver.find_element(By.NAME, "password").send_keys(email_password)
    time.sleep(.5)
    driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d" ).click()
    time.sleep(1)

def comment_and_like_video(driver,links, comment_list):
    for link in links:
        driver.get(link)
        time.sleep(5)
        like_button = driver.find_element(By.XPATH,'//*[@id="top-level-buttons-computed"]/ytd-toggle-button-renderer[1]').get_attribute("class")  # Looks at if like button has been pressed. If it has active in the name, then it is already liked.
        html_nightmare = like_button.split()
        if not "style-default-active" in html_nightmare:  # Likes the video if it has not already been liked.
            driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[6]/div[1]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div[1]/ytd-toggle-button-renderer[1]/a/yt-icon-button').click()  # This will click the like button for the video.
        driver.find_element(By.ID, "placeholder-area").click()  ##This selected youtube comment box, COMMENT BOX NEEDS TO BE CLICKED
        comment = random.choice(comment_list)
        driver.find_element(By.ID, "contenteditable-root").send_keys(comment)  ##Types in Comment
        time.sleep(3)  ##Just tells system to wait a second, to aviod google bot dectections
        driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[1]/ytd-comments-header-renderer/div[5]/ytd-comment-simplebox-renderer/div[3]/ytd-comment-dialog-renderer/ytd-commentbox/div[2]/div/div[4]/div[5]/ytd-button-renderer[2]/a/tp-yt-paper-button').click()  # Clicks the post comment.
        time.sleep(1)


links = ["https://youtu.be/shSb9B5K0KQ", "https://youtu.be/qPfhp6jxMjA"]


#Main Code Section
owner = "Monte-Python2022"
repo = "YoutubePythonBot"
path = "Nice Comments File"
email_username = "iamnotarobotpython@gmail.com"
email_password = "Python!Please_give_me_100_on_this_project@2022!YoutubeBot"

print("Hello, welcome to my Youtube Bot. Please fill out the following information for the bot to work.")
print("")


driver = run_uc_crhome()
login_into_youtube(driver, email_username, email_password)
comment_list = file_to_comment_paragraph(owner, repo, path) #Allow user to import their own nice comments if they want. If they just wanna use mine, leave those fields blank.
comment_and_like_video(driver, links, comment_list)
print("Program Has Finished. Have a Good Day!")




