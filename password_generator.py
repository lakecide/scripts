##Quick code to generate password randomly. this is still being developed

import string
import random
try:
        pass_len = int(input('Your password length preference? '))

        
        all_chars = string.ascii_letters + string.digits + string.punctuation
        password = ''
        for char in range(pass_len):
                rand_char = random.choice(all_chars)
                password += rand_char
        print('Password generated is: ', password)              
except ValueError:
        print("Invalid character entered, Try Again")
        
        

