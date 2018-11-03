#from user import User


class Credential:
    """
    Class that generates new instances of users
    """

    cred_list = []  #Empty user user_list



    def __init__(self, username, cred_app, cred_user, cred_pass):
        """
        __init__ method that helps us define properties for our objects.
        """
        self.username = username
        self.cred_app = cred_app
        self.cred_user = cred_user
        self.cred_pass = cred_pass
    #end init cred



    def save_cred(self):
        '''
        save_cred method saves credential objects into cred_list
        '''

        Credential.cred_list.append(self)
    # end save_cred


    def delete_cred(self):
        '''
        delete_cred method deletes a saved credential from the cred_list
        '''

        Credential.cred_list.remove(self)
    # end delete_cred


    @classmethod
    def search_cred(cls, user_search, app_search,):
        '''
        Method that takes in an Appname and username and returns a credential that matches.

        Args:
            username: Username to search for
            cred_app: Appname to search
        Returns :
            Credential that matches Username and Appname.
        '''

        for credential in cls.cred_list:
            if credential.username == user_search and credential.cred_app == app_search:
                return credential
            # else:
            #     return " :( Credential Not Found"
    #end search_cred


    @classmethod
    def display_creds(cls, user_search):
        '''
        method that returns the credentials list
        '''
        all_user_creds =[]
        for credential in cls.cred_list:
            if credential.username == user_search:
                all_user_creds.append(credential)
        return all_user_creds
    #end display_creds







#############
