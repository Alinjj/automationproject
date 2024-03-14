import os

class Data:
    def __init__(self, driver):
        self.driver = driver
    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")