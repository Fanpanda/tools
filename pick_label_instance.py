# -*- coding: utf-8 -*-
"""
Created on Thu Dec 07 23:18:06 2017

@author: 35901
"""
import os
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


root=r'D:/DataSets/cityscape/gtFine_trainvaltest/gtFine/val'
sv_root=r'C:/Users/Administrator/Desktop/label/'
subroot=os.listdir(root)
for x in xrange(len(subroot)):
    if  os.path.exists(sv_root+subroot[x])==0:
        os.mkdir(sv_root+subroot[x])
    root_img=root+'/'+subroot[x]
    label=os.listdir(root_img)
    num=len(label)
    
    for i in xrange(num):
        if label[i][-15:-4]=='instanceIds':
            label_img=Image.open(root_img+'\\'+label[i])
            label_img=np.array(label_img)
#            plt.figure(i)
#            plt.imshow(label_img,cmap ='gray')
            plt.axis('off')
            new_label=np.zeros(label_img.shape,dtype=np.uint16)##创建新的label_map
            label_cls=1
            print i
            
            indx=np.where((label_img>25999)&(label_img<27000))
            new_label[indx[0],indx[1]]=label_img[indx[0],indx[1]]
#            plt.figure('new')
#            plt.imshow(new_label,cmap='gray')
#            plt.imsave('1.png',new_label,format='png',cmap=plt.cm.gray)
            
            I=Image.fromarray(new_label)
##            #I=I.resize((480,360))
            I.save(sv_root+subroot[x]+'/'+label[i][0:-3]+'tiff')
            print label[i][0:-3]
#           
