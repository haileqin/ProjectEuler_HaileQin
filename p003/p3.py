#!/usr/bin/python
# -*- coding: utf-8 -*-


# value=600851475143

def function(val):
	for x in xrange(2,val):
		if val%x==0:
			print x, val/x
			function(val/x)
			break

function(600851475143)
