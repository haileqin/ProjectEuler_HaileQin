#!/usr/bin/python
# -*- coding: utf-8 -*-

sum_of_all_names=0
list_names=list()
character={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

def read_file():
	global list_names

	fp=open('p022_names2.txt')

	for line in fp:
	    # print line.replace("\r\n", "")

	    list_names.append(line.replace("\r\n", ""))

	fp.close()

def name_calcute(name_str):
	sum_of_name=0
	for x in xrange(len(name_str)):
		sum_of_name=sum_of_name+character.get(name_str[x])
	return sum_of_name


read_file()

list_names_sorted=sorted(list_names)
# print list_names_sorted


index=0

for name in list_names_sorted:
    index=index+1
    sum_of_name=name_calcute(name)
    # print index, name, sum_of_name

    sum_of_all_names=sum_of_all_names+index*sum_of_name

print sum_of_all_names
