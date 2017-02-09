#!/usr/bin/python
# -*- coding: utf-8 -*-


# a+b+c=1000
# a*a+b*b=c*c
# a*a+b*b=(1000-a-b)*(1000-a-b)

for a in xrange(1,999):
	for b in xrange(1,999):
		if a*a+b*b==(1000-a-b)*(1000-a-b):
			print a, b, 1000-a-b, a*b*(1000-a-b)
			break

