
# library and file imports
import boto3
from .aws_base import *



# s3 class functions (sub-class)
class awss3bucket(awsclass):

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
            aws_access_key_id = self.config["AWS_GLOBAL_USER_ID"], 
            aws_secret_access_key = self.config["AWS_GLOBAL_USER_KEY"]
        )
        return session.client(self.config["AWS_S3_BUCKET_TYPE"])


    def create_s3_resource(self):
        """create s3 resource"""
        s3_resource = boto3.resource(
            self.config["AWS_S3_BUCKET_TYPE"],
            region_name = self.config["AWS_S3_REGION"],
            aws_access_key_id = self.config["AWS_GLOBAL_USER_ID"], 
            aws_secret_access_key = self.config["AWS_GLOBAL_USER_KEY"]   
        )
        return s3_resource


    def create_s3_bucket(self):
        """create s3 bucket"""
        try:
            self.create_s3_client().create_bucket(
                Bucket = self.config["AWS_S3_BUCKET_NAME"],
                CreateBucketConfiguration = {'LocationConstraint': self.config["AWS_S3_REGION"]}   
            )
            print(f'aws s3 bucket created successfully: {self.config["AWS_S3_BUCKET_NAME"]}\n')
        except: print(f'aws s3 bucket already exists: {self.config["AWS_S3_BUCKET_NAME"]}\n')


    def delete_s3_bucket(self):
        """delete s3 bucket"""
        try:
            bucket = self.create_s3_resource().Bucket(self.config["AWS_S3_BUCKET_NAME"])
            bucket.objects.all().delete()
            bucket.delete()
            print(f'aws s3 bucket and all files deleted successfully: {self.config["AWS_S3_BUCKET_NAME"]}\n')
        except: print(f'aws s3 bucket cannot be deleted: {self.config["AWS_S3_BUCKET_NAME"]}\n')


    def get_s3_buckets_list(self):
        """fetch the list of existing S3 buckets"""
        buckets = self.create_s3_client().list_buckets()
        bucketlist = []
        for bucket in buckets["Buckets"]: bucketlist.append(bucket["Name"])
        return bucketlist


    def get_s3_bucket_objects_list(self):
        """list s3 bucket objects"""
        s3_session = self.create_s3_session()
        return s3_session.list_objects(Bucket = self.config["AWS_S3_BUCKET_NAME"])["Contents"]


    def get_s3_bucket_files_folders_paths(self, return_type = "file_paths"):
        """
        get s3 bucket file or folder paths
        return_type = "file_paths" or "folder_paths"
        default return type is file_paths
        """
        files_folders_list = [file["Key"] for file in self.get_s3_bucket_objects_list()]
        resultsdict = {
            "file_paths": [file for file in files_folders_list if '/' not in file[-1]],
            "folder_paths": [file for file in files_folders_list if '/' in file[-1]]
        }
        return resultsdict[return_type]


    def read_s3_bucket_file(self, file_type = None):
        """read a file from s3 bucket"""
        s3_object = self.create_s3_client().get_object(
            Bucket = self.config["AWS_S3_BUCKET_NAME"],
            Key = self.config["AWS_S3_BUCKET_FOLDER_PATH"] + self.config["AWS_S3_BUCKET_FILE_NAME"]
        )
        return read_file_with_pandas(s3_object["Body"], file_type)


    def gets3_file_path(self):
        """get s3 file path for download from s3 bucket"""
        return f'{self.config["AWS_S3_BUCKET_FOLDER_PATH"]}/{self.config["AWS_S3_BUCKET_FILE_NAME"]}'


    def download_s3_file(self, localfilepath = None):
        """download s3 bucket file"""
        s3_file_path = check_str_for_substr_and_replace(self.gets3_file_path(), "//")
        self.create_s3_resource().Bucket(self.config["AWS_S3_BUCKET_NAME"]).download_file(s3_file_path, localfilepath)


    def upload_s3_file(self, localfilepath = None, s3filepath = None):
        """upload local file to s3 bucket"""
        self.create_s3_resource().Bucket(self.config["AWS_S3_BUCKET_NAME"]).upload_file(localfilepath, s3filepath)


    def download_s3_bucket_file_write_locally(self, bucket = None, folderpath = None, filename = None):
        """
        download s3 bucket file maintain s3 bucket folder structure locally
        return local file path each time this function is called
        """
        self.set_s3_bucket_name_override(bucket)
        self.set_s3_bucket_folder_path_override(folderpath)
        self.set_s3_bucket_file_name_override(filename)
        localpath = check_str_for_substr_and_replace(f'./{self.config["LOCAL_DATA_FOLDER"]}/s3bucket/{bucket}/{folderpath}', "//")
        if not os.path.exists(localpath): os.makedirs(localpath)
        localfilepath = f"{localpath}/{filename}" 
        with open(localfilepath, "wb") as my_s3_file:
            self.download_s3_file(localfilepath)   
        print(f"{localfilepath} written locally successfully....\n")
        return localfilepath


    def upload_s3_bucket_file_from_local(self, bucket = None, localfilepath = None, s3filepath = None):
        """upload local file to s3 bucket and maintain local folder structure"""
        self.set_s3_bucket_name_override(bucket)
        self.upload_s3_file(localfilepath, s3filepath)
        print(f"{localfilepath} uploaded to s3 bucket {bucket}: {s3filepath} successfully....\n")