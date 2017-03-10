#!/usr/bin/python
# -*- coding: utf-8 -*-


amicable_numbers=[]
sum_of_divisors=0


def sum_of_divisor(number):
	sum_divisor=0

	for x in xrange(1,number):
		if number%x==0:
			sum_divisor=sum_divisor+x

	return sum_divisor


for x in xrange(2,10000):
	if x in amicable_numbers:
		continue

	num1=sum_of_divisor(x)
	num2=sum_of_divisor(num1)

	

	if x==num2 and x!=num1:
		print x, num1
		amicable_numbers.append(x)
		amicable_numbers.append(num1)

		sum_of_divisors=sum_of_divisors+x+num1


print sum_of_divisors