from flask import Flask, render_template, request, jsonify
from selenium import webdriver
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import time
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("main.html")
@app.route('/num', methods=['POST'])
def msg():
    textnum=request.form['textnum']
    print(textnum)
    time.sleep(30)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--disable-gpu')
    #chrome_options.add_argument("window-size=1024x768")
    chrome_options.add_argument("--no-sandbox")
    
    
    #The Below line is set for linux , it does need to scan the qrcode again to signin 
    #This line differ for different os
    chrome_options.add_argument("--user-data-dir=~/.config/google-chrome")
    
    chrome_options.add_argument("--profile-directory=Default")

    chrome_options = webdriver.ChromeOptions()
    chromedriver= webdriver.Chrome('chromedriver',options=chrome_options)
    chromedriver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(chromedriver, 600)
    target = [textnum]#,"second phone number"]
    string = "Message sent using Python!!! "
    xpath='//*[@id="side"]/div[1]/div/label/div/div[2]'
    title = wait.until(EC.presence_of_element_located((By.XPATH, xpath))) 
    for target_no in target :
        title.send_keys(target_no + Keys.ENTER)
        chromedriver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(string + Keys.ENTER)
        print(target_no,"Sent")
    return "Completed"
    
    




if __name__ == '__main__':
	app.run(host="0.0.0.0",debug=True)