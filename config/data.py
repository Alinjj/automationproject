import os
from dotenv import load_dotenv

load_dotenv()
class Data:
    def __init__(self, driver):
        self.driver = driver
    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")