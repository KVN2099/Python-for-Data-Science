#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

from decimal import *

# no difference between ' ' and " "
x = '''seven
this is a multiline string with triple quotes
'''.upper() # Everything is an object in Python, including literal strings

y = 'seven "{1:<09}" "{0:>09}"'.format(8, 9) # 9 spaces to the right and 9 to the left
print(f'x is {x}')
print(type(x))
print(y)

print(.1 + .1 + .1 - .3) # Not exact

a = Decimal('.10') # Class decimal.Decimal
b = Decimal('.30') # Class decimal.Decimal
z = a + a + a - b
print(z) # 0.00
# When dealing with money, use a decimal library to improve accuracy

print(type(None)) # Class NoneType
if None:
    print(True)
else:
    print(False)
# Prints False

x = (1, 'two', 3.0, [4, 'four'], 5)
y = (1, 'two', 3.0, [4, 'four'], 5)

if x == y: # same values
    print('yep')
else:
    print('nope')

if x is y: # same space in memory
    print('yep')
else:
    print('nope')

if isinstance(x, tuple):
    print('x is a tuple')
elif isinstance(x, list):
    print('x is a list')