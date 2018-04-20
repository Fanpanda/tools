# -*- coding: utf-8 -*-
"""
Created on Thu Dec 07 23:18:06 2017

@author: 35901
"""
import os
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

root=r'D:/DataSets/cityscape/gtFine_trainvaltest/gtFine/train'
sv_root=r'C:/Users/Administrator/Desktop/label/'
subroot=os.listdir(root)
for x in xrange(len(subroot)):
    if  os.path.exists(sv_root+subroot[x])==0:
        os.mkdir(sv_root+subroot[x])
    root_img=root+'/'+subroot[x]
    label=os.listdir(root_img)
    num=len(label)
    classes={'person':24,'road':7,'car':26}
    for i in xrange(num):
        if label[i][-12:-4]=='labelIds':
            label_img=Image.open(root_img+'\\'+label[i])
            label_img=np.array(label_img)
#            plt.figure(i)
#            plt.imshow(label_img,cmap ='gray')
#            plt.axis('off')
            new_label=np.zeros(label_img.shape,dtype=np.uint8)##create new label maps
            label_cls=1
            print i
            for j in classes:
                indx=np.where(label_img==classes[j])
                new_label[indx[0],indx[1]]=label_cls
                label_cls=label_cls+1
#            plt.figure('new')
#            plt.imshow(new_label,cmap='gray')
            I=Image.fromarray(new_label)
            I=I.resize((480,360))
            I.save(sv_root+subroot[x]+'/'+label[i])
            
#           
