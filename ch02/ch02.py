# sequence
*a, b = range(10)

print(a)
print(b)


# namedtuple
from collections import namedtuple

City = namedtuple('City', ['name', 'state'])

fortaleza = City('Fortaleza', 'CE')

print(fortaleza)

print(City._fields)

# returns an collections.OrderedDict
print(fortaleza._asdict())

# slicing

MY_SLICE = slice(0, 10)

my_name = "Abelardo Vieira Mota"

print(my_name[MY_SLICE])