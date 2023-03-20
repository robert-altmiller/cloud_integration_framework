# library and file imports
from helpers.generic_helpers import *


# class_obj class is in --> azure_helpers.py
def aws_s3_bucket_api_test(aws_s3_obj = None):
    # test aws s3 bucket api functionality
    
    # create an s3 bucket and then delete it
    aws_s3_obj.set_s3_bucket_name_override("raqo-bucket") # optional
    aws_s3_obj.create_s3_bucket()
    aws_s3_obj.delete_s3_bucket()

    # print all the s3 buckets
    buckets = aws_s3_obj.get_s3_buckets_list()
    print(f"buckets: {buckets}")

    # read a file with filename override (e.e. red wine quality)
    aws_s3_obj.set_s3_bucket_name_override("ra-aws-bucket-dev") # optional
    aws_s3_obj.set_s3_bucket_folder_path_override("Bronze/kaggle_datasets/red_wine_quality_dataset/") #optional
    aws_s3_obj.set_s3_bucket_file_name_override("winequality-red.csv") # optional
    df = aws_s3_obj.read_s3_bucket_file("csv")
    print(df)

    # get a list of all the files and folders in an s3 bucket and create two lists: 
    # one for file paths and the other for folder paths
    aws_s3_obj.set_s3_bucket_name_override("ra-aws-bucket-dev")
    files_folders_list = [file["Key"] for file in aws_s3_obj.get_s3_bucket_files_list()]
    file_paths = [file for file in files_folders_list if '/' not in file[-1]]
    print(f"file_paths: {file_paths}")
    folder_paths = [file for file in files_folders_list if '/' in file[-1]]
    print(f"folder_paths: {folder_paths}")