#!/usr/bin/python
# -*- coding: utf-8 -*-

continuous_prime_number=2

prime_list=list()

def formula(n,a,b):
    return abs(n*n+a*n+b)

def prime_judge(val):
    for x in xrange(2,abs(val)):
        if abs(val)%x==0:
            return False
    return True

def prime_calculate(val):
    global prime_list
    for x in xrange(2,val):
        if val%x==0:
            return
    prime_list.append(val)
    prime_list.append(-1*val)

def traverse(a,b):
    global continuous_prime_number

    for n in xrange(0,1000000):
        if prime_judge(formula(n,a,b))==True:
            continue
        else:
            if n>continuous_prime_number:
                continuous_prime_number=n
                print "n=",n,"a=",a,"b=",b,"a*b=",a*b
            return


for x in xrange(3,10000):
    prime_calculate(x)


for b in prime_list:
    for a in xrange(-999,1000):
        traverse(a,b)




