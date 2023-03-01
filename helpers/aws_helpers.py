
# library and file imports
import boto3


# aws class (main-class)
class awsclass:

    # class constructor    
    def __init__(self, config):
        # get all configuration variables
        self.config = config


# s3 class functions (sub-class)
class S3Class(awsclass):

    # class constructor    
    def __init__(self, config):
        # get all configuration variables
        super().__init__(config)


    def create_s3_client():
        """
        create s3 client
        """
        s3_client = boto3.client("s3")
