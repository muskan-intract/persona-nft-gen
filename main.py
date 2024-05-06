import time, uuid
from logdata import Log_data
from db import check_mongo_connection
from imageGeneration.controller import imageGenerator

def start_server():
    # Starting Server
    Log_data({"message": "Starting server..."})
    # time.sleep(1)
    Log_data({"message": "server started..."})

# Main entry point
if __name__ == "__main__":
    if check_mongo_connection():
        start_server()
        while(True):
            try:
                processId = str(uuid.uuid4())
                log_dict = {"message": "Image generation process started.", "processId": processId}
                Log_data(log_dict)
                result = imageGenerator(processId)
                log_dict['result'] = result
                log_dict['message'] =  "Image generation process completed."
                Log_data(log_dict)
                time.sleep(60)   
            except Exception as e:
                Log_data({"error in main loop":str(e)})
    else:
        Log_data({"Error":"Cannot start server due to MongoDB connection failure."})
     