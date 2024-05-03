import logging
import uuid
from datetime import datetime

class Log_data(object):
    def __init__(self, data):
        data['log_id']=str(uuid.uuid4())
        data['log_time']=str(datetime.now())
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        file = 'logs.log'
        logging.basicConfig(filename = f'{file}',format="%(message)s",level=logging.INFO)
        logging.info(data)