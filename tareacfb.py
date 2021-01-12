# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 23:23:51 2021

@author: ANGY
"""
fic = open('texto.txt', "r")

caracteres= []
caracteres2=[]
pruebap=[]
contadorc=[]
for linea in fic:
    for c in linea:
        if(c!=' ' and c!='\n' and c!= '\xad'):
            caracteres.append(c)

print("\t=============================")
print("\tTEXTO SEPARADO POR CARACTERES")
print("\t=============================")
print(caracteres)

dato=input("Cual es el conjunto de letras que deseas buscar? ")
for caracter in dato:
     caracteres2.append(caracter)
     
print(caracteres2)     
print("\t====================================================================")
print("\tSEPARACION DEL TEXTO EN CADENAS DE LONGITUD DE LA PALABRA A BUSCAR")
print("\t====================================================================")

for indice in range(len(caracteres)-len(caracteres2)):
    if (caracteres2[0]==caracteres[indice]):
        for c in range(len(caracteres2)):   
            pruebap.append(caracteres[indice+c])
        print("",indice+1,pruebap,end="")
    if (pruebap==caracteres2):
            contadorc.append(indice)
            
    pruebap=[]    

    
print("\n\t=============================================")
print("\tPOSICIONES EN LAS QUE SE ENCUENTRA LA PALABRA",caracteres2)
print("\t=============================================")
if(len(contadorc)!=0):
    for indice in range(len(contadorc)):
        print("\nLa ocurrencia",indice+1,"se encuentra en la posicion:",\
              contadorc[indice]+1)
if(len(contadorc)==0):
    print("No se encontro la cadena")

fic.close()

