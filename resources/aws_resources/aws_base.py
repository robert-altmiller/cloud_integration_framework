# library and file imports
from helpers.generic_helpers import *


# aws class (main-class)
class awsclass:

    # class constructor    
    def __init__(self, config):
        # get all configuration variables
        self.config = config

    def aws_global_user_id_override(self, global_user_id = None):
        """set a new aws global user id"""
        self.config["AWS_GLOBAL_USER_ID"] = global_user_id

    
    def aws_user_key_override(self, global_user_key = None):
        """set a new aws global user key"""
        self.config["AWS_GLOBAL_USER_KEY"] = global_user_key


    def aws_region_override(self, global_region = None):
        """set a new aws global region"""
        self.config["AWS_GLOBAL_REGION"] = global_region