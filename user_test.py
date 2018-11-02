import unittest     #import unittest module
from user import User   #import the user class


class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the user class behavioursself.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("nignanthomas","blablabla",) # create user object
    # end setUp


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"nignanthomas")
        self.assertEqual(self.new_user.password,"blablabla")

    # end test_init


    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new contact
        self.assertEqual(len(User.user_list),1)
    # end test_save_user


    







if __name__ == '__main__':
    unittest.main()
