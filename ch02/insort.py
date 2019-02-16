import bisect 
import random 

SIZE = 7

random.seed(1729)

my_list = []

for i in range(SIZE):

    new_item = random.randrange(SIZE * 2)
    # ? what's the implications of insort with hi/lo not default?
    bisect.insort(my_list, new_item, lo=0, hi=min(2, len(my_list)))

    print('%2d ->' % new_item, my_list)