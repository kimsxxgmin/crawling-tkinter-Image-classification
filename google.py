from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By   #추가한 코드
import time
import urllib.request
import os

## create Directory
def createDirectory(directory):
    current_path = os.getcwd()

    try:
        os.mkdir(current_path + "/" + directory)
    except OSError:
        print("Error: Failed to create the directory.")

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
elem = driver.find_element(By.NAME, "q")   
elem.send_keys("single animal")  
elem.send_keys(Keys.RETURN)

##Scroll

SCROLL_PAUSE_TIME = 2

last_height = driver.execute_script("return document.body.scrollHeight")  # Get scroll height

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(SCROLL_PAUSE_TIME)

new_height = driver.execute_script("return document.body.scrollHeight")

if new_height == last_height:
    driver.find_element(By.CLASS_NAME, "mye4qd").click()


createDirectory("image")
current_path = os.getcwd()

images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd") 
count = 1
for image in images:
    image.click()
    time.sleep(2)
    imgUrl = driver.find_element(By.CLASS_NAME, "n3VNCb").get_attribute("src")  
    path = str(current_path) + "/image/" 
    urllib.request.urlretrieve(imgUrl, path + str(count) + ".jpg")
    count = count + 1
    if count > 50:  #50장까지 다운제한
        break 
driver.close()