import os, time, sys
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from imageGeneration.functions import *
import urllib.parse
import base64


from selenium.webdriver.chrome.service import Service
from htmlTemplates.configurations import configuraitons

def test():
    try:
        tmp_dir = "outputs"
        os.makedirs(tmp_dir,exist_ok=True)  
        file_path = "blast2.png"
        screenshot_file_path = os.path.join(tmp_dir, file_path) 
        chainId = 81457 
        tier = "TIER2"
        html_template = configuraitons.get(chainId).get(tier).get('template')
        configWidth = configuraitons.get(chainId).get(tier).get('width',None)
        configHeight = configuraitons.get(chainId).get(tier).get('height',None)
        width = configWidth if configWidth else 375
        height = configHeight if configHeight else 545
        rendered_html = substitute_template(html_template, {}, ')hdgvb')
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--single-process')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--window-size=1920,1080")  # Set the desired resolution
        options.add_argument("--force-device-scale-factor=3")  # Set the desired pixel density
        options.add_argument("--blink-settings=imagesEnabled=true")  # Enable image loading

        service = Service(executable_path='/Users/muskan259/Documents/persona-nft-gen/chromedriver')
        driver = webdriver.Chrome(service=service,options=options)
        encoded_html = urllib.parse.quote(rendered_html)
        driver.get("data:text/html;charset=utf-8," + encoded_html)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'div')))
        driver.set_window_size(width, height)
        driver.get_screenshot_as_file(screenshot_file_path)
    except Exception as e:
        print(e)
    

test()    