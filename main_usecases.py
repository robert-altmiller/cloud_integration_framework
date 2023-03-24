# library and file imports
from config import *
from use_cases import *


# environment variables initialization
config = Config()
config.print_config_vars()
config = config.get_config_vars()


def run_test(usecase_category = None, usecase_name = None):
    """has a list of the api tests to run"""
    runusecases= {
        "migration":{
            "s3_azurestorage": False,
            "azurestorage_s3": True ,       
            "s3_gcp": False,
            "gcp_s3": False,
            "gcp_azurestorage": False,
            "azurestorage_gcp": False
        }
    }
    return runusecases[usecase_category][usecase_name]



def main():
    """
    run main program
    """

    # azure storage account migration to s3 bucket
    if run_test("migration", "azurestorage_s3") == True:

        migrationconfig = {
            # a list of all the containers to download from a single azure storage account
            "azstorageacctname": "rastorageaccount",
            "azglobalcontainers": ["bronze", "silver", "gold"],
            # s3 bucket to copy the azure storage account files to
            "awstobucket": "ra-aws-bucket-dev"
        }

        az_azure_storage_obj = azurestorageaccount(config)
        aws_s3_obj = awss3bucket(config)
        az_storage_to_aws_s3(migrationconfig, az_azure_storage_obj, aws_s3_obj)


    # azure storage account migration to s3 bucket
    if run_test("migration", "s3_azurestorage") == True:

        migrationconfig = {
            # a list of all the containers to download from a single azure storage account
            "s3bucketname": "ra-aws-bucket-dev",
            "azglobalcontainers": ["bronze", "silver", "gold"],
        }

        az_azure_storage_obj = azurestorageaccount(config)
        aws_s3_obj = awss3bucket(config)
        az_storage_to_aws_s3(migrationconfig, az_azure_storage_obj, aws_s3_obj)


if __name__ == "__main__":
    main()