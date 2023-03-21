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
            "azurestorage_s3": False ,       
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


if __name__ == "__main__":
    main()