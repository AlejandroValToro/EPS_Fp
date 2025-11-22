import os

class Config:
    DB_USER = "user_ptyhon"
    DB_PASSWORD = "Clas3s1Nt2024_!"
    DB_HOST = "localhost"
    DB_PORT = "3307"
    DB_NAME = "EPS"
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    ENCRYPTION_KEY = os.environ.get('ENCRYPTION_KEY') or b'8k9L5_5y7P3x1Z0a2B4c6D8e0F2g4H6j8K0m2N4p6Q8='
