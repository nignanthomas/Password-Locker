class User:
    """
    Class that generates new instances of users
    """

    user_list = []  #Empty user user_list



    def __init__(self, username, password):
        """
        __init__ method that helps us define properties for our objects.
        """

        self.username = username
        self.password = password
        
    #end init
