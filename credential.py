class Credent:
    """
    Class that generates new instances of users
    """

    cred_list = []  #Empty user user_list



    def __init__(self, cred_app, cred_user, cred_pass):
        """
        __init__ method that helps us define properties for our objects.
        """

        self.cred_app = cred_app
        self.cred_user = cred_user
        self.cred_pass = cred_pass

    #end init
