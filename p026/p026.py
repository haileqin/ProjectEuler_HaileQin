#!/usr/bin/python
# -*- coding: utf-8 -*-

digit_list=list()
remainder_list=list()

max_cycle_len=0

def calculate(value):
    global max_cycle_len

    base_num=1

    del digit_list[0:]
    del remainder_list[0:]

    index=0

    # print ""

    for x in xrange(1,1000):

    	

    	if base_num%value==0:
    		digit_list.append(base_num/value)
    		break

    	if base_num<value:
    		base_num=10*base_num
    		if base_num<value:
    			while base_num>value :
    				base_num=10*base_num
		    		digit_list.append(0)
		    		index=index+1
        
        if base_num in remainder_list:
        	index=remainder_list.index(base_num)
        	print index
    		break
        remainder_list.append(base_num)
        # print base_num,
        digit_list.append(base_num/value)
    	base_num=base_num%value

    	# if x>4:
    	# 	remainder_list.append(base_num)
    # print ""
    if len(digit_list)-index>max_cycle_len:
    	max_cycle_len=len(digit_list)-index

    print value, " [", len(digit_list)-index, "]: ",
    for x in xrange(0,len(digit_list)):
    	if x==index:
    		print "(",
    	print digit_list[x],

    print ")"



for x in xrange(2,1000):
	calculate(x)

print "max_cycle_len=",max_cycle_len	


