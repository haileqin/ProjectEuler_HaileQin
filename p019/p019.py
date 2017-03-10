#!/usr/bin/python
# -*- coding: utf-8 -*-

# week 1-7 sun-sat
# month 1-12
# year 1901-2000

week_day=2

def week_calculate(week_day, days):
    week_day=(week_day+days)%7

    return week_day


for x in xrange(1901,2000+1):
    for y in xrange(1,12+1):
    	print x, y, 1, week_day

        if y==1: #31
            if x==1901:
            	week_day=week_calculate(week_day, 31)
            	continue
            
        elif y==2: #28,29
            if (x%4==0 and x%100!=0) and x%400==0:
                week_day=week_calculate(week_day, 29)
            else:
                week_day=week_calculate(week_day, 28)
        elif y==3: #31
            week_day=week_calculate(week_day, 31)
        elif y==4: #30
            week_day=week_calculate(week_day, 30)
        elif y==5: #31
            week_day=week_calculate(week_day, 31)
        elif y==6: #30
            week_day=week_calculate(week_day, 30)
        elif y==7: #31
            week_day=week_calculate(week_day, 31)
        elif y==8: #31
            week_day=week_calculate(week_day, 31)
        elif y==9: #30
            week_day=week_calculate(week_day, 30)
        elif y==10: #31
            week_day=week_calculate(week_day, 31)
        elif y==11: #30
            week_day=week_calculate(week_day, 30)
        elif y==12: #31
            week_day=week_calculate(week_day, 31)

        






