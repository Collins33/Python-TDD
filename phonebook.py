class Contact:
    contact_list=[]#empty contact list to contain saved contacts

    def __init__(self,first_name,last_name,number):
        self.first_name=first_name
        self.last_name=last_name
        self.number=number
    


    def save_contact(self):
        #saves the contact into the contact list
        Contact.contact_list.append(self)
