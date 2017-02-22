#!/usr/bin/python
# -*- coding: utf-8 -*-

max_collatz_value=0
max_index_value=0

def calculate(number, index):
    # print number, index

    if number==1:
        return index

    if number%2==0:
        index=calculate(number/2, index+1)
    else:
        index=calculate(number*3+1, index+1)

    return index


for x in xrange(2,1000000):
    collatz_index=calculate(x, 0)
    # print x, collatz_value
    if max_index_value<collatz_index:
        max_index_value=collatz_index
        max_collatz_value=x

print max_collatz_value, max_index_value







    