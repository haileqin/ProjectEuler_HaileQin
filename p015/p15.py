#!/usr/bin/python
# -*- coding: utf-8 -*-

list_arrays=[]
index=0

def print_array(i, j):
    return "("+str(i)+","+str(j)+")"

def calcelate(arrays_value, i, j, max_value):
    global index

    arrays_value=arrays_value+print_array(i, j)

    if i==max_value and j==max_value:
        # print arrays_value
        # if arrays_value not in list_arrays:
        #     list_arrays.append(arrays_value)
        # list_arrays.append(arrays_value)
        index=index+1
        return
    
    for x in xrange(0,2):
        if i==max_value and j==max_value:
               return

        if x==0:
            if i<max_value:
                calcelate(arrays_value, i+1, j, max_value) 
            elif i==max_value:
                continue       
        else:
            if j<max_value:
                calcelate(arrays_value, i, j+1, max_value)
            elif j==max_value:
                continue



i=0
j=0
arrays_value=""

calcelate(arrays_value, i, j, 10)

# list_arrays=list(set(list_arrays))

# print len(list_arrays)
# for x in list_arrays:
#     print x

print index

