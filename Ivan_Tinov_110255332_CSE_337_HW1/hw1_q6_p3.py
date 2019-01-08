# Ivan Tinov, ID# 110255332, CSE 337 HW1_q6_p3
import itertools
import functools

lst = ["hi hi hi what is up?"]
words = (list(itertools.chain.from_iterable(x.split() for x in lst)))
count = {k:len(list(v)) for k,v in itertools.groupby(words)}
print(count)






