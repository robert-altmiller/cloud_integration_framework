# library and file imports


# gcp class (main-class)
class gcpclass:

    # class constructor    
    def __init__(self, config):
        # get all configuration variables
        self.config = config



# big query (sub-class)
class bigquery(gcpclass):
    
    # class constructor    
    def __init__(self, config):
        # get all configuration variables
        super().__init__(config)