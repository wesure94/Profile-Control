# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 15:19:50 2018

@author: Administrator
"""


import csv
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import VR2Position
#import apartspeed
import dismatrix


file_path = open('E:\BaoSight/Codes/ASCDATA/writefile/26020003    _10_extract.csv')
csv_reader = csv.DictReader(file_path)
rows = [row for row in csv_reader]
#rows = VR2Position.rows
#l,r = apartspeed.apartspeed()
l,r = VR2Position.Position(rows)
r = l-1
l = 0
print(l,r)

def update(k):
    Y1 = []
    X1 = []
    for j in range(5,43):
        column = 'SPFB' + str(j)
        #Y1.append(int(rows[loc[k]][column]))
        Y1.append(int(rows[loc][column]))
        X1.append(j)
    
    X = []
    Y = []
    for j in range(5,43):
        column = 'SPFB' + str(j)
        Y.append(int(rows[k][column]))
        X.append(j)
        
    ax.set_xlim(min(min(X),min(X1))-1,max(max(X),max(X1))+1)
    ax.set_ylim(min(min(Y),min(Y1))-1,max(max(Y),max(Y1))+1)
    #ax.set_ylim(-2000,8000)
    
    #plt.clf
    ax.plot(X1,Y1,color = 'red')
    line.set_data(X,Y)
    ax.figure.canvas.draw()
    #print(Y)
    print('update',k)
    return line

#loc = [0 for i in range(len(rows))]
#for i in range(len(l)):
for i in range(1):
    #t = dismatrix.position(rows[l[i]:r[i]+1])
    #for j in range(l[i],r[i]+1):
    #    loc[j] = t+l[i]
    t = dismatrix.position(rows[l:r])
    for j in range(l,r):
        loc = t+l
    
    plt.close()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    line, = ax.plot([],[])
        #plt.ion()
    #l,r = VR2Position.Position()
    #l = 0
    #r = 12
    #print('position:',l[i],r[i])

    #print(loc)
    
    #rangelist = range(l[i],r[i]+1)
    rangelist = range(l,r)
    
    ani = animation.FuncAnimation(fig, update, rangelist, interval = 200)
    plt.show()
