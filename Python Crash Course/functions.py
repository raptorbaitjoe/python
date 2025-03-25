def display_message():
    """Explain what you're learning this chapter"""
    print("Functions")

display_message()

def favourite_book(bewk):
    """Tell the your favourite book"""
    print(f"One of my favourite books is {bewk.title()}")

favourite_book('1984')

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

character = get_formatted_name('maka', 'albarn')

print(character)


def get_formatted_long_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

characterone = get_formatted_long_name('death', 'kid', 'the')

charactertwo = get_formatted_long_name('black', 'star')

print(characterone)
print(charactertwo)
