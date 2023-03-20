# library and file imports
from .azure_base import *


class azurestorageaccount(azureclass):
    
    # class constructor    
    def __init__(self, config):
        # get all configuration variables
        self.filename = None
        super().__init__(config)

    def set_filename(self, filename):
        """
        set text value an format as list
        """
        self.filename = filename