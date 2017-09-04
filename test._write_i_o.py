# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 11:28:54 2017

@author: User
"""

test = ['hello','world']

file = open ('test_write.csv', 'w')

for line in test:
    file.write(line +'\n')
    print (line+'\n')


