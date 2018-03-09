# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 15:16:19 2018

@author: Administrator
"""
"""
Calculate the distance between each two lines and save as an array
Find the minest sum of distance.
"""
#Calculate the similarity between each pair of the curves

from fastdtw import fastdtw
import sys
from datetime import datetime

import VR2Position

def position(rows):
    
    #rows = VR2Position.rows
    #l,r = VR2Position.Position()
    #rows = rows[l:r+1]
    
    cnt = len(rows)
    dtw = [[0 for i in range(cnt)] for j in range(cnt)]
    
    #print(datetime.now())
    for i in range(cnt):
        X = []
        for k in range(1,49):
            string = 'SPFB'+str(k)
            X.append(int(rows[i][string]))
        for j in range(cnt):
            if i != j:
                #Y = []
                ans = 0
                for k in range(1,49):
                    string = 'SPFB'+str(k)
                    ans += abs(X[k-1]-int(rows[j][string]))
                    #Y.append(float(rows[j][string]))
                #dtw[i][j],_ = fastdtw(X,Y, dist = lambda x,y:abs(x-y))
                dtw[i][j] = ans
                #dtw[j][i] = dtw[i][j]
        #print('end',i)
    #print(datetime.now())
    
    #print(dtw)
    Min = sys.maxsize
    for i in range(cnt):
        ans = 0
        for j in range(cnt):
            ans += dtw[i][j]
        if ans < Min:
            Min = ans
            underline = i
            
    #print('minest',Min, underline)
    return underline