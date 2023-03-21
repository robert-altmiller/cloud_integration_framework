# library and file imports
from helpers.generic_helpers import *



# class_obj class is in --> resources --> azure_resources
def azure_storage_account_api_test(azure_storage_account_obj = None):

    # create and delete a container
    new_container_name = "abc"
    azure_storage_account_obj.create_container(new_container_name)
    azure_storage_account_obj.delete_container(new_container_name)
    
    
    # get list of all blobs in container (format: container/filepath/filename)
    blobs = azure_storage_account_obj.get_blob_list()
    filepaths = []
    for blob in blobs: filepaths.append(f"{blob.container}/{blob.name}")
    print(filepaths)