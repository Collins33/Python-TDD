class Contact:
    contact_list=[]#empty contact list to contain saved contacts

    def __init__(self,first_name,last_name,number):
        self.first_name=first_name
        self.last_name=last_name
        self.number=number
    


    def save_contact(self):
        #saves the contact into the contact list
        Contact.contact_list.append(self)

    def delete_contact(self):
        #removes the contact from the contact list
        Contact.contact_list.remove(self)

    @classmethod
    def find_contact(cls,number):
        for contact in cls.contact_list:
            if contact.number==number:
                return contact

    @classmethod
    def contact_exists(cls,number):
        for contact in cls.contact_list:
            if contact.number == number:
                return True
        return False

    @classmethod
    def display_contacts(cls):
        return cls.contact_list                    
    
    @classmethod
    def update_name(cls,oldname,newName):
        for contact in cls.contact_list:
            if contact.first_name == oldname:
                contact.first_name.replace(contact.first_name,newName)
                return contact
