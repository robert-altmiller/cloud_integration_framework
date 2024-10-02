from fuzzywuzzy import fuzz

def fuzzy_ratio(x, y):
    """
    calculates the edit distance between some ordering of the x and y strings
    using the difflib.ratio (e.g. Levenstein distance)
    returns the ratio of type float.
    """
    return fuzz.ratio(x, y)

 
def fuzzy_w_ratio(x, y):
    """
    an attempt to weight (the name stands for 'Weighted Ratio') results from different
    algorithms to calculate the 'best' score.
    returns the weights ratio of type float
    """
    return fuzz.WRatio(x, y)


def fuzzy_p_ratio(x, y):
    """
    takes in the shortest string x or y and then matches it with all
    the sub-strings of length(min(x or y)).
    returns partial ratio of type float.
    """
    return fuzz.partial_ratio(x, y)

 
def fuzzy_token_sort_ratio(x, y):
    """
    this method attempts to account for similar strings that are out of order.
    returns the token sort ration of type float.
    """
    return fuzz.token_sort_ratio(x, y)


def get_fuzzy_match_score(str1 = None, str2 = None):
    """get fuzzy match score combining  w_ratio + p_ratio"""
    return fuzzy_w_ratio(str1, str2) + fuzzy_p_ratio(str1, str2)
