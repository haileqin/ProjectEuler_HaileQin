#!/usr/bin/python
# -*- coding: utf-8 -*-

LIMITED_VAL=4000000
value=0


def Fibonacci_sum(val1, val2):
    global LIMITED_VAL
    global value
    val3=val1+val2

    if val3<=LIMITED_VAL:
        if val3%2==0:
            value=value+val3
        Fibonacci_sum(val2,val3)


value=2
Fibonacci_sum(1, 2)

print value
