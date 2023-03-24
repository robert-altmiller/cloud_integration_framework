# library and file imports
from helpers.generic_helpers import *


def aws_s3_to_azure_storage(config, azstorageobj, s3obj):

    # download azure storage account files locally
    localpaths = download_s3_bucket_files_locally(config, azstorageobj)
    upload_to_azure_storage(config, azstorageobj, localpaths)
    delete_local_dirs(f'{azstorageobj.config["LOCAL_DATA_FOLDER"]}/s3bucket/{config["s3bucketname"]}')


def download_s3_bucket_files_locally(config, s3obj):
    
    # get a list of all the files and folders in an s3 bucket and create two lists: 
    # one for file paths and the other for folder paths
    print("get all s3 bucket file and folder paths:")
    s3obj.set_s3_bucket_name_override(config["s3bucketname"])
    s3_file_paths = s3obj.get_s3_bucket_files_folders_paths(return_type = "file_paths")
    print(f"all file_paths: {s3_file_paths}")
    s3_folder_paths = s3obj.get_s3_bucket_files_folders_paths(return_type = "folder_paths")
    print(f"all folder_paths: {s3_folder_paths}\n")


    # download all the s3 files locally under the data folder while maintaining s3 folder structure in s3 bucket
    # this function can run locally on a scaled virtual machine hosted in a kubernetes container 
    print("downloads s3 bucket files locally:")
    s3localfilepaths = []
    for s3filepath in s3_file_paths:
        s3folderpath = s3filepath.rsplit('/', 1)[0] # s3 file folderpath
        s3filename = s3filepath.split("/")[-1] # s3 file filename
        if s3folderpath == s3filename: s3folderpath = "/"
        s3localfilepath = s3obj.download_s3_bucket_file_write_locally(config["s3bucketname"], s3folderpath, s3filename)
        s3localfilepaths.append(s3localfilepath)
    return s3localfilepaths


def upload_to_azure_storage(config, azstorageobj, localpaths):
    
    # upload local files to azure storage account container while maintaining the local folder stucture
    print("uploading local files to azure storage account container:")
    for localpath in localpaths:
        blobfilepath1 = localpath.split(config["storageacctname"])[1].strip("/")
        container = blobfilepath1.split("/")[0]
        blobfilepath2 = blobfilepath1.split(container)[1].strip("/")
        azstorageobj.upload_blob_from_local(config["storageacctname"], container, localpath, blobfilepath2, True)
        # cleanup local azure storage account blob files
        delete_local_file(localpath)