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
