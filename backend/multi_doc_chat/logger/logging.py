import logging 
import os 
from datetime import datetime


LOG_DIR = "logs" #Creates folder where logs will be stored.


os.makedirs(LOG_DIR, exist_ok=True) #Automatically creates logs folder if missing.


log_file = os.path.join(
    LOG_DIR, 
    f"app_{datetime.now().strftime('%Y_%m_%d')}.log" #Creates daily log file.
)

logging.basicConfig(#it controls Log format, Log Location and Log severity level
    filename=log_file,
    format="[%(asctime)s] %(levelname)s - %(name)s - %(message)s",
    level=logging.INFO
)


logger = logging.getLogger("multi_doc_chat") #logger = getLogger() Creates reusable logger object across project.