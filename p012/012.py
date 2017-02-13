#!/usr/bin/python
# -*- coding: utf-8 -*-

number_sum=0

def divisor_cal(value):
	index=0
	for x in xrange(2,value+1):
		if value%x==0:
			index=index+1

	return index


for x in xrange(100,500000):
	number_sum=0

	for y in xrange(1,x):
		number_sum=number_sum+y

	divisor_cal_num=divisor_cal(number_sum)
	print x, number_sum, divisor_cal_num
	if divisor_cal_num>500:
		print x, number_sum, divisor_cal_num
		break


# 12376 76576500 575