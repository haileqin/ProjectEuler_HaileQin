#!/usr/bin/python
# -*- coding: utf-8 -*-

result=0

for x in xrange(500,999):
	for y in xrange(500,999):
		value=x*y
		if int(value/100000)==value%10 and int(value/10000)%10==(value/10)%10 and int(value/1000)%10==(value/100)%10:
			if value>result:
				result=value


print result