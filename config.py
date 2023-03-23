# library and file imports
import os
from dotenv import load_dotenv
from resources import *


# load .env environment file
load_dotenv()


class Config:
# configuration class definition

    # class constructor    
    def __init__(self):
        # local variables
        self.LOCAL_DATA_FOLDER = str(os.getenv('LOCAL_DATA_FOLDER'))
        self.ENVIRONMENT = str(os.getenv('ENVIRONMENT'))

        # AZURE VARIABLES

        # azure environment
        self.AZURE_TENANT_ID = str(os.getenv('AZURE_TENANT_ID'))
        self.AZURE_SUBSCRIPTION_ID = str(os.getenv('AZURE_SUBSCRIPTION_ID'))
        self.AZURE_RESOURCE_GROUP_NAME = str(os.getenv('AZURE_RESOURCE_GROUP_NAME'))
        self.AZURE_CLIENT_ID = str(os.getenv('AZURE_CLIENT_ID'))
        self.AZURE_CLIENT_SECRET = str(os.getenv('AZURE_CLIENT_SECRET'))

        # authentication
        self.AZURE_AUTHENTICATION_AUTHORITY = f"{str(os.getenv('AZURE_AUTHENTICATION_AUTHORITY'))}/{self.AZURE_TENANT_ID}"
        self.AZURE_AUTHENTICATION_GRANT_SCOPE = [str(os.getenv('AZURE_AUTHENTICATION_GRANT_SCOPE'))] # must be list
        
        # cogntive services
        self.AZURE_COG_SERVICES_RESOURCE_NAME = f"{str(os.getenv('AZURE_COG_SERVICES_RESOURCE_NAME'))}-{self.ENVIRONMENT}"
        self.AZURE_COG_SERVICES_BASE_URL = str(os.getenv('AZURE_COG_SERVICES_BASE_URL'))
        self.AZURE_COG_SERVICES_API_KEY = str(os.getenv('AZURE_COG_SERVICES_API_KEY'))
        
        # storage account
        self.AZURE_STORAGE_ACCOUNT_NAME = f"{str(os.getenv('AZURE_STORAGE_ACCOUNT_NAME'))}{self.ENVIRONMENT}"
        self.AZURE_STORAGE_ACCOUNT_CONTAINER = str(os.getenv('AZURE_STORAGE_ACCOUNT_CONTAINER'))
        self.AZURE_STORAGE_ACCOUNT_FOLDER_PATH = str(os.getenv('AZURE_STORAGE_ACCOUNT_FOLDER_PATH'))
        self.AZURE_STORAGE_ACCOUNT_FILE_NAME = str(os.getenv('AZURE_STORAGE_ACCOUNT_FILE_NAME'))
        self.AZURE_STORAGE_ACCOUNT_KEY = str(os.getenv('AZURE_STORAGE_ACCOUNT_KEY'))
        self.AZURE_STORAGE_ACCOUNT_CONN = f'DefaultEndpointsProtocol=https;AccountName={self.AZURE_STORAGE_ACCOUNT_NAME};AccountKey={self.AZURE_STORAGE_ACCOUNT_KEY};EndpointSuffix=core.windows.net'

        # AWS VARIABLES
        
        # aws environment

        self.AWS_GLOBAL_REGION = str(os.getenv('AWS_GLOBAL_REGION'))
        self.AWS_GLOBAL_USER_ID = str(os.getenv('AWS_GLOBAL_USER_ID'))
        self.AWS_GLOBAL_USER_KEY = str(os.getenv('AWS_GLOBAL_USER_KEY'))

        # s3 stprage account
        self.AWS_S3_REGION = str(os.getenv('AWS_S3_REGION'))
        self.AWS_S3_BUCKET_TYPE = str(os.getenv('AWS_S3_BUCKET_TYPE'))
        self.AWS_S3_BUCKET_NAME = f"{str(os.getenv('AWS_S3_BUCKET_NAME'))}-{self.ENVIRONMENT}"
        self.AWS_S3_BUCKET_FOLDER_PATH = str(os.getenv('AWS_S3_BUCKET_FOLDER_PATH'))
        self.AWS_S3_BUCKET_FILE_NAME = str(os.getenv('AWS_S3_BUCKET_FILE_NAME'))
        self.AWS_S3_BUCKET_ACCESS_KEY_ID = str(os.getenv('AWS_S3_BUCKET_ACCESS_KEY_ID'))
        self.AWS_S3_BUCKET_SECRET_KEY_ID = str(os.getenv('AWS_S3_BUCKET_SECRET_KEY_ID'))

        # GCP variables

        # format and print environment variables
        self.format_config_vars()
        

    def format_config_vars(self):
        """
        additional formatting for configuration variables
        this function is optional if you need it
        """
        return None


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