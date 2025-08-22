from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env file

class Data:
    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")