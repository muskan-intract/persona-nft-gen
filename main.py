import time
from db import check_mongo_connection
from imageGeneration.controller import imageGenerator

def start_server():
    # Starting Server
    print("Starting server...")
    # time.sleep(1)
    print("Server started.")

# Main entry point
if __name__ == "__main__":
    if check_mongo_connection():
        start_server()
        # while(True):
        try:
            imageGenerator()
            time.sleep(10)   
        except Exception as e:
            print("Error in main loop:", e)
    else:
        print("Cannot start server due to MongoDB connection failure.")
     