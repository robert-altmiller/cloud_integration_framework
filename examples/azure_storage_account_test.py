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
    print("downloads azure storage account blobs locally:")
    storageacctname = "rastorageaccount"
    globalcontainers = ["bronze", "silver", "gold"] # a list of all the containers to download from
    azstoragelocalfilepaths = []
    for globalcontainer in globalcontainers:
        azure_storage_account_obj.set_azure_storage_acct_container_name_override(globalcontainer)
        blobs = azure_storage_account_obj.get_blob_list()
        filepaths = []
        for blob in blobs:
            # filepaths.append(f"{blob.container}/{blob.name}")
            container = blob.container # container
            folderpath = blob.name.rsplit('/', 1)[0] # blob folderpath
            filename = blob.name.split("/")[-1] # blob filename
            if folderpath == filename: folderpath = "/"
            azstoragelocalfilepath = azure_storage_account_obj.download_blob_write_locally(storageacctname, container, folderpath, filename)
            azstoragelocalfilepaths.append(azstoragelocalfilepath)
    print("\n")


    # upload local files to azure storage account container while maintaining the local folder stucture
    print("uploading local files to azure storage account container:")
    storageacctname = "rastorageaccount"
    for azstoragelocalfilepath in azstoragelocalfilepaths:
        blobfilepath1 = azstoragelocalfilepath.split(storageacctname)[1].strip("/")
        container = blobfilepath1.split("/")[0]
        blobfilepath2 = blobfilepath1.split(container)[1].strip("/")
        azure_storage_account_obj.upload_blob_from_local(storageacctname, container, azstoragelocalfilepath, blobfilepath2, True)
        # cleanup local azure storage account blob files
        delete_local_file(azstoragelocalfilepath)
    # clean up local azure storage account directories
    delete_local_dirs(f'{azure_storage_account_obj.config["LOCAL_DATA_FOLDER"]}/azurestorage/{storageacctname}')
    print("\n")