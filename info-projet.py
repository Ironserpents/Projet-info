# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from random import randint
#affichage des 0 sur la map 
def genereMat(n,m):
    MAT=[[0 for j in range(m)]for i in range(n)]
    for i in range(1,len(MAT)):
        j=randint(0,len(MAT[i])-1)
        MAT[i][j-1]=1
    x=0
    #Apparition d objet
    i=randint(-1,4)
    j=randint(-1,9)
    if MAT[i][j]==0:
        MAT[i][randint(0,len(MAT[i])-1)]=2
    if MAT[i][j]==1:
        MAT[i][j+1]=2
