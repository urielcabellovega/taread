# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 23:23:51 2021

@author: ANGY
"""
fic = open('texto.txt', "r")

caracteres= []

for linea in fic:
    for c in linea:
        if(c!=' ' and c!='\n' and c!= '\xad'):
            caracteres.append(c)
        
print(caracteres)

for indice in range(len(caracteres)-3):
    pruebap= (caracteres[indice],caracteres[indice+1],caracteres[indice+2],\
              caracteres[indice+3])
    #print(pruebap)
    
fic.close()
