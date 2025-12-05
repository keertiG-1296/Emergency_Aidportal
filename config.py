import os
class Config:
    # Database configuration
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_USER = os.environ.get('DB_USER', 'root')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', 'MYSQL')
    DB_NAME = os.environ.get('DB_NAME', 'emergency_aidportal')
    
    # Flask configuration
    SECRET_KEY = os.environ.get('SESSION_SECRET', 'dev_secret_key')
    DEBUG = True
    
    # Uploads configuration
    UPLOAD_FOLDER = 'static/uploads'