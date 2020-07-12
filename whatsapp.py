from selenium import webdriver
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import time


def whatsapp_message():
    global wdriver
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--disable-gpu')
    #chrome_options.add_argument("window-size=1024x768")
    #chrome_options.add_argument("--no-sandbox")
    
    
    #The Below line is set for linux , it does need to scan the qrcode again to signin 
    #This line differ for different os
    chrome_options.add_argument("--user-data-dir=~/.config/google-chrome")
    
    chrome_options.add_argument("--profile-directory=Default")
    wdriver= webdriver.Chrome('chromedriver',options=chrome_options)
    wdriver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(wdriver, 600)
    #time.sleep(5)
    
    '''
    x_arg = '//span[contains(@title,' + target + ')]'
    title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg))) 
    title.click() 
    inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
    input_box = wait.until(EC.presence_of_element_located(( By.XPATH, inp_xpath))) 
    time.sleep(10)
    input_box.send_keys(string + Keys.ENTER)
    '''
    
    
    target = ["Target's Phone no. ","second phone number"]
    string = "Message sent using Python!!! "
    xpath='//*[@id="side"]/div[1]/div/label/div/div[2]'
    title = wait.until(EC.presence_of_element_located((By.XPATH, xpath))) 
    for target_no in target :
        title.send_keys(target + Keys.ENTER)
        wdriver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(string + Keys.ENTER)
        print(target_no,"Sent")
    return "Completed"

if __name__=="__main__":
    p=whatsapp_message()
    print(p)
    global wdriver
    wdriver.quit()