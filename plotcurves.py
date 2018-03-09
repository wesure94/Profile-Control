# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 15:19:50 2018

@author: Administrator
"""
"""
Visit all files and classify.
Classify feature: Grade No., Thickness, PassNo.,
Locate position: l,r, Plot the minest sum of distance in one file and calculate the average line and plot it.
"""

import csv
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import VR2Position
#import apartspeed
import dismatrix
import os
"""
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
"""
namelist = []
Gradelist = []
floder = 'E:\BaoSight/Codes/ASCDATA/writefile/'
file_list = os.listdir(floder)
for filenames in file_list:
    if filenames.endswith('.txt'):
        file = open(os.path.join(floder,filenames),'r').readlines()
        Grade = file[1].split('\t')[1]
        PassNo1 = file[4].split('\t')[1]
        PassNo2 = file[4].split('\t')[2]
        if PassNo1 == PassNo2:
            namelist.append(filenames)
            Gradelist.append(Grade+file[3].split('\t')[2])
            #print('thick:',file[3].split('\t')[1],file[3].split('\t')[2])

#print('namelist:',namelist)
#print('Gradelist:', Gradelist)
gradecnt = list(set(Gradelist))
#print(gradecnt)
name = [[]for i in range(len(gradecnt))]
for i in range(len(Gradelist)):
    if namelist[i] == '46040163    _10_extract.txt':
        continue
    Grade = Gradelist[i]
    name[gradecnt.index(Grade)].append(namelist[i].split('.')[0]+'.csv')
#for i in range(len(gradecnt)):
#    print(name[i])
    

print('name:',len(name))
tt = 39
for k in range(tt,tt+1):#len(name)):
    #plt.close()
    #plt.pause(10)
    plt.figure(k)
    y = [0 for i in range(49)]
    print('name[k]',len(name[k]))
    for i in range(len(name[k])):
        file = os.path.join(floder,name[k][i])
        
        file_path = open(file)
        csv_reader = csv.DictReader(file_path)
        rows = [row for row in csv_reader]
        print('filename:',name[k][i],'shape:',len(rows))
        #rows = VR2Position.rows
        #l,r = apartspeed.apartspeed()
        l,r = VR2Position.Position(rows)
        r = l-1
        l = 0
        print('l,r:',l,r)
        
        t = dismatrix.position(rows[l:r])
        for j in range(l,r):
            loc = t+l
        print('loc:',loc)
        Y1 = []
        X1 = []
        for j in range(1,49):
            column = 'SPFB' + str(j)
            #Y1.append(int(rows[loc[k]][column]))
            y[j-1] += int(rows[loc][column])/(len(name[k]))
            Y1.append(int(rows[loc][column]))
            X1.append(j)
        plt.plot(X1,Y1,label = i)
        
    for i in range(47,-1,-1):
        y[i+1] = y[i]
    plt.plot(X1,y[1:],marker = 'x')
    
    plt.legend(loc = 'upper right')
    plt.show()

"""
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
"""