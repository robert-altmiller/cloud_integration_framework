
# library and file imports
import boto3
# from pandas_aws import get_client
# from pandas_aws.s3 import get_df_from_keys
from  helpers.generic_helpers import *

# aws class (main-class)
class awsclass:

    # class constructor    
    def __init__(self, config):
        # get all configuration variables
        self.config = config


# s3 class functions (sub-class)
class s3bucket(awsclass):

    # class constructor    
    def __init__(self, config):
        # get all configuration variables
        super().__init__(config)


    def set_s3_bucket_name_override(self, s3_bucketname = None):
        """set a new s3 bucket name"""
        self.config["AWS_S3_BUCKET_NAME"] = s3_bucketname


    def set_s3_bucket_folder_path_override(self, s3_folderpath = None):
        """set a new s3 folder path name"""
        self.config["AWS_S3_BUCKET_FOLDER_PATH"] = s3_folderpath


    def set_s3_bucket_file_name_override(self, s3_filename = None):
        """set a new s3 file name"""
        self.config["AWS_S3_BUCKET_FILE_NAME"] = s3_filename


    def create_s3_client(self):
        """create s3 client"""
        s3_client = boto3.client(
            self.config["AWS_S3_BUCKET_TYPE"],
            aws_access_key_id = self.config["AWS_S3_BUCKET_ACCESS_KEY_ID"], 
            aws_secret_access_key = self.config["AWS_S3_BUCKET_SECRET_KEY_ID"],
            region_name = self.config["AWS_S3_REGION"]
        )
        return s3_client


    def create_s3_session(self):
        """create s3 session"""
        session = boto3.Session(
            aws_access_key_id = self.config["AWS_S3_BUCKET_ACCESS_KEY_ID"], 
            aws_secret_access_key = self.config["AWS_S3_BUCKET_SECRET_KEY_ID"]
        )
        return session.client(self.config["AWS_S3_BUCKET_TYPE"])


    def get_s3_buckets_list(self):
        """fetch the list of existing S3 buckets"""
        buckets = self.create_s3_client().list_buckets() 
        bucketlist = []
        for bucket in buckets["Buckets"]: bucketlist.append(bucket["Name"])
        return bucketlist


    def get_s3_bucket_files_list(self):
        """list s3 bucket files"""
        s3_session = self.create_s3_session()
        return s3_session.list_objects(Bucket = self.config["AWS_S3_BUCKET_NAME"])["Contents"]


    def read_s3_bucket_file(self, file_type = None):
        """read a file from s3 bucket"""
        s3_object = self.create_s3_client().get_object(
            Bucket = self.config["AWS_S3_BUCKET_NAME"],
            Key = self.config["AWS_S3_BUCKET_FOLDER_PATH"] + self.config["AWS_S3_BUCKET_FILE_NAME"]
        )
        return read_file_with_pandas(s3_object["Body"], file_type)
