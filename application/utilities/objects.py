import re
from collections import UserDict
from application.utilities.constants import Constants, InvalidNameError, InvalidPhoneError, InvalidPhoneLengthError

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def __eq__(self, other):
        return hasattr(other, "value") and self.value == other.value
    
    def __hash__(self):
        return hash(self.value)
    
    def __ne__(self, other):
        return not hasattr(other, "value") or self.value != other.value

class Name(Field):
    def __init__(self, value):
        if not value:
            raise InvalidNameError()
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        pattern = re.compile(r'^[0-9+-]+$')
        
        if len(value) != 10:
            raise InvalidPhoneLengthError()   
        elif not pattern.match(value):
            raise InvalidPhoneError()
        
        super().__init__(value)
    

class Record:
    def __init__(self, name):
        self.name : Name = Name(name)
        self.phones : set[Phone] = set()

    def add_phone(self, phone):
        self.phones.add(Phone(phone))
    
    def remove_phone(self, phone):
        return bool(self.phones.discard(Phone(phone)))

    def edit_phone(self, old_phone, new_phone):
        self.phones.discard(Phone(old_phone))
        self.phones.add(Phone(new_phone))
    
    def find_phone(self, name):
        return [phone for phone in self.phones if name in phone.value]
    
    def __str__(self):
        return Constants.contact_info.replace("{1}", self.name.value).replace('{2}', '; '.join(p.value for p in self.phones))


class AddressBook(UserDict[Name, Record]):
    from collections import UserDict

    def __str__(self):
        return "\n".join(str(contact) for contact in self.data.values())

    def add_contact(self, contact):
        name = contact.name
        phones = contact.phones

        contact = self.data.setdefault(name, contact)
        for phone in phones:
            contact.add_phone(phone.value)
    
    def find_record(self, name):
        contact = self.data.get(Name(name), None)
        if contact:
            return contact
        else: 
            raise KeyError
    
    def delete_record(self, name):
        del self.data[Name(name)]