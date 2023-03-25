# library and file imports
from helpers.generic_helpers import *


def az_storage_to_aws_s3(config, azstorageobj, s3obj):

    # download azure storage account files locally
    localpaths = download_azure_storage_account_files_locally(config, azstorageobj)
    upload_to_s3_bucket(config, s3obj, localpaths)
    delete_local_dirs(f'{azstorageobj.config["LOCAL_DATA_FOLDER"]}/azurestorage/{config["azstorageacctname"]}')


def download_azure_storage_account_files_locally(config, azstorageobj):
    
    # get list of all blobs in container (format: container/filepath/filename)
    # and download all the blobs locally under the data folder while maintaining blob folder structure in container
    # this function can run locally on a scaled virtual machine hosted in a kubernetes container 
    print("downloads azure storage account blobs locally:\n")
    azstoragelocalfilepaths = []
    for globalcontainer in config["azglobalcontainers"]:
        azstorageobj.set_azure_storage_acct_container_name_override(globalcontainer)
        blobs = azstorageobj.get_blob_list()
        filepaths = []
        for blob in blobs:
            container = blob.container # container
            folderpath = blob.name.rsplit('/', 1)[0] # blob folderpath
            filename = blob.name.split("/")[-1] # blob filename
            if folderpath == filename: folderpath = "/"
            azstoragelocalfilepath = azstorageobj.download_blob_write_locally(config["azstorageacctname"], container, folderpath, filename)
            print(azstoragelocalfilepath)
            azstoragelocalfilepaths.append(azstoragelocalfilepath)
    return azstoragelocalfilepaths


def upload_to_s3_bucket(config, s3obj, localpaths):

    # upload s3 local files to a mew aws s3 bucket while maintaining the local folder stucture from another s3 bucket
    print("uploading local files to s3 bucket:\n")
    for localpath in localpaths:
        s3bucketfilepath = localpath.split(config["azstorageacctname"])[1].strip("/")
        print(s3bucketfilepath)
        s3obj.upload_s3_bucket_file_from_local(config["s3bucketname"], localpath, s3bucketfilepath)
        # cleanup local azure storage account blob files
        delete_local_file(localpath)
