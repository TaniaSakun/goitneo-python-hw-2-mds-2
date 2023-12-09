from application.utilities.objects import AddressBook, Record
from application.utilities.constants import Constants
from typing import List

def parse_input(user_input: str) -> List[str]:
    cmd, *args = user_input.split()
    return [cmd.strip().lower(), *args]

def add_contact(contacts: AddressBook, args: list[str]) -> str:
    name, phone = args
    record = Record(name)
    record.add_phone(phone)
    contacts.add_contact(record)
        
    return Constants.contact_added.replace("{1}", name)

def change_contact(contacts: AddressBook, args: list[str]) -> str:
    name, old_phone, new_phone = args
    record = contacts.find_record(name)
    
    if(record):
        record.edit_phone(old_phone, new_phone)
        return Constants.contact_changed.replace("{1}", name)
    else:
        raise KeyError
    
def remove_phone(contacts: AddressBook, args: list[str]) -> str:
    name, phone = args
    record = contacts.find_record(name)
    
    if not record:
        raise KeyError
    if record.remove_phone(phone):
        return Constants.phone_number_removed.replace("{1}", phone).replace("{2}", name)  
    else:
        return Constants.phone_number_not_exist.replace("{1}", phone).replace("{2}", name)  
    
def get_contact(contacts: AddressBook, args: list[str]) -> str:
    return contacts.find_record(args[0])

def get_all_contacts(contacts: AddressBook, *args: list[str]) -> str:
    if not contacts:
        return Constants.no_contacts_text
    return str(contacts)
    
def delete_contact(contacts: AddressBook, args: list[str]) -> str:
    contacts.delete_record(args[0])  
    return Constants.contact_deleted.replace("{1}", args[0])