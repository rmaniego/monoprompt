"""
    (c) 2020 Rodney Maniego Jr.
    MonoPrompt
"""
import shutil


def decorator(string, chars=0):
    """
        Fills a single line of the console with a certain number of user-defined characters.
        ...
        Parameters
        ---
        string: string
            a string to repeat
        chars: integer
            if = 0, set length to max-width, else uses user-defined length
    """
    max = width()
    string = str(string)
    chars = get_int(chars, min=0, max=max)
    if chars <= 0: chars = max
    print(((string * (chars//len(string)))[:chars]), end="")

def message(string, chars=0, fill="", padding="", centered=False):
    """
        Prints a message to the console.
        ...
        Parameters
        ---
        string: string
            a string to print in the console
        chars: integer
            if = 0, set length to max-width, else uses user-defined length
        fill: string
            a sing character string filled on the trailing spaces of the line
        padding: string
            a string printed at the start and end of the message
        centered: boolean
            decides if string is aligned-left or centered on the console
    """
    max = width()
    string = str(string)
    padding = str(padding)
    chars = get_int(chars, min=0, max=max)
    if chars <= 0: chars = max
    if centered:
        chars = chars - (len(padding) * 2)
        string = string.center(chars)
    else:
        chars = chars - (len(padding) * 2) - len(string)
        spaces = " " * chars
        string = f"{string}{spaces}"
    if len(fill) >= 1:
        fill = str(fill)[0]
        string = string.replace("  ", f"{fill}{fill}").replace(f"{fill} ", f"{fill}{fill}")
    print(f"{padding}{string}{padding}", end="")

def catalog(items):
    """
        Creates an ordered list of all the items.
        ...
        Parameters
        ---
        items: list, tuple, iterable
            a list of items
    """
    size = len(str(len(items)))
    if type(items) in (list, tuple):
        for index, item in enumerate(items):
            numbering = index
            if size == 2:
                numbering = f"{index:0>2}"
            elif size == 3:
                numbering = f"{index:0>3}"
            elif size == 4:
                numbering = f"{index:0>4}"
            print(f" {numbering}: {item}")

def keys(items, extend=[]):
    """
        Generate a list of 1-based indices and extends an optional list of items
        ...
        Parameters
        ---
        items: list, tuple, iterable
            a list of items
        extend: list, tuple, iterable
            a list of items
    """
    indices = []
    for index in range(0, len(items)):
        indices.append(str(index))
    if type(extend) in (list, tuple):
        indices.extend(extend)
    return indices

def ask(label, chars=0, once=False):
    """
        Ask user for a string with an optional
        character count limit and optional loop
        for failing input.
        ...
        Parameters
        ---
        label: string
            a instruction for the user
        chars: integer
            max character count, removes extra characters from user input.
        once: boolean
            if set to True, allows empty input.
    """
    query = input(str(label))
    query = query.strip()
    if query == "" and not once:
        return ask(label)
    chars = get_int(chars, min=0)
    if chars > 0 and len(query) > chars:
        query = query[:chars]
    return query

def request(label, selection, blocklist=()):
    """
        Request an input from the user against an allowlist and/or a blocklist.
        Will continue to request user until an acceptable value is entered.
        ...
        Parameters
        ---
        label: string
            a instruction for the user
        selection: array, list, tuple, iterable
            a list to check whether user input is found within the list
        blocklist: array, list, tuple, iterable (optional)
            a list to check whether user input is not found within the list
    """
    selected = input(str(label))
    selected = selected.strip()
    if (selected in selection) and not (selected in blocklist):
        return selected
    return request(label, selection, blocklist)

# utils
def width():
    """ Gets the number of characters that fits a single line of the console window. """
    return shutil.get_terminal_size().columns

def get_int(string, min=0, max=99999):
    """
        Converts a string into an integer with an optional min and max range.
        ...
        Parameters
        ---
        string: string
            a numeric string
        min: integer
            a number less than or equal to the requested number
        max: array, list, tuple, iterable (optional)
            a number greater than or equal to the requested number
    """
    try:
        number = int(str(string))
        if int(min) <= number <= int(max):
            return number
        return min
    except:
        return min