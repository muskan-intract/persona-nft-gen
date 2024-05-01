import time
import uuid
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def html_to_image(rendered_template_path,record):
    try:
        gvhdbn
        x = uuid.uuid4()
        print(f"{x}before",datetime.now())
        time.sleep(10)  
        print(f"{x}after",datetime.now())
        print("yes")
    except Exception as e:
        return {"status":"FAILED","error":str(e),"record":record.get('_id')}