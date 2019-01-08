# Ivan Tinov, ID# 110255332, CSE 337 HW1_q5_p1
import re
from itertools import groupby


def check_length(password):
    if (len(password) >= 6 and len(password) <= 20):
        return (True)
    else:
        return (False)

def check_Digit_and_Upper(password):
    if (any(char.isdigit() for char in password) and any(char.isupper() for char in password)):
        return (True)
    else:
        return (False)

def check_Special(password):
    if (re.match(r'[A-Za-z0-9@#$%^&+=]', password)):
        return (True)
    else:
        return (False)

def check_user_and_pass(username, password):
    if ((username not in password) and username[::-1] not in password):
        return (True)
    else:
        return (False)

def check_palindrome(password):
    if (password != password[::-1]):
        return (True)
    else:
        return (False)

def check_unique(password):
    uniqueChars = set()
    for i in password:
        if (i in uniqueChars):
            continue
        else:
            uniqueChars.add(i)
    if (len(uniqueChars) > 0.5 * len(password)):
        return (True)
    else:
        return (False)

def check_subsequence(password):
    if re.findall(r'((\w)\2+)', password):
        return (True)
    else:
        return (False) 
            
def check_Final_User_Pass(username, password):
    if(check_length(password)):
        if(check_Digit_and_Upper(password) and check_Special(password) and check_user_and_pass(username, password)):
            if(check_palindrome(password) and check_unique(password) and check_subsequence(password)):
               print(True)
            else:
               print(False)
        else:
           print(False)
    else:
        print(False)


#check_Final_User_Pass('Ivan','iamsoCOOL@24')
        


    
