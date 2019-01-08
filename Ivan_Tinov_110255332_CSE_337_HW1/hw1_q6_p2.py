# Ivan Tinov, ID# 110255332, CSE 337 HW1_q6_p2

lst = [1, 4, 20] # test values here
lst2 = list(map(lambda x: 2**x, lst))
lst3 = list(filter(lambda x: x <= 1000, lst2))
print(lst3)


