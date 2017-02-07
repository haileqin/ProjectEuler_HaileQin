#!/usr/bin/python
# -*- coding: utf-8 -*-

LIMIT_VAL=1000

val=0

for x in xrange(0,1000):
	if x%3==0 or x%5 ==0:
		val=val+x


print val