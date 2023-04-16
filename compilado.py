
# -*- coding: utf-8 -*-
from Postfix_AFN import PostifixToAFN 
import pickle

# cargar bytes desde archivos binarios
with open('afns.pkl', 'rb') as f:
    afns_bytes = f.read()
with open('afn_final.pkl', 'rb') as f:
    afn_final_bytes = f.read()

# convertir bytes a objetos
afns = pickle.loads(afns_bytes)
afn_final = pickle.loads(afn_final_bytes)

palabras = []
archivo = input("Ingrese el nombre del archivo a resolver:\n--> ") 
with open(archivo, 'r') as f:
    contenido = f.read()
    palabras = contenido.split()

resultado_verificaciones = []
for palabra in palabras:
    valor = afn_final.simular_cadena(palabra)
    try:
        if valor == False:
            resultado_verificaciones.append(
                "'" + palabra + "'" + " --> No se reconoce")
        if valor[0] == True:
            for afn in afns:
                if valor[1] in afn[1].ef:
                    resultado_verificaciones.append(
                        "'" + palabra + "'" + " --> " + str(afn[0][0]).upper())
                    break
    except:
        pass

# Escribir el resultado en el .txt
with open('file_resuelto.txt', 'w') as f:
    f.write(contenido)
    f.write('\n\n')
    for resultado in resultado_verificaciones:
        f.write(resultado)
        f.write('\n')

print("\nArchivo resuelto con exito")
