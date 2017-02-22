#!/usr/bin/python
# -*- coding: utf-8 -*-
index_val=0

def calculate(i, j, max_val):
    global index_val
    if j==max_val and j==max_val:
        index_val=index_val+1
        return

    for x in xrange(0,2):
        if x%2==1:
            if i<max_val:
                calculate(i+1, j, max_val)
            else:
                return
            

        if x%2==0:
            if j<max_val:
                calculate(i, j+1, max_val)
            else:
                return

     
def max_number_matrix(max_val):
    global index_val         
    index_val=0
    calculate(0, 0, max_val)
    print str(max_val)+"x"+str(max_val)+":", index_val




for x in xrange(2,21):
    max_number_matrix(x)
