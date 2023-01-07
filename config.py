import os

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5785034384:AAFyR6fLGeC1zdzNTC4kJ4rP_R6UN-wdq-o")
    
    API_ID = int(os.environ.get("API_ID", "15823382"))
    
    API_HASH = os.environ.get("API_HASH", "016d5e115a06ddfb6121823d72ae4d8c")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 500
    
    CHUNK_SIZE = int(128)

    HTTP_PROXY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "5104293442"))

    SESSION_NAME = "UploadLinkToFileBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://W9Uyj61afEXSw601:W9Uyj61afEXSw601@cluster0.zsxso.mongodb.net/?retryWrites=true&w=majority")

    MAX_RESULTS = "50"
