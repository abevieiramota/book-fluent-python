import bisect
import sys 

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

def demo(bisect_fn):

    for needle in reversed(NEEDLES):

        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))


print('bisect')
print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
demo(bisect.bisect)
print('\nbisect_left')
print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
demo(bisect.bisect_left)



# looks like pandas.cut
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):

    # if score = some breakpoint -> assign previous grade
    # i = bisect.bisect_left(breakpoints, score)
    # if score = some breakpoint -> assign next grade
    i = bisect.bisect(breakpoints, score)

    return grades[i]
