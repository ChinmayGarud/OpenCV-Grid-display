# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 12:20:39 2021

@author: Chinmay Garud
"""

import cv2
import numpy as np
import json

with open('data.txt') as json_file:
    data = json.load(json_file)

directory = 'C:/Users/student/Desktop/P/Railways/13--Interview'
display = []

size= (24,24)
dis = []
l = 0
ld = 0
for face in data:
    img = cv2.imread(directory+'/'+face)
    for i in data[face]:
        x,y,w,h = i
        fc = img[abs(y):abs(y+h), abs(x):abs(x+w)]
        fc_ = cv2.resize(fc,size)
        if l!=4:
            if l==0:
                dis = fc_
            else:
                dis = np.concatenate((dis, fc_),axis = 1)
            l+=1
        else:
            if ld==0:
                display = dis
            else:    
                display = np.concatenate((display,dis),axis = 0)
            ld+=1
            l = 0
pixels = 0
no = 1
while pixels< len(display):
    if pixels+96<len(display):
        v = display[pixels:pixels+96,:]
    else:
        v = display[pixels:,:]
    cv2.imwrite('result_'+ str(no)+'.png', v)
    pixels+=96
    no+=1

