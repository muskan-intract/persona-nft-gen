import os, json
import urllib.parse
import boto3
import mimetypes
from io import BytesIO
from logdata import Log_data
from selenium import webdriver
from htmlTemplates.configurations import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


s3_client = boto3.client(service_name='s3', region_name=os.getenv('REGION_NAME'), aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'), aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))

def imageGen(tmp_dir,rendered_html,record,specificProcessId):
    recordId = record.get("_id")
    chainId = record.get("chainId")
    tokenId = record.get("tokenId")
    userAddress = record.get("userAddress")
    nftContractAddress = record.get("nftContractAddress")
    tier = record.get("tier")
    log_dict = {"process_id": specificProcessId, "message": f"Starting image generation for {recordId}."}
    Log_data(log_dict)
    try:
        file_path = userAddress + nftContractAddress + tokenId + str(chainId) + ".png"
        screenshot_file_path = os.path.join(tmp_dir, file_path)
        configWidth = configuraitons.get(chainId).get(tier).get('width',None)
        configHeight = configuraitons.get(chainId).get(tier).get('height',None)
        width = configWidth if configWidth else 375
        height = configHeight if configHeight else 545
        log_dict['width'] = width
        log_dict['height'] = height
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--single-process')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--window-size=1920,1080")  # Set the desired resolution
        options.add_argument("--force-device-scale-factor=3")  # Set the desired pixel density
        options.add_argument("--blink-settings=imagesEnabled=true")  # Enable image loading

        service = Service(executable_path=os.getenv('CHROME_DRIVER_PATH'))
        driver = webdriver.Chrome(service=service,options=options)
        encoded_html = urllib.parse.quote(rendered_html)
        driver.get("data:text/html;charset=utf-8," + encoded_html)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'div')))
        driver.set_window_size(width, height)
        driver.get_screenshot_as_file(screenshot_file_path)
        driver.quit()
        log_dict['screenshot_completes'] = 'screen shot completed successfully.'
        Log_data(log_dict)
        # get s3 imageURL
        imagePath = ''
        if(chainId == ZKEVM_CHAIN_ID):
            imagePath = f"persona-nfts/images/{os.getenv('ENVIRONMENT').lower()}/{userAddress}.png"
        else:
            imagePath = f"persona-nfts/images/{os.getenv('ENVIRONMENT').lower()}/{chainId}/{nftContractAddress}/image/{tokenId}.png"         
        imageUrl = save_to_cloud(screenshot_file_path, imagePath, mimetypes.guess_type(imagePath)[0],os.getenv('BUCKET_NAME'))
        log_dict['image_url'] = imageUrl
        #get s3 metadataURL
        metaDataPath = ''
        if(chainId == ZKEVM_CHAIN_ID):
            metaDataPath = f"persona-nfts/metadata/{os.getenv('ENVIRONMENT').lower()}/{tokenId}"
        else:
            metaDataPath = f"persona-nfts/metadata/{os.getenv('ENVIRONMENT').lower()}/{chainId}/{nftContractAddress}/metadata/{tokenId}"
        metadata = {
            'name': 'Intract Persona NFT',
            'description': f"This NFT represents the on-chain persona of Intract user {userAddress}",
            'image': imageUrl,
            'external_url': 'https://intract.io/',
        }
        metadata_json = json.dumps(metadata)
        metadata_bytes = metadata_json.encode('utf-8')
        metadata_url = save_to_cloud(BytesIO(metadata_bytes), metaDataPath, 'application/json',os.getenv('BUCKET_NAME'))
        log_dict['metadata_url'] = metadata_url
        return {
            "status":"SUCCESS",
            "specificProcessId" : specificProcessId,
            "recordId":recordId,
            "imageUrl":imageUrl,
            "metadataUrl":metadata_url
        }
    except Exception as e:
        log_dict['error'] = str(e)
        return {
            "status":"FAILED",
            "error":str(e),
            "specificProcessId" : specificProcessId,
            "recordId":recordId
        }
    finally:
        Log_data(log_dict)
        # Delete directory
        if(os.path.exists(screenshot_file_path)):
            os.remove(screenshot_file_path)
        

def save_to_cloud(file_path, aws_path, content_type, bucket_name):
        aws_path = aws_path
        content_type = mimetypes.guess_type(aws_path)[0]
        s3_client.upload_file(
            Filename=file_path,
            Bucket=bucket_name,
            Key=aws_path,
            ExtraArgs={'ContentType': content_type}
        )

        url = f"https://{bucket_name}.s3.amazonaws.com/{aws_path}"
        url = url.replace(f"https://{bucket_name}.s3.amazonaws.com", 'https://static.highongrowth.xyz/')
        return url        