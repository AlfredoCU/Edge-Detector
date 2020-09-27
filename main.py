#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 20:16:22 2020

@author: alfredocu
"""

# Biblioteca para trabajar con datos numéricos.
import numpy as np
# Biblioteca para crear graficas.
import matplotlib.pyplot as plt
# Biblioteca para trabajar con imagenes.
import matplotlib.image as mpimg

# f crea una figuara con unas dimenciones.
# axes es una matriz de objetos.
f, axes = plt.subplots(2, 2)
# print(f)
# print(axes)

# Leer una imgaen en una matriz.
img = mpimg.imread('Gal.jpg')
# print(img)

# Obtener las dimensiones de la imagen.
height, width, layer = img.shape
# print(height) # Alto
# print(width) # Ancho
# print(layer) # Imagenes RGB -> 3 RGBA -> 4 y si no tienen es escala de grises.
# print(img.shape) # Es una tupla

# Pasar a escala de grises.
imgGray = np.zeros((height, width))
# print(imgGray) # Devuelve una matriz llena de ceros con las dimenciones de la imagen original.

# Un for para iterar hasta height -> range(675) ayuda crea una secuencia de números. 0 - 674
for i in range(height):
    # Un for para iterar hasta widght -> ranger(1080) crea una secuenca de números. 0 - 1079
    for j in range(width):
        # La función int () convierte el valor especificado en un número entero.
        # Devuelve un objeto entero construido a partir de un número o cadena.
        imgGray[i, j] = (int(img[i, j, 0]) + int(img[i, j, 1]) + int(img[i, j, 2])) // 3 # Canales RGB
        
#print(imgGray) # La matriz de 0 se llena con valores de la img original.

# Crear filtro. Umbralizar
sobel1 = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
#print(sobel1) # Se crea una matriz.

imgSobel = np.zeros((height - 2, width - 2))
# print(imgSobel) # Se crea una matriz de ceros con dimenciones menos 2.

imgFinal = np.zeros((height - 2, width - 2))
# print(imgFinal) #  Se crea una matriz de ceros con dimenciones menos 2.

for i in range(1, height - 1):
    for j in range(1, width - 1):
        imTemp = imgGray[i - 1: i + 2, j - 1: j + 2] # Creamos un temporal
        temp = np.abs((sobel1 * imTemp).sum())
        imgSobel[i - 1][j - 1] = temp
        # 255 pixels
        if temp > 255:
            # Bordes más fuertes.
            imgFinal[i - 1][j - 1] = True
        else:
            # Bordes menos fuertes.
            imgFinal[i - 1][j - 1] = False

# Imagen 1
axes[0, 0].imshow(img) # Imagen.
axes[0, 0].set_title("Imagen original") # Titulo de la gráfica.

# Imagen 2
axes[0, 1].imshow(imgGray, cmap=plt.cm.gray)
axes[0, 1].set_title("Escala de grises")

# Imagen 3
axes[1, 0].imshow(imgSobel, cmap=plt.cm.gray)
axes[1, 0].set_title("Imagen Filtrada")

# Imagen 4
axes[1, 1].imshow(imgFinal, cmap=plt.cm.binary)
axes[1, 1].set_title("Bordes")

# Ajuste de los limites, 
f.subplots_adjust(hspace=0.5) # hspace -> La altura del relleno entre subparcelas, como una fracción de la altura promedio de los ejes.
plt.show() # Es una función que nos dibuja la gráfica.

f.savefig('Detector_de_bordes.eps', format="eps") # Es para guardar una imagen en un formato eps, para mejor calidad de imagen.
