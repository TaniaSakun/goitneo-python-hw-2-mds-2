from typing import Optional
from application.bot.service import (add_contact, change_contact, get_contact, get_all_contacts, delete_contact, parse_input, remove_phone)
from application.utilities.objects import AddressBook
from application.utilities.constants import Constants
from application.utilities.validations import input_error


OPERATIONS = {
    "add": add_contact,
    "all": get_all_contacts,
    "change": change_contact,
    "close": lambda *_: None,
    "delete": delete_contact,
    "exit" : lambda *_: None,
    "find": get_contact,
    "hello": lambda *_: Constants.help_question,
    "help": lambda *_: Constants.help_text,
    "remove": remove_phone
    
}

@input_error
def get_handler(user_input: str, contacts: AddressBook) -> Optional[str]:
    cmd, *args = parse_input(user_input)
    return OPERATIONS.get(cmd, lambda *_: Constants.invalid_command)(contacts, args)
