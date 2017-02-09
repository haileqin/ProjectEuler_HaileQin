#!/usr/bin/python
# -*- coding: utf-8 -*-

sum_prime=2

def prime_judge(index, max_index,value):
    global sum_prime

    if index>=max_index:

        sum_prime=sum_prime+value
        return
    
    if value%index!=0:
        prime_judge(index+1, int(value/index), value)
    else:
        return

            



for y in xrange(3,2000000):
    if y%10000==0:
        print y, sum_prime
    prime_judge(2, y, y)


print sum_prime


