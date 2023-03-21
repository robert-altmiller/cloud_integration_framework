# library and file imports
import os, pathlib
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
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

    
    def create_blob_service_client(self):
        """create azure storage blob service client"""
        return BlobServiceClient.from_connection_string(self.config["AZURE_STORAGE_ACCOUNT_CONN"])


    def create_container_client(self):
        """create azure storage account container client"""
        return self.create_blob_service_client().get_container_client(self.config["AZURE_STORAGE_ACCOUNT_CONTAINER"])


    def create_blob_client(self):
        """create azure storage account blob client"""
        return self.create_blob_service_client().get_blob_client(
            container = self.config["AZURE_STORAGE_ACCOUNT_CONTAINER"],
            blob = f'{self.config["AZURE_STORAGE_ACCOUNT_FOLDER_PATH"]}/{self.config["AZURE_STORAGE_ACCOUNT_FILE_NAME"]}'
        )
    
    def create_container(self, containername = None):
        """create azure storage account container"""
        try:
            self.create_blob_service_client().create_container(containername)
            print(f"container {containername} created successfully...")
        except: print(f"create container failed: container {containername} already exists...")


    def delete_container(self, containername = None):
        """delete azure storage account container"""
        try:
            self.create_blob_service_client().delete_container(containername)
            print(f"container {containername} deleted successfully...")
        except: print(f"delete container failed: container {containername} does not exist...")


    def get_blob_list(self):
        """get list of blobs in azure storage account container"""
        return self.create_container_client().list_blobs()


    def download_blob(self, container = None, filepath = None, filename = None):
        """download azure storage container blob"""
        self.set_azure_storage_acct_container_name_override(container)
        self.set_azure_storage_acct_folder_path_override(filepath)
        self.set_azure_storage_acct_file_name_override(filename)
        localpath = f"./data/blobs/{container}/{filepath}/"
        if not os.path.exists(localpath): os.makedirs(localpath)
        with open(f"{localpath}/{filename}", "wb") as my_blob:
            blob_data = self.create_blob_client().download_blob()
            blob_data.readinto(my_blob)
        print(f"{localpath}/{filename} written locally successfully")


    def upload_blob(self, blobpath):
        """upload a blob to an azure storage account container"""
        with open(blobpath, "rb") as data:
           self.create_container_client().upload_blob(name="my_blob", data = data)


    def delete_blob(self):
        """delete blob from azure storage account"""
        self.create_blob_client().delete_blob()



