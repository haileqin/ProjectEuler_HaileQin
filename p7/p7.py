#!/usr/bin/python
# -*- coding: utf-8 -*-



def prime_judge(value):
    for x in xrange(2, value-1):
    	if value%x==0:
    		return 0
    
    return value
            

index =1

for y in xrange(3,9999999999):
	if prime_judge(y)!=0:
		index=index+1
		print index, y
		if index==10001:
			break
