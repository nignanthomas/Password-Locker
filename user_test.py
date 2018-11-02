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

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []
    # end tearDown


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
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)
    # end test_save_user


    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("nignanthomas", "blablabla") # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)







if __name__ == '__main__':
    unittest.main()
