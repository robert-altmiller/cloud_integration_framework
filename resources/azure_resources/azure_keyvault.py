# azure keyvault class functions
class azurekeyvault(azureclass):

    # class constructor    
    def __init__(self, config):
        # get all configuration variables
        self.text = None
        super().__init__(config)