import unittest

from phonebook import Contact

class TestPhonebook(unittest.TestCase):

    #test if it is an instance of phonebook object

    def setUp(self):
        #set up method runs before each test
        #it creates instance of Contact class
        self.new_contact=Contact("collins","njau","0702848032")

    def tearDown(self):
        #this test runs after every test
        #it clears the contact_list
        Contact.contact_list=[]    


    def test_initialize_phonebook(self):
        #tests if object initializes well       
        self.assertEqual(self.new_contact.first_name, "collins")

    def test_save_adds_to_list(self):
        self.new_contact.save_contact()
        self.assertEqual(len(Contact.contact_list),1)

    def test_save_multiple_contacts(self):
        self.new_contact.save_contact()
        test_contact=Contact("olivia","neema","0712002200")
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list),2)


    def test_delete_removes_contact(self):
        self.new_contact.save_contact()
        test_contact=Contact("olivia","neema","0712002200")
        test_contact.save_contact()

        self.new_contact.delete_contact()
        self.assertEqual(len(Contact.contact_list),1)
