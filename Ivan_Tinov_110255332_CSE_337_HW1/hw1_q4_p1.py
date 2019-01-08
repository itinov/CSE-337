# Ivan Tinov, ID# 110255332, CSE 337 HW1_q4_p1

file = open("100-0.txt", "r", encoding="utf8")
lines = file.read()


def n_grams(lines, n):
    lines = lines.split(' ')
    outStr = {}
    if(n <= 10): 
        for i in range(len(lines) - (n + 1)):
            s = ' '.join(lines[i : i + n])
            outStr.setdefault(s, 0)
            outStr[s] += 1
    else:
        print('Value of n-grams must be 10 or less!')
    print(outStr)


n_grams(lines, 2) # test output here


