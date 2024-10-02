# library and file imports
from .gcp_base import *


# big query (sub-class)
class bigquery(gcpclass):
    
    # class constructor    
    def __init__(self, config):
        # get all configuration variables
        super().__init__(config)