# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 14:28:11 2017

@author: david
"""

list=[2,8,8,8,8,7,9,8,10,11,9,12]

def sd(list):#計算標準差的函式
    n=len(list)#取得n值:數列的個數
    thesum=0#作為儲存數列的總和的變數
    sigma=0
    for i in range(n):
        thesum+=list[i]
    u=thesum/n #平均值u
    
    
    for i in range(n):
        sigma+=(list[i]-u)**2
        
    sd=(sigma/n)**0.5
        
    return sd

print(list,"的標準差為:",sd(list))

