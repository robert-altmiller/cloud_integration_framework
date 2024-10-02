# library and file imports
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
from .azure_base import *


# azure text analytics class functions (e.g. cognitive services)
class azuretextanalytics(azureclass):

    # class constructor    
    def __init__(self, config):
        # get all configuration variables
        self.text = None
        super().__init__(config)


    def set_text(self, text):
        """
        set text value an format as list
        """
        self.text = check_text_as_list(text)


    def get_text_analytics_config(self):
        """
        get azure cognitive services connection information and api keys
        fqdn = fully qualified domain name
        """
        textconfig = {
            "resource_name": self.config["AZURE_COG_SERVICES_RESOURCE_NAME"],
            "api_key": self.config["AZURE_COG_SERVICES_API_KEY"],
            "base_url": self.config["AZURE_COG_SERVICES_BASE_URL"]
        }
        textconfig["fqdn"] = "https://" + textconfig["resource_name"] + "." + textconfig["base_url"]
        return textconfig


    def get_text_analytics_client(self):
        """
        get azure cognitive services text analytics client
        """
        config = self.get_text_analytics_config()       
        creds = AzureKeyCredential(config["api_key"])
        text_analytics_client = TextAnalyticsClient(endpoint = config["fqdn"], credential = creds)
        return text_analytics_client


    def get_text_analytics_keyphrases(self):
        """
        get text analytics keyphrases for a string in a python list
        """
        keyphrase_response = self.get_text_analytics_client().extract_key_phrases(self.text, language = "en")
        return keyphrase_response


    def get_text_analytics_sentiment(self):
        """
        get text analytics sentiment for a string in a python list
        """
        sentiment_response = self.get_text_analytics_client().analyze_sentiment(self.text)
        return sentiment_response


    def get_text_analytics_entities(self):
        """
        get text analytics named entities for a string in a python list
        """
        entities_response = self.get_text_analytics_client().recognize_entities(documents = self.text)
        return entities_response


    def get_text_analytics(self, return_type = None):
        """
        return_types: "sentiment_score, sentiment_confidence, keyphrases, or entities"
        """
        entity_list = []
        entity_dict = {}
        
        # keyphrases
        if return_type == "keyphrases":
            response = get_json_loads(get_json_dumps(self.get_text_analytics_keyphrases()[0].key_phrases))
            return get_json_dumps([{"input_text": self.text, "keyphrases": response}])
        
        # sentiment score
        if return_type == "sentiment_score":
            response = get_json_loads(get_json_dumps(self.get_text_analytics_sentiment()[0].sentiment))
            return get_json_dumps([{"input_text": self.text, "sentiment_score": response}])
        
        # sentiment confidence
        if return_type == "sentiment_confidence":
            conf = self.get_text_analytics_sentiment()[0].confidence_scores
            entity_dict["positive"] = conf.positive
            entity_dict["neutral"] = conf.neutral
            entity_dict["negative"] = conf.negative
            return get_json_dumps([{"input_text": self.text, "sentiment_confidence": entity_dict}])
        
        # named entities
        if return_type == "named_entities":
            entities = self.get_text_analytics_entities()[0].entities
            for entity in entities:
                entity_dict["entity_text"] = entity.text
                entity_dict["entity_category"] = entity.category
                entity_dict["entity_subcategory"] = entity.subcategory
                entity_dict["entity_length"] = entity.length
                entity_dict["entity_offset"] = entity.offset
                entity_list.append(entity_dict)
            return get_json_dumps([{"input_text": self.text, "entities": entity_dict}])