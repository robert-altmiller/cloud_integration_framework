# library and file imports
from helpers.helpers import *


# class_obj class is in --> azure_helpers.py
def azure_text_analytics_unit_test(config = None, textanalytics_obj = None):
    # unit test for azure congitive services text analytics sub class
    
    text_list = \
    [
        "I want to order a small pizza",
        "I want to buy a book.",
        "I love you, and you are an asbolute amazing person",
        "you are terrible and such a bad person bad bad",
        "Dr. Smith has a very modern medical office, and she has great staff.",
        "what are you working on at the moment because I really could use your help",
        "I am really glad you are here",
        "there is person named bill in bakersfield, california"
    ]

    all_results_list = []
    for text in text_list:
        textanalytics_obj.set_text(text)
        keyphrases = get_json_loads(textanalytics_obj.get_text_analytics("keyphrases"))
        sentiment_score = get_json_loads(textanalytics_obj.get_text_analytics("sentiment_score"))
        sentiment_confidence = get_json_loads(textanalytics_obj.get_text_analytics("sentiment_confidence"))
        named_entities = get_json_loads(textanalytics_obj.get_text_analytics("named_entities"))

        json_structure = {
            "input_text": keyphrases[0]["input_text"],
            "keyphrases": keyphrases[0]["keyphrases"],
            "sentiment_score": sentiment_score[0]["sentiment_score"],
            "sentiment_confidence": sentiment_confidence[0]["sentiment_confidence"],
            "entities": named_entities[0]["entities"]
        }
        all_results_list.append(json_structure)
    
    return get_json_dumps(all_results_list)