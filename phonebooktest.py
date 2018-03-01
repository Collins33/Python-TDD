import unittest

from phonebook import Contact

class TestPhonebook(unittest.TestCase):

    #test if it is an instance of phonebook object

    def setUp(self):
        #set up method runs before each test
        #it creates instance of Contact class
        self.new_contact=Contact("collins","njau","0702848032")


    def test_initialize_phonebook(self):
        
        self.assertEqual(self.new_contact.first_name, "collins")