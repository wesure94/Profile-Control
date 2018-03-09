# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 14:37:05 2018

@author: Administrator
"""
"""
Locate the start and end point according to its speed term
Find the max speed and set a constant(ex. 100) range
"""

#According to VR, locate the three positions. Header, Middle, and Tail

import csv

#file_path = open('E:\BaoSight/Codes/ASCDATA/writefile/26020003    _10_extract.csv')
#csv_reader = csv.DictReader(file_path)
#rows = [row for row in csv_reader]

def Position(rows):
    speed = []
    for i in range(len(rows)):
        speed.append(float(rows[i]['Speed[m/10m]']))
    max_speed = max(speed)
    delta = 100
    
    for i in range(len(speed)):
        if speed[i] > max_speed - delta:
            break
        
    for j in range(len(speed)-1,-1,-1):
        if speed[j] > max_speed - delta:
            break
        
    return i,j