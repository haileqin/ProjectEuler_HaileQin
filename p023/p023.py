#!/usr/bin/python
# -*- coding: utf-8 -*-

num_sumdivisor={}
list_abundant_num_sum=[]
sum_of_all=0

def sum_of_divisor(number):
	sum_divisor=0

	for x in xrange(1,number):
		if number%x==0:
			sum_divisor=sum_divisor+x

	return sum_divisor


for x in xrange(12,28123+1):
	sum_divisor=sum_of_divisor(x)
	if x<sum_divisor:
		num_sumdivisor[x]=sum_divisor
		# print x, sum_divisor

    
for i in num_sumdivisor:
	for j in num_sumdivisor:
		list_abundant_num_sum.append(i+j)

list_abundant_num_sum=list(set(list_abundant_num_sum))

print "num of abundant sum: ",len(list_abundant_num_sum)

for k in xrange(1,28123+1):
	if k in list_abundant_num_sum:
		continue

	sum_of_all=sum_of_all+k

print sum_of_all
