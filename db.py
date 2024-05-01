import os
from pymongo import MongoClient
from dotenv import load_dotenv

if os.getenv("ENVIRONMENT"):
    if os.getenv("ENVIRONMENT")=='PRODUCTION':
        os.environ["ENVIRONMENT_PATH"] = '.env.production'
    elif os.getenv("ENVIRONMENT")=='DEVELOPMENT':
        os.environ["ENVIRONMENT_PATH"] = '.env.development'
    elif os.getenv("ENVIRONMENT")=='STAGING':
        os.environ["ENVIRONMENT_PATH"] = '.env.staging'
    else:
        raise RuntimeError('InCorrect  Environment')
else:
    raise RuntimeError('Missing  Environment')
        
load_dotenv(dotenv_path=str(os.getenv('ENVIRONMENT_PATH')))

client = MongoClient(str(os.getenv("MONGO_URI")))
db = client[str(os.getenv("MONGO_DB_NAME"))]

def check_mongo_connection():
    try:
        client = MongoClient(str(os.getenv("MONGO_URI")))  # Connect to MongoDB server
        db = client[str(os.getenv("MONGO_DB_NAME"))]
        server_info = db.command('serverStatus')  # Execute a command to check server status
        print("MongoDB connection successful!")
        print("Server version:", server_info['version'])
        return True
    except Exception as e:
        print("MongoDB connection failed:", e)
        return False    