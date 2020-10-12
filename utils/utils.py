#CONSTANTS
import inspect

URL = "https://opensource-demo.orangehrmlive.com"
USERNAME = "Admin"
PASSWORD = "admin123"

def whomami():
    return inspect.stack()[1][3]