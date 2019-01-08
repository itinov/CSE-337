# Ivan Tinov, ID# 110255332, CSE 337 HW1_q6_p1

print('Printing N-Narcissistic Numbers between 100 and 999: ')
n_num = [i for i in range(1000) if sum(list(map(lambda y: y ** len(str(i)), list(map(int, str(i)))))) == i]
print(n_num)
