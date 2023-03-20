# library and file imports
from .azure_base import *


# azure storage account class functions
class azurestorageaccount(azureclass):
    
    # class constructor    
    def __init__(self, config):
        # get all configuration variables
        self.filename = None
        super().__init__(config)
    

    def set_azure_storage_acct_name_override(self, az_storage_account_name = None):
        """set a new azure storage account name"""
        self.config["AZURE_STORAGE_ACCOUNT_NAME"] = az_storage_account_name


    def set_azure_storage_acct_container_name_override(self, az_storage_account_container_name = None):
        """set a new azure storage account container name"""
        self.config["AZURE_STORAGE_ACCOUNT_CONTAINER"] = az_storage_account_container_name


    def set_azure_storage_acct_folder_path_override(self, az_storage_acct_foldpath = None):
        """set a new azure storage account folder path"""
        self.config["AZURE_STORAGE_ACCOUNT_FOLDER_PATH"] = az_storage_acct_foldpath


    def set_azure_storage_acct_file_name_override(self, az_storage_acct_filename = None):
        """set a new azure storage account file name"""
        self.config["AZURE_STORAGE_ACCOUNT_FILE_NAME"] = az_storage_acct_filename


    # def create_azure_storage_account_client(self):
    #     """create azure storage account client"""
    #     s3_client = boto3.client(
    #         self.config["AWS_S3_BUCKET_TYPE"],
    #         aws_access_key_id = self.config["AWS_S3_BUCKET_ACCESS_KEY_ID"], 
    #         aws_secret_access_key = self.config["AWS_S3_BUCKET_SECRET_KEY_ID"],
    #         region_name = self.config["AWS_S3_REGION"]
    #     )
    #     return s3_client