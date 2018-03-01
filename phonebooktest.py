import unittest

from phonebook import Contact

class TestPhonebook(unittest.TestCase):

    #test if it is an instance of phonebook object

    def test_initialize_phonebook(self):
        self.new_contact=Contact("collins","njau","0702848032")

        self.assertEqual(self.new_contact.first_name, "collins")