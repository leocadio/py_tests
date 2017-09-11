# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 19:10:54 2017

@author: leocadio
"""
import os
import pandas as pd
import re

'''
path = "c:\\test\\acars_ls71241.txt"
file = open (path,'r')
print(file.readlines()[9])
'''

acars_set = []
path = "c:\\test\\ACARS_LS"
for filename in os.listdir(path):
    file = open (path+'\\'+ filename ,'r')
    count = 0
    acars_subset = []
    for line in file:
        count+=1
        newline = line.rstrip('\r\n')
        if count == 9:
            acars_subset.append(newline)
        elif count == 10:
            acars_subset.append(newline)
        elif re.search('PAYLOAD',newline):
            acars_subset.append(newline)
        elif re.search('MZFW',newline):
            acars_subset.append(newline)
        elif re.search('UNDLD',newline):
            acars_subset.append(newline)
            acars_set.append(acars_subset)
    file.close()

pd.DataFrame(acars_set).to_csv('C:\\projects\\Aeroflot\\dgp\\test.csv')