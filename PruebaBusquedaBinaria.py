'''
Created on 03/12/2018

@author: acer
'''


def busquedaBinaria(unaLista, elemento):
    primero = 0
    ultimo = len(unaLista) -1
    while(primero <= ultimo):
        centro = int((primero + ultimo) / 2)
        valorCentro = unaLista[centro]
        print("Comparando " + str(elemento) + " con " + str(unaLista[centro]))
        
        if elemento == valorCentro:
            return centro
        elif elemento < valorCentro:
            ultimo = centro - 1
        else:
            primero = centro + 1
    return -1

listaPrueba = [0, 1, 2, 8, 13, 17, 19, 32,  42]
busquedaBinaria(listaPrueba, 3)
print("----------------------")
busquedaBinaria(listaPrueba, 13)


