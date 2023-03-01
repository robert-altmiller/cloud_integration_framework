# library and file imports
import os, json


def file_folder_exists(path = None):
    """
    check if a local file or folder exists
    """
    return os.path.exists(path)


def get_json_dumps(data = None):
    """get json dumps"""
    return json.dumps(data)


def get_json_dump(data = None):
    """get json dump"""
    return json.dump(data)


def get_json_load(data = None):
    """get json load"""
    return json.load(data)


def get_json_loads(data = None):
    """get json loads"""
    return json.loads(data)


def check_text_as_list(text = None):
    """
    checks and formats an input string as a python list
    """
    if type(text) == list: text_list = text
    else: text_list = [text]
    return text_list


def write_to_local(data = None, folderpath = None, filename = None):
    """write to a local file"""
    filepath = folderpath + "/" + filename
    if file_folder_exists(folderpath) == False:
    # then create the directory path recursively
        os.makedirs(folderpath)
    with open(filepath, "w") as f:
        f.write(data)