# library and file imports
from helpers.generic_helpers import *



# class_obj class is in --> resources --> azure_resources
def azure_storage_account_api_test(azure_storage_account_obj = None):

    # create and delete a container
    new_container_name = "databricks"
    azure_storage_account_obj.create_container(new_container_name)
    azure_storage_account_obj.delete_container(new_container_name)

    
    # get list of all blobs in container (format: container/filepath/filename)
    # and download all the blobs locally under the data folder while maintaining blob folder structure in container
    # this function can run locally on a scaled virtual machine hosted in a kubernetes container 
    storageacctname = "rastorageaccount"
    globalcontainers = ["bronze", "silver", "gold"] # a list of all the containers to download from
    for globalcontainer in globalcontainers:
        azure_storage_account_obj.set_azure_storage_acct_container_name_override(globalcontainer)
        blobs = azure_storage_account_obj.get_blob_list()
        filepaths = []
        for blob in blobs:
            filepaths.append(f"{blob.container}/{blob.name}")
            container = blob.container # container
            folderpath = blob.name.rsplit('/', 1)[0] # blob folderpath
            filename = blob.name.split("/")[-1] # blob filename
            if folderpath == filename: folderpath = "/"
            azure_storage_account_obj.download_blob_write_locally(storageacctname, container, folderpath, filename)


