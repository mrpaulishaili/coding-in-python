"""
    ---   META-DATA   ---
    Phonebook Program
    Written in Python
    Developed by: Paul Ishaili C.
"""
import time

contact = {}

contact_file = 'a://phonebook.txt'


def contacts_file_content():
    file_contents = open(contact_file, "r+").read()
    return file_contents


phonebook_options = {
    1: "Display",
    2: "Create",
    3: "Search",
    4: "Delete",
    5: "Close"
}


# Define function to welcome user and provide options on how the phonebook works
def welcome():
    time.sleep(3)
    #  Create an entry variable using the input function and multiple line strings format
    entry = int(input("""
                >>> 🤗 What would you like to do? <<<
                
                    1. Display      2. Create
                    3. Search       4. Delete 
                             5. Close
                             
                Enter your entry here (1,2,3, or 4): """))
    #  Close function
    return entry


# Define display_contact function
def display_contact():
    #  If contact is not empty, print contacts

    file_contents = contacts_file_content()
    print(file_contents)
    if bool(contact):
        for name, number in contact.items():
            print(name, '-->', number)
    #  else inform that contact book is empty
    else:
        print('Phonebook is currently empty! Add a new contact to create one.')
    return


#  Define create_contact function
def create_contact():
    phone_number = input('Enter phone number: ')
    contact_name = input('What would you want to save this contact as? "Firstname Lastname": ')

    def save_contact():
        contact.update({contact_name: phone_number})
        file1 = open(contact_file, "a")
        file1.write("{" + contact_name + ": " + phone_number + "}\n")
        file1.close()
        return

    def validate_input():
        # Check if contact doesn't exist, then add new contact to contacts
        if contact_name not in contact:
            save_contact()
            display_contact()

        # else inform that the contact already exists
        else:
            print('This contact already exists in phonebook.')
            return

    validate_input()


#  Define search_contact function
def search_contact():
    contact_name = input('Enter contact name you wish to view')

    if contact_name in contact:
        print('The contact result:', contact_name, '-->', contact[contact_name])

    else:
        print('Not found!')


#  Define delete_contact function
def delete_contact():
    ...


# Define a function phonebook
def phonebook():

    # Initiate a while loop to continuously run the phonebook program
    while True:
        try:
            #  Set entry variable to welcome function
            entry = welcome()

            #  Create conditions for decision-making, for any option entered by the user.
            if entry == 1:
                display_contact()
            elif entry == 2:
                create_contact()
            elif entry == 3:
                search_contact()
            elif entry == 4:
                delete_contact()
            else:
                print('Select a valid option')
        except ValueError:
            print('Select a valid option')


phonebook()
