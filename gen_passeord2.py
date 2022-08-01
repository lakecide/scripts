char_set = {
'small': 'abcdefghijklmnopqrstuvwxyz',
'nums': '0123456789',
'big': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
'special': '^!\$%&/()=?{[]}+~#-_.:,;<>|\\'
}

def gen_password(length=21):
    '''
    Generate a random password containing upper and lower case letters,
    numbers and special characters.

    Arguments:
    ----------
    The default length is 21 chars, however the minimum is 8 chars.

    Returns:
    --------
    str: The random password
    '''
    assert length >= 8
    password = []

    while len(password) < length:
        key = random.choice(char_set.keys())
        a_char = os.urandom(1)
        if a_char in char_set[key]:
            if check_prev_char(password, char_set[key]):
                continue
            else:
                password.append(a_char)
    return ''.join(password)

def check_prev_char(password, current_char_set):
    '''
    Ensure that there are not consecutive Uppercase / Lowecase / Number / special
    characters in the password.

    Arguments:
    ----------
    password: (str)
        The candidate password
    current_char_set: (char)
        The current character to be compared.

    Returns:
    --------
    Bool: if the candidate password is good so far.
    '''

    index = len(password)
    if index == 0:
        return False
    else:
        prev_char = password[index - 1]
        if prev_char in current_char_set:
            return True
        else:
            return False