
# library and file imports
from helpers.main import *


# class_obj class is in --> azure_helpers.py
def aws_s3_bucket_api_test(s3_object = None):
    # test aws s3 bucket api functionality
    
    # print all the s3 buckets
    buckets = s3_object.get_s3_buckets_list()
    print(f"buckets: {buckets}")

    # read a file with filename override (red-win-quality)
    s3_object.set_s3_bucket_folder_path_override("ra-aws-bucket-dev") # optional
    s3_object.set_s3_bucket_folder_path_override("Bronze/kaggle_datasets/red_wine_quality_dataset/") #optional
    s3_object.set_s3_bucket_file_name_override("winequality-red.csv") # optional
    df = s3_object.read_s3_bucket_file("csv")
    print(df)

    # get a list of all the files and folders in an s3 bucks and create two lists
    # one for file paths and the other for folder paths
    s3_object.set_s3_bucket_folder_path_override("ra-aws-bucket-dev")
    files_folders_list = [file["Key"] for file in s3_object.get_s3_bucket_files_list()]
    file_paths = [file for file in files_folders_list if '/' in file[-1]]
    print(f"file_paths: {file_paths}")
    folder_paths = [file for file in files_folders_list if '/' not in file[-1]]
    print(f"folder_paths: {folder_paths}")