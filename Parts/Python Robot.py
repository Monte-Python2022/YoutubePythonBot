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


#https://www.youtube.com/watch?v=Xjv1sY630Uc, may help with perment home for driver.




chrome_options = Options()

chrome_options.add_experimental_option("detach", True) #allows for the window to stay open, maybe add as option in final edit. Its not working with uc.
driver = uc.Chrome(use_subprocess = True, chrome_options = chrome_options)
#driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_options) #-If you dont have it downloaded.

driver.get("https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
email_username = "iamnotarobotpython@gmail.com"
email_password = "Python!Please_give_me_100_on_this_project@2022!YoutubeBot"

driver.find_element(By.ID, "identifierId").send_keys(email_username)
time.sleep(1.5)
driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d" ).click()
time.sleep(1)
driver.find_element(By.NAME, "password").send_keys(email_password)
time.sleep(.5)
driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d" ).click()
time.sleep(1)

#https://youtu.be/qPfhp6jxMjA,(Stop the bots), https://youtu.be/shSb9B5K0KQ (Stop the bots old).
link = "https://youtu.be/qPfhp6jxMjA"
Comment = ("First Automated Python Comment, Test 1")
action = webdriver.ActionChains(driver)

driver.get(link)
time.sleep(5)
like_button = driver.find_element(By.XPATH, '//*[@id="top-level-buttons-computed"]/ytd-toggle-button-renderer[1]').get_attribute("class")   #Looks at if like button has been pressed. If it has active in the name, then it is already liked.
html_nightmare = like_button.split()
if not "style-default-active" in html_nightmare: #Likes the video if it has not already been liked.
    driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[6]/div[1]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div[1]/ytd-toggle-button-renderer[1]/a/yt-icon-button').click()  # This will click the like button for the video.

print(html_nightmare)




##//*[@id="top-level-buttons-computed"]/ytd-toggle-button-renderer[1]
#//*[@id="button"]

#//*[@id="top-level-buttons-computed"]/ytd-toggle-button-renderer[4]



##driver.find_element(By.ID, "placeholder-area").click()                  ##This selected youtube comment box, COMMENT BOX NEEDS TO BE CLICKED
##driver.find_element(By.ID, "contenteditable-root").send_keys(Comment)   ##Types in Comment
##time.sleep(3)                                                           ##Just tells system to wait a second, to aviod google bot dectections
##driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[1]/ytd-comments-header-renderer/div[5]/ytd-comment-simplebox-renderer/div[3]/ytd-comment-dialog-renderer/ytd-commentbox/div[2]/div/div[4]/div[5]/ytd-button-renderer[2]/a/tp-yt-paper-button').click() #Clicks the post comment.

#//*[@id="button"]


time.sleep(1000)











