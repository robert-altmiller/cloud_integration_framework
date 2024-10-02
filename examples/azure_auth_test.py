# library and file imports
from helpers.generic_helpers import *


# class_obj class is in --> resources --> azure_resources
def azure_auth_api_test(azure_auth_obj = None):
    # test to create an oauth2 auth token

    # get azure oauth2 token and print it
    oauth2token = azure_auth_obj.get_oauth2_token()
    print(f"azure oauth2 token: {oauth2token}\n")
