from functools import wraps


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            if func.__name__ == "change_contact":
                return "Enter user name and new phone for updating."
            return "Give me name and phone please."
        except KeyError:
            return 'Such name does not exists in the contacts.'
        except IndexError:
            return 'Enter the argument (user name).'

    return inner


@input_error
def add_contact(args, contacts):
    """
    The function add a user name and phone numer as kay-value to the dict

    Parameters:
        args: list that contains entered and parsed as username and phone
        contacts: dict of contacts
    Returns:
        str: a string containing an explanation of the result
    Raises:
        ValueError: if data entered incorrectly
    """
 
    name, phone = args
    name = name.strip().lower()
    if contacts.get(name) is None: 
        contacts[name] = phone
        return "Contact added."
    else:
        return "Such a name already exists. If you want update it, input command 'change [name] [phone number]'."
   
    
@input_error
def change_contact(args, contacts):
    """
    The function change a user's phone numer

    Parameters:
        args: list that contains entered and parsed as username and phone
        contacts: dict of contacts
    Returns:
        str: a string containing an explanation of the result
    Raises:
        ValueError: if data entered incorrectly
    """
    
    name, phone = args
    name = name.strip().lower()
    if contacts.get(name) is not None:
        contacts[name] = phone
        return f"Contact {name} updated to {contacts[name]}"
    else:
        return "Such a name does not exists in the contacts. If you want to add it, input command 'add [name] [phone number]'."
    

@input_error
def show_phone(args, contacts):
    """
    The function show a user's phone numer by name

    Parameters:
        args: list that contains entered and parsed a username and phone
        contacts: dict of contacts
    Returns:
        str: a phone number of the user or  string containing an explanation of the result
    Raises:
        ValueError: if data entered incorrectly
    """
    
    name = args[0].strip().lower()
    return f'{name}: {contacts[name]}'


@input_error
def show_all(contacts):
    """
    The function show all added contacts

    Parameters:
        contacts: dict of contacts
    Returns:
        dict: dict of contacts
        or str:  string containing an explanation of the result
    """

    if len(contacts) != 0:
        return f'All contacts: {contacts}'
    else:
        return 'There is no saved contacts.'
    
