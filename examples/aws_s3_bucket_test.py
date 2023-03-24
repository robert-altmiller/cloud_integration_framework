# library and file imports
from helpers.generic_helpers import *


# class_obj class is in --> resources --> aws_resources
def aws_s3_bucket_api_test(aws_s3_obj = None):
    # test aws s3 bucket api functionality
    
    # create an s3 bucket and then delete it
    aws_s3_obj.set_s3_bucket_name_override("raqo-bucket") # optional
    aws_s3_obj.create_s3_bucket()
    aws_s3_obj.delete_s3_bucket()


    # print all the s3 buckets
    buckets = aws_s3_obj.get_s3_buckets_list()
    print(f"all s3 buckets listed: {buckets}\n")


    # read a file with filename override (e.e. red wine quality)
    print("read a file with filename override (e.e. red wine quality):")
    aws_s3_obj.set_s3_bucket_name_override("ra-aws-bucket-dev") # optional
    aws_s3_obj.set_s3_bucket_folder_path_override("Bronze/kaggle_datasets/red_wine_quality_dataset/") #optional
    aws_s3_obj.set_s3_bucket_file_name_override("winequality-red.csv") # optional
    df = aws_s3_obj.read_s3_bucket_file("csv")
    print(df)
    print("\n")


    # get a list of all the files and folders in an s3 bucket and create two lists: 
    # one for file paths and the other for folder paths
    print("all file and folder paths:")
    aws_s3_obj.set_s3_bucket_name_override("ra-aws-bucket-dev")
    s3_file_paths = aws_s3_obj.get_s3_bucket_files_folders_paths(return_type = "file_paths")
    print(f"all file_paths: {s3_file_paths}")
    s3_folder_paths = aws_s3_obj.get_s3_bucket_files_folders_paths(return_type = "folder_paths")
    print(f"all folder_paths: {s3_folder_paths}\n")


    # download all the s3 files locally under the data folder while maintaining s3 folder structure in s3 bucket
    # this function can run locally on a scaled virtual machine hosted in a kubernetes container 
    print("downloads s3 bucket files locally:")
    bucket = "ra-aws-bucket-dev"
    s3localfilepaths = []
    for s3filepath in s3_file_paths:
        s3folderpath = s3filepath.rsplit('/', 1)[0] # s3 file folderpath
        s3filename = s3filepath.split("/")[-1] # s3 file filename
        if s3folderpath == s3filename: s3folderpath = "/"
        s3localfilepath = aws_s3_obj.download_s3_bucket_file_write_locally(bucket, s3folderpath, s3filename)
        s3localfilepaths.append(s3localfilepath)
    print("\n")


    # upload s3 local files to a mew aws s3 bucket while maintaining the local folder stucture from another s3 bucket
    print("uploading local files to s3 bucket:")
    frombucket = "ra-aws-bucket-dev"
    tobucket = "ra-bucket-migrate"
    for s3localfilepath in s3localfilepaths:
        s3bucketfilepath = s3localfilepath.split(frombucket)[1].strip("/")
        aws_s3_obj.upload_s3_bucket_file_from_local(tobucket, s3localfilepath, s3bucketfilepath)
        # cleanup local s3 files
        delete_local_file(s3localfilepath)
    # clean up local s3 directories
    delete_local_dirs(f'{aws_s3_obj.config["LOCAL_DATA_FOLDER"]}/s3bucket/{frombucket}')