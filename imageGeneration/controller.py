import os
import subprocess
import concurrent.futures
from htmlTemplates.mapping import configuraitons
from imageGeneration.functions import *
from imageGeneration.service import *

def imageGenerator():
    try:
        records = getPendingRecords(int(os.getenv("LIMIT",10)))
        has_documents = False
        for _ in records:
            has_documents = True
            break
        if not has_documents:
            return "No records to process"
        tmp_dir = "xyz"
        os.makedirs(tmp_dir, exist_ok=True)
        # Creating a thread pool with a maximum of 5 threads
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = []
            for record in records:
                # print(record)
                metricsData = record.get("metrics",{})
                userAddress = record.get("userAddress")
                tier = record.get("tier")
                nftContractAddress = record.get("nftContractAddress")
                tokenId = record.get("tokenId")
                chainId = record.get("chainId")
                if(any(not var for var in [tier, nftContractAddress, tokenId, chainId, userAddress])):
                    print("Invalid Data in record")
                    update_record_status(record.get("_id"),"FAILED")
                    continue
                if not configuraitons.get(chainId) or configuraitons[chainId].get(tier) is None:
                    print("Invalid chain or tier configuration")
                    update_record_status(record.get("_id"), "FAILED")
                    continue
                html_template = configuraitons.get(chainId).get(tier)
                rendered_html = substitute_template(html_template, metricsData, userAddress)
                rendered_template_path = os.path.join(tmp_dir, f'{record.get("_id")}_template.html')
                subprocess.run(["chmod", "775", str(tmp_dir)])
                with open(rendered_template_path, "w") as html_file:
                    html_file.write(rendered_html)
                
                futures.append(executor.submit(html_to_image, rendered_template_path,record))
            
            # Wait for all tasks to complete
            for future in concurrent.futures.as_completed(futures):
                try:
                    print(future.result())
                except Exception as e:
                    print(e)    
    except Exception as e:
        print(e)
    finally:
        # Delete directory
        os.rmdir(tmp_dir)