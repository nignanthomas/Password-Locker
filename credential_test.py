import unittest     #import unittest module
from credential import Credential   #import the user class


class TestCredential(unittest.TestCase):
    """
    Test class that defines test cases for the Credential class behavioursself.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_cred = Credential("nignanthomas","Facebook", "totofb", "totofbpassword") # create user object
    # end setUp


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_cred.username,"nignanthomas")
        self.assertEqual(self.new_cred.cred_app,"Facebook")
        self.assertEqual(self.new_cred.cred_user,"totofb")
        self.assertEqual(self.new_cred.cred_pass,"totofbpassword")

    # end test_init


    def test_save_cred(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_cred.save_cred() # saving the new contact
        self.assertEqual(len(Credential.cred_list),1)

    # end test_save_cred






if __name__ == '__main__':
    unittest.main()
