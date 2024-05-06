import os, uuid
import shutil
import concurrent.futures
from logdata import Log_data
from htmlTemplates.configurations import configuraitons
from imageGeneration.functions import *
from imageGeneration.service import *

def imageGenerator(processId):
    log_dict = {"message": "Starting image generation process...", "processId": processId}
    Log_data(log_dict)
    records = getPendingRecords(int(os.getenv("LIMIT",5)))
    log_dict['limit'] = os.getenv("LIMIT")
    log_dict['records'] = records
    Log_data(log_dict)
    if(len(records) == 0):
        return {"message": "No records to process"}
    max_workers = int(os.getenv("MAX_WORKERS",5))
    # Creating a thread pool with a maximum of 5 threads
    with concurrent.futures.ThreadPoolExecutor(max_workers) as executor:
        futures = []
        tmp_dir = "tmp"
        os.makedirs(tmp_dir,exist_ok=True)
        for record in records:
            recordId = record.get("_id")
            specificProcessId = str(uuid.uuid4())
            job_dict = {"specificProcessId": specificProcessId, "processId": processId, "recordId":recordId}
            Log_data(job_dict)
            metricsData = record.get("metrics",{})
            userAddress = record.get("userAddress")
            tier = record.get("tier")
            nftContractAddress = record.get("nftContractAddress")
            tokenId = record.get("tokenId")
            chainId = record.get("chainId")
            retryAttempts = record.get("retryCount",0)
            if(any(not var for var in [tier, nftContractAddress, tokenId, chainId, userAddress])):
                job_dict["message"] =  "Invalid Data in record"
                update_record_status(recordId,status="FAILED")
                Log_data(job_dict)
                continue
            if not configuraitons.get(chainId) or configuraitons[chainId].get(tier) is None:
                job_dict["message"] = "Invalid chain or tier configuration"
                update_record_status(recordId, status="FAILED")
                Log_data(job_dict)
                continue
            if retryAttempts >= int(os.getenv("MAX_RETRY_ATTEMPTS",3)):
                job_dict["message"] = "Max retry attempts reached"
                update_record_status(recordId, status="FAILED")
                Log_data(job_dict)
                continue
            html_template = configuraitons.get(chainId).get(tier).get('template')
            rendered_html = substitute_template(html_template, metricsData, userAddress)
            
            futures.append(executor.submit(imageGen,tmp_dir,rendered_html,record,specificProcessId))
        
        # Wait for all tasks to complete
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                result.get('specificProcessId')
                new_dict = {"message": "Processed record", "result": result, processId:processId}
                Log_data(new_dict)
                recordId = result.get('recordId')
                if result.get('status') == "SUCCESS":
                    recordId = result.get('recordId')
                    imageUrl = result.get('imageUrl')
                    metadataUrl = result.get('metadataUrl')
                    update_record_status(result.get('record'),"SUCCESS",imageUrl = imageUrl,metadataUrl = metadataUrl)
                    new_dict['message'] = 'updated Urls in record'
                else:
                    retryCount = retryAttempts + 1
                    new_dict['updated_retry_count'] = retryCount
                    update_record_status(recordId,retryCount = retryCount)
                Log_data(new_dict)    
            except Exception as e:
                log_dict = {"error in threads": str(e)}
                Log_data(log_dict)  

        # Clean up the temporary directory
        shutil.rmtree(tmp_dir)
    return {"message": "Processed all records"}