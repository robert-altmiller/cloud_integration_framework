# library and file imports
import msal
from .azure_base import *


# azure authentication class functions
class azureauth(azureclass):

    # class constructor    
    def __init__(self, config):
        # get all configuration variables
        self.filename = None
        super().__init__(config)


    def set_auth_grant_scope_override(self, auth_grant_scope = None):
        """
        set new authentication grant scope
        return type must be a list
        """
        self.config["AZURE_AUTHENTICATION_GRANT_SCOPE"] = [auth_grant_scope]


    def set_auth_authority_override(self, auth_authority = None):
        """set new authentication authority"""        
        self.config["AZURE_AUTHENTICATION_AUTHORITY"] = auth_authority


    def get_oauth2_app(self):
        """get oauth2 app using MSAL"""
        app = msal.ConfidentialClientApplication(
            self.config["AZURE_CLIENT_ID"],
            authority = self.config["AZURE_AUTHENTICATION_AUTHORITY"],
            client_credential = self.config["AZURE_CLIENT_SECRET"] 
        )
        return app
    

    def get_oauth2_token(self):
        """get oauth2 token using MSAL"""
        return self.get_oauth2_app().acquire_token_for_client(
            scopes = self.config["AZURE_AUTHENTICATION_GRANT_SCOPE"]
        )


    def print_oauth2_token(self):
        """print oauth2 token"""
        print(self.get_oauth2_token())