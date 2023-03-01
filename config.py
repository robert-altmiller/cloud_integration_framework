# library and file imports
import os
from dotenv import load_dotenv
from helpers.helpers import *


# load .env environment file
load_dotenv()


class Config:
# configuration class definition

    # class constructor    
    def __init__(self):
        # i/o variables
        self.DATA_LOCATION = os.getenv('DATA_LOCATION')
        # azure variables
        self.AZURE_COG_SERVICES_BASE_URL = os.getenv('AZURE_COG_SERVICES_BASE_URL')
        self.AZURE_COG_SERVICES_API_KEY = os.getenv('AZURE_COG_SERVICES_API_KEY')
        self.AZURE_COG_SERVICES_RESOURCE_NAME = os.getenv('AZURE_COG_SERVICES_RESOURCE_NAME')
        # aws variables
        self.AWS_S3_TYPE = os.getenv('AWS_S3_TYPE')
        self.AWS_S3_BUCKET_NAME = os.getenv('AWS_S3_BUCKET_NAME')
        # format environment variables
        self.format_config_vars()


    def format_config_vars(self):
        # format configuration variables
        self.DATA_LOCATION = str(self.DATA_LOCATION)
        self.AZURE_COG_SERVICES_BASE_URL = str(self.AZURE_COG_SERVICES_BASE_URL)
        self.AZURE_COG_SERVICES_API_KEY = str(self.AZURE_COG_SERVICES_API_KEY)
        self.AZURE_COG_SERVICES_RESOURCE_NAME = str(self.AZURE_COG_SERVICES_RESOURCE_NAME)
        self.AWS_S3_TYPE = str(self.AWS_S3_TYPE)
        self.AWS_S3_BUCKET_NAME = str(self.AWS_S3_BUCKET_NAME)


    def get_config_vars(self):
        # get class configuration variables
        config = Config()
        return vars(config)


    def print_config_vars(self):
        # get configuration variables in a python dictionary
        variables = self.get_config_vars()
        print("configuration variables:")
        vars_list = []
        for key, val in variables.items():
            print(f"{key}: {val}")
        print("\n")