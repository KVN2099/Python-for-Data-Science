#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = [ 1, 2, 3, 4, 5 ]
for i in x:
    print('i is {}'.format(i))
# Tuples are not mutable
# x = (1, 2, 3, 4, 5)
# x[2] = 34 throws an error

y = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5 }
for k, v in y.items(): # k is key, v is value, any element can be any type
    print('i is {} {}'.format(k, v))
# Dictionaries are mutable