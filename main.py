# library and file imports
from config import *
from examples import *


# environment variables initialization
config = Config()
config.print_config_vars()
config = config.get_config_vars()



def run_test(cloudservicename = None):
    """has a list of the api tests to run"""
    runtests = {
        "azure_auth": False,
        "azure_storage": False,
        "azure_textanalytics": True,
        "aws_s3bucket": False,
        "aws_lamda": False,
        "gcp_bigquery": False
    }
    return runtests[cloudservicename]


def main():
    """
    run main program
    """

    # azure text analytics keyphrases anb sentiment
    # text analytics (ta) class is in resources --> azure_resources
    if  run_test("azure_textanalytics") == True:
        azure_ta_obj = textanalytics(config)
        ta_data_json = azure_text_analytics_api_test(azure_ta_obj)
        # write json results to a local file
        fldr_path = config["LOCAL_DATA_FOLDER"] + "/text_analytics_example"
        fname = "text_analytics.json"
        write_to_local(
            data = ta_data_json,
            folderpath = fldr_path, 
            filename = fname
        )
        print(f"local text analytics results are stored: {fldr_path}/{fname}")


    # s3 bucket integration
    # s3bucket class is in resources --> aws_resources
    if run_test("aws_s3bucket") == True:
        aws_s3_obj = s3bucket(config)
        aws_s3_bucket_api_test(aws_s3_obj)

    
    # azure oauth2 authentication token creation
    # azureauth class is in resources --> azure_resources
    if run_test("azure_auth") == True:
        azure_auth_obj = azureauth(config)
        azure_auth_api_test(azure_auth_obj)


main()
