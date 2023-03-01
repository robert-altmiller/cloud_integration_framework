# library and file imports
from examples.text_analytics import *
from config import *


# environment variables initialization
config = Config().get_config_vars()


def main():
    """
    run main program
    """

    # this class is in helpers --> azure_helpers.py
    ta_class_obj = textanalytics(config)
    ta_data_json = azure_text_analytics_unit_test(config, ta_class_obj)
    write_to_local(
        data = ta_data_json,
        folderpath = config["DATA_LOCATION"] + "/text_analytics_example", 
        filename = "text_analytics_json.txt"
    )


main()
