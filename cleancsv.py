# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 10:51:41 2018

@author: Administrator
"""
"""
Clean up the dataset, turn each excel file into a new file with useful terms we needed
"""

import csv
import os

path = 'E:\BaoSight/20辊板型数据/ASCDATA/'
files = os.listdir(path)
for file_list in files:
    eachfile = os.path.join(path,file_list)
    filename = file_list.split('.')[0]
    #csv_reader = csv.DictReader(open('E:\BaoSight/20辊板型数据/ASCDATA/26020003    _5.csv'))
    csv_reader = csv.reader(open(eachfile))
    rows = [row for row in csv_reader]
    """
    Number = rows[0][1]             #Coil No.   type:string
    Grade = rows[1][1]              #Grade      type:string
    Width = int(rows[2][1])         #Width      type:int
    ThicknessIn = int(rows[3][1])   #Thickness  type:int
    ThicknessOut = int(rows[3][2])  #Thickness  type:int
    PassNoIn = int(rows[4][1])      #PassNo.    type:int
    PassNoOut = int(rows[4][2])     #PassNo.    type:int
    PassNoDir = int(rows[4][3])     #PassNo.    type:int
    """
    writepath = os.path.join('writefile/',filename + '_extract.txt')
    writer = open(writepath,'w')
    for i in range(5):
        for j in range(len(rows[i])):
            writer.write(rows[i][j]+'\t')
        writer.write('\n')
    writer.close()
    
    rows = rows[6:]
    fieldnames = ['Counter','Speed[m/10m]','asu_fb1_1','asu_fb1_2','asu_fb1_3',
                  'asu_fb1_4','asu_fb1_5','asu_fb1_6','asu_fb1_7','lat_fb1','lat_fb2',
                  'SPFB1','SPFB2','SPFB3','SPFB4','SPFB5','SPFB6','SPFB7','SPFB8','SPFB9',
                  'SPFB10','SPFB11','SPFB12','SPFB13','SPFB14','SPFB15','SPFB16','SPFB17',
                  'SPFB18','SPFB19','SPFB20','SPFB21','SPFB22','SPFB23','SPFB24','SPFB25',
                  'SPFB26','SPFB27','SPFB28','SPFB29','SPFB30','SPFB31','SPFB32','SPFB33',
                  'SPFB34','SPFB35','SPFB36','SPFB37','SPFB38','SPFB39','SPFB40','SPFB41',
                  'SPFB42','SPFB43','SPFB44','SPFB45','SPFB46','SPFB47','SPFB48']
    writepath = os.path.join('writefile',filename + '_extract.csv')
    csv_file = open(writepath,'w',newline = '')
    csv_writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
    csv_writer.writeheader()
    for i in range(len(rows)):
        #if rows[i][0] == 'Coil No.':
        #    break
        for j in range(111,158):
            rows[i][j] = int(rows[i][j])
        if rows[i][137]==0 and rows[i][138]==0 and rows[i][139]==0 and rows[i][140]==0 and rows[i][134]==0 and rows[i][135]==0 and rows[i][136]==0:
            continue
        else:
            csv_writer.writerow({'Counter':rows[i][0],'Speed[m/10m]':rows[i][3],'asu_fb1_1':rows[i][38],
                                  'asu_fb1_2':rows[i][39],'asu_fb1_3':rows[i][40],'asu_fb1_4':rows[i][41],
                                  'asu_fb1_5':rows[i][42],'asu_fb1_6':rows[i][43],'asu_fb1_7':rows[i][44],
                                  'lat_fb1':rows[i][58],'lat_fb2':rows[i][59],'SPFB1':rows[i][111],
                                  'SPFB2':rows[i][112],'SPFB3':rows[i][113],'SPFB4':rows[i][114],
                                  'SPFB5':rows[i][115],'SPFB6':rows[i][116],'SPFB7':rows[i][117],
                                  'SPFB8':rows[i][118],'SPFB9':rows[i][119],'SPFB10':rows[i][120],
                                  'SPFB11':rows[i][121],'SPFB12':rows[i][122],'SPFB13':rows[i][123],
                                  'SPFB14':rows[i][124],'SPFB15':rows[i][125],'SPFB16':rows[i][126],
                                  'SPFB17':rows[i][127],'SPFB18':rows[i][128],'SPFB19':rows[i][129],
                                  'SPFB20':rows[i][130],'SPFB21':rows[i][131],'SPFB22':rows[i][132],
                                  'SPFB23':rows[i][133],'SPFB24':rows[i][134],'SPFB25':rows[i][135],
                                  'SPFB26':rows[i][136],'SPFB27':rows[i][137],'SPFB28':rows[i][138],
                                  'SPFB29':rows[i][139],'SPFB30':rows[i][140],'SPFB31':rows[i][141],
                                  'SPFB32':rows[i][142],'SPFB33':rows[i][143],'SPFB34':rows[i][144],
                                  'SPFB35':rows[i][145],'SPFB36':rows[i][146],'SPFB37':rows[i][147],
                                  'SPFB38':rows[i][148],'SPFB39':rows[i][149],'SPFB40':rows[i][150],
                                  'SPFB41':rows[i][151],'SPFB42':rows[i][152],'SPFB43':rows[i][153],
                                  'SPFB44':rows[i][154],'SPFB45':rows[i][155],'SPFB46':rows[i][156],
                                  'SPFB47':rows[i][157],'SPFB48':rows[i][158]})
    csv_file.close()
    
