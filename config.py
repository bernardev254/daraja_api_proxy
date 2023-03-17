import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True
    URL = os.getenv("URL")
    TOKEN = os.getenv("TOKEN")
    

class TestingConfig(Config):
    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    DEBUG = True
    URL = os.getenv("URL")
    TOKEN = os.getenv("TOKEN")
    CLIENT_ID = os.getenv("CLIENT_ID")


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
    )