# library and file imports
from examples.main import *
from config import *


# environment variables initialization
config = Config()
config.print_config_vars()
config = config.get_config_vars()



def run_test(cloudservicename = None):
    """has a list of the api tests to run"""
    runtests = {
        "azure_storage": False,
        "azure_textanalytics": True,
        "aws_s3bucket": True,
        "aws_lamda": False,
        "gcp_bigquery": False
    }
    return runtests[cloudservicename]


def main():
    """
    run main program
    """

    # textanalytics class is in helpers --> azure_helpers.py
    if  run_test("azure_textanalytics") == True:
        ta_class_obj = textanalytics(config)
        ta_data_json = azure_text_analytics_api_test(ta_class_obj)
        # write json results to a local file
        write_to_local(
            data = ta_data_json,
            folderpath = config["LOCAL_DATA_FOLDER"] + "/text_analytics_example", 
            filename = "text_analytics_json.json"
        )


    # s3bucket class is in helpers --> aws_helpers.py
    if run_test("aws_s3bucket") == True:
        s3_class_obj = s3bucket(config)
        aws_s3_bucket_api_test(s3_class_obj)


main()
