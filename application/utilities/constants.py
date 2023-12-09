class Constants:
   #Command messages
   
    contact_added = "Contact {1} added."
    contact_changed = "Contact {1} changed."
    contact_deleted = "Contact {1} deleted."
    contact_info = "Contact name: {1}, phones: {2}"
    contact_not_found = "Contact not found."
    enter_command = "Enter a command: "
    help_question = "How can I help you?"
    help_text = """
    These are common commands used in various situations:
    start commands
        hello       Starting command
    set commands 
        add         Adds a new contact with a phone number. Note: takes name and phone number as parameters
        change      Changes phone number for the concrete contact. Note: takes name and phone number as parameters
        delete      Deletes phone number for the concrete contact. Note: takes name as parameter
        remove      Removes the phone number from the concrete contact. Note: takes name and phone number as parameters
               
    get commands
        all         Gets list of all created contacts with phone numbers
        find        Gets phone number of the concrete contact. Note: takes a name as a parameter
        help        In case you need help with detailed commands names and descriptions
    
    end commands
        close       Ends the interaction
        exit        Ends the interaction
    """
    good_bye_message = "Good bye!"
    phone_number_removed = "Phone number {1} removed from the contact {2}"
    task_bot = "Bot task"
    
    #Error messages

    invalid_command = "Invalid command."
    invalid_input = "Invalid command. Try again."
    invalid_name = "Invalid name for the Contact"
    invalid_parameters = "Give me name and phone please."
    phone_number_length = "Phone number must be 10 digits long."
    phone_number_not_exist = "There is no phone number {1} for the contact {2} in the AddressBook."
    phone_number_value = "Phone number must have only digits and '+' or '-' symbols."
    no_contacts_text = """Contacts have not been added yet. To add a contact, please enter the following command: 
    'add contactName phone', where contactName is the name of contact, and phone is a contact phone number."""
    contact_not_exist = "Contact do not exist."
    
#Custom exceptions  
  
class InvalidNameError(Exception): 
    ...
class InvalidPhoneError(Exception):
    ...
class InvalidPhoneLengthError(Exception):
    ...