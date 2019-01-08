# Ivan Tinov, ID# 110255332, CSE 337 HW1_q5_p2
from hw1_q5_p1 import check_Final_User_Pass

while (True):
    try:
        username = input('Please enter a username: ')
        password = input('Please enter a password: ')
        if (check_Final_User_Pass(username, password)):
            break
    except (Exception, e):
        print('Error')
