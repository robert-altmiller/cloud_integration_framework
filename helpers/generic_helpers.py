# library and file imports
import os, json, shutil, re, string
from pathlib import Path
import pandas as pd


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


def read_file_with_pandas(filename = None, filetype = None):
    """read csv file using pandas"""
    if filetype.lower() == "csv":
        return pd.read_csv(filename)
    

def check_str_for_substr_and_replace(inputstr = None, substr = None):
    """remove a substring from a string input"""
    if substr in inputstr:
        return inputstr.replace(substr, '')
    else: return inputstr


def delete_local_file(filepath = None):
    """remove a local file"""
    os.remove(filepath)


def delete_local_dirs(folderpath = None):
    """remove local directories"""
    rootfolder = Path(__file__).parents[1]
    shutil.rmtree(f"{rootfolder}/{folderpath}")


def remove_invalid_chars(
        inputstr = None, 
        lowercase = False,
        uppercase = False,
        removenumbers = False,
        removespaces = False,
        removepunctuation = False,
        singledashes = False
    ):
    """remove all characters from python string besides letters dynamically"""
    if lowercase: inputstr = inputstr.lower()
    if uppercase: inputstr = inputstr.upper()
    if removenumbers: inputstr = re.sub(r'[0-9]', '', inputstr)
    if removespaces: inputstr = inputstr.replace(' ', '')
    if removepunctuation:
        punctuation = [punct for punct in str(string.punctuation)]
        punctuation.remove("-")
        for punct in punctuation:
            inputstr = inputstr.replace(punct, '')
    if singledashes: inputstr = re.sub(r'(-)+', r'-', inputstr)
    return inputstr
