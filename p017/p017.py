#!/usr/bin/python
# -*- coding: utf-8 -*-

dics={0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8,20:6, \
      30:6,40:5,50:5,60:5,70:7,80:6,90:6,100:7,1000:11}

sum_val=0

for x in xrange(1,1001):
    cal_val=0

    if x<100:
        if x<=20:
            cal_val=dics.get(x)
        else:
            cal_val=dics.get(x-x%10)+dics.get(x%10)
    elif x>=100 and x<1000:
        if x%100==0:
            cal_val=dics.get(x/100)+dics.get(100)
        elif x%100<=20 and x%100>0:
            cal_val=dics.get(x%100)+dics.get(x/100)+dics.get(100)+3#3:and
        elif x%100>20 :
            cal_val=dics.get(x%100-x%100%10)+dics.get(x%100%10)+dics.get(x/100)+dics.get(100)+3#3:and     
    elif x>=1000:       
        cal_val=dics.get(1000)

    print x, cal_val
    sum_val=sum_val+cal_val
        

print "total sum:",sum_val
