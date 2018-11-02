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


    def save_user(self):
        '''
        save_user method saves contact objects into user_list
        '''

        User.user_list.append(self)
    #end save_contact








#############################
