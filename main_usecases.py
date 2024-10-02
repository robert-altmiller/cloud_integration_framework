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
            "s3_azurestorage": True,
            "azurestorage_s3": False,       
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
            # az storage account which needs to be migrated 
            "azstorageacctname": "rastorageaccount",
            # a list of all the containers to download from a single azure storage account (must be all lowercase)
            "azglobalcontainers": ["bronze", "silver", "gold"],
            # s3 bucket to migrate the storage account containers to
            "s3bucketname": "ra-aws-bucket-dev",
            # this parameter will write each az storage account container as a folder in a single s3 bucket
            # if set to TRUE each az storage account container will be created as an individual folder in a single s3 bucket
            # if set to FALSE each az storage container will be created as an individual s3 buckets
            "toplevel_azstoragecontainers_as_folders_ins3": True,

        }
        az_storage_obj = azurestorageaccount(config)
        aws_s3_obj = awss3bucket(config)
        az_storage_to_aws_s3(migrationconfig, az_storage_obj, aws_s3_obj)


    # s3 bucket migration to azure storage account
    if run_test("migration", "s3_azurestorage") == True:

        migrationconfig = {
            # s3 bucket which needs to be migrated
            "s3bucketname": "ra-bucket-migrate", # MANDATORY
            # storage account to migrate s3 bucket to
            "azstorageacctname": "rastorageaccount", # MANDATORY
            # storage account container to migrate s3 bucket to (mandatory)
            "azmigratecontainer": "s3-migration-container", # MANDATORY
            # this parameter will write the top level s3 folders as new containers in the azure storage account 
            # if set to TRUE top level s3 bucket folders will be created as individual az storage account containers.  Individual root level files will be copied into migrationconfig["azmigratecontainer"]
            # if set to FALSE top level s3 bucket folders will be created individual folders in a single az storage account container (e.g. migrationconfig["azmigratecontainer"])
            "toplevel_s3fldrs_as_containers_inazstorage": True, # OPTIONAL
            # this parameter is used to consolidate s3 folders similar to names below into the same az container if toplevel_s3fldrs_as_containers_inazstorage = True
            # DEFAULT VALUE IS None, could also be ["bronze", "silver", "gold"]
            "fuzzymatchcontainers": ["bronze", "silver", "gold"] # OPTIONAL
        }
        az_storage_obj = azurestorageaccount(config)
        aws_s3_obj = awss3bucket(config)
        aws_s3_to_az_storage(migrationconfig, az_storage_obj, aws_s3_obj)


if __name__ == "__main__":
    main()