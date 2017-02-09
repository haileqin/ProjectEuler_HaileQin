#!/usr/bin/python
# -*- coding: utf-8 -*-



def prime_judge(value):
    for y in xrange(2, value-1):
        if value%y==0:
            return 0
    
    return value
            

sum_prime=2

for y in xrange(3,200000):
    if y%10000==0:
        print y
    if prime_judge(y)!=0:
        sum_prime=sum_prime+y

print sum_prime


