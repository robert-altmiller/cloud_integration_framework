# library and file imports
from helpers.generic_helpers import *
from helpers.fuzzy_matching import *


def aws_s3_to_az_storage(config, azstorageobj, s3obj):

    # download azure storage account files locally
    localpaths = download_s3_bucket_files_locally(config, s3obj)
    upload_to_azure_storage(config, azstorageobj, localpaths)
    delete_local_dirs(f'{azstorageobj.config["LOCAL_DATA_FOLDER"]}/s3bucket/{config["s3bucketname"]}')


def download_s3_bucket_files_locally(config, s3obj):
    
    # get a list of all the files and folders in an s3 bucket and create two lists: 
    # one for file paths and the other for folder paths
    print("get all s3 bucket file and folder paths:\n")
    s3obj.set_s3_bucket_name_override(config["s3bucketname"])
    s3_file_paths = s3obj.get_s3_bucket_files_folders_paths(return_type = "file_paths")

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
    print("uploading local files to azure storage account container:\n")
    for localpath in localpaths:
        blobfilepath = localpath.split(config["s3bucketname"])[1].strip("/")


        # defines how to write the s3 bucket to the az storage acct -  in a single
        # az storage acct container or in multiple az storage acct containers.
        if config["toplevel_s3fldrs_as_containers_inazstorage"] == True:
            container = blobfilepath.split("/")[0]

            # we need a place to store root level files with no subdirectories
            if container == blobfilepath: container = config["azmigratecontainer"]
            else: blobfilepath = blobfilepath.split(container)[1].strip("/")

            # apply fuzzy logic to see if any top level s3 folders match config["fuzzymatchcontainers"] (e.g. bronze, silver, gold)
            # this helps with consolidating top level s3 folders in the same az storage account containers.
            if config["fuzzymatchcontainers"] != None:
                containersfuzzyscorelist = [{cont: get_fuzzy_match_score(container, cont)} for cont in config["fuzzymatchcontainers"]]
                containersfuzzyscoredict = {k: v for d in containersfuzzyscorelist for k, v in d.items()}
                if max(containersfuzzyscoredict.values()) > 100: # then fuzzy match found (e.g. bronze, silver, gold)
                    container = max(containersfuzzyscoredict, key=containersfuzzyscoredict.get)
                    print(f"fuzzy match container override is {container}\n")
                
        else: container = config["azmigratecontainer"]


        azstorageobj.upload_blob_from_local(config["azstorageacctname"], container, localpath, blobfilepath, True)
        # cleanup local azure storage account blob files
        delete_local_file(localpath)