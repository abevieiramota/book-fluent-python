a = dict(one=1, two=2)
b = {'one': 1, 'two': 2}
c = dict(zip(['one', 'two'], [1, 2]))
d = dict([('one', 1), ('two', 2)])
e = dict({'one': 1, 'two': 2})



x = {'a': 1}

# returns the value associated to b, and if it doesn't exist, set it to the default value passed and return it
x.setdefault('b', []).append('c')

print(x)


class WeirdDict(dict):

    def __missing__(self, k):

        print(f'{k} is missing')

        return None

w = WeirdDict()
w['b']

