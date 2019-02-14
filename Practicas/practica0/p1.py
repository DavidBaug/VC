# -*- coding: utf-8 -*-
"""
Practica 0 

David Gil Bautista

45925324M

"""

import numpy as np
import cv2
from matplotlib import pyplot as plt


def read_image(path, mode):

    
    
    if (mode != 1 and mode != 0):
        print("Mode must be: 0, 1")
    elif mode==0:
        print("Reading {} in grey mode".format(path))
    elif mode==1:
        print("Reading {} in RGB mode".format(path))

    
    img = cv2.imread(path, mode)
    
    return img
    
def print_image(title, image):
    cv2.imshow(title,image)

    print("Press ESC to exit or S to save it")
    k = cv2.waitKey(0)
        
    name = title+'.png'
        
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite(name,image)
        cv2.destroyAllWindows()
        
    print()
    
    
def print_matrix(img):
    
    if(img.shape[-1] != 3):
        print("Printing Grey matrix")
    else:
        print("Printing RGB matrix")
    
    print()
    
    print(img)
    
def read_images(images):
    for img in images:
        print_image()
        
    
###############################################################################
###############################################################################

###############################################################################
###############################################################################


        
print()
print("Practica 0")
print()
print()


def ejercicio1():

    print()
    
    print("Ejercicio 1")
    print()
    print()
        
    image_name = 'rainbow'
            
    img = read_image('images/'+image_name+'.jpg', 0)
    print_image(image_name,img)
    
    img = read_image('images/'+image_name+'.jpg', 1)
    print_image(image_name,img)
    print()

###############################################################################

def ejercicio2():

    print()
    
    print("Ejercicio 2")
    print()
    print()
    
    image_name = 'rainbow'
            
    img = read_image('images/'+image_name+'.jpg', 0)
    print_matrix(img)
    
    print()
    
    img = read_image('images/'+image_name+'.jpg', 1)
    print_matrix(img)

###############################################################################
    
def ejercicio3():
    print()
    
    print("Ejercicio 3")
    print()
    print()
    
    names = ['rainbow', 'gradient','mountain']

    images = []

    for i in names:
        img = read_image('images/'+i+'.jpg', 1)
        print("image shape: ",img.shape)
        images.append(img)
    
#    Al cargar una imagen en escala de grises como si fuera una imagen en color
#        podemos seguir concatenando las matrices, aunque estamos desperdiciando
#        espacio ya que ocupamos una matriz de 3 dimensiones para una imagen que
#        necesita solo 2.
      
    img = read_image('images/rainbowgrey.png',1)
    images.append(img)
    
    original = cv2.resize(images[0], (300,300), interpolation = cv2.INTER_AREA)
        
    for i in np.arange(1,len(images)):
        aux = cv2.resize(images[i], (300,300), interpolation = cv2.INTER_AREA)
        
        original = np.concatenate((original, aux), axis=1)

        
        
    print_image("Imagenes", original)
           

###############################################################################
    

def ejercicio4():
    print()
    
    print("Ejercicio 4")
    print()
    print()
    
    image_name = 'mountain'
            
    img = read_image('images/'+image_name+'.jpg', 1)
    
    print_image("No modificada", img)
    

    repite = 1
          
    while repite==1:
        repite = 0
        
        fc = input("Introduce f/c para seleccionar fila o columna: ")

        num1 = int(input("Comienzo: "))
        num2 = int(input("Final: "))
        
        
        
        if fc == 'f' or fc == 'F':
            if (num1 >= 0 and num1 < img.shape[1] and num2>=num1 and num2 < img.shape[1]):
                img[num1:num2,::]=0
            else:
                print("El tamanio de la fila estar entre 0 y ",img.shape[1])
                repite = 1
                
        elif fc== 'C' or fc == 'c':
            if (num1 >= 0 and num1 < img.shape[0] and num2>num1 and num2 < img.shape[0]):
                img[::,num1:num2]=0
            else:
                print("El tamanio de la columna estar entre 0 y ",img.shape[0])
                repite = 1
        else:
            print("Esperado f o c")
            repite = 1
        
        print_image("Modificada", img)
        
        
###############################################################################

def ejercicio5():
    print()
    print("Ejercicio 5")
    print()
    print()
    names = ['rainbow', 'gradient','mountain']

    images = []

    for i in names:
        img = read_image('images/'+i+'.jpg', 1)
        print("image shape: ",img.shape)
        images.append(img)
          
    
    original = cv2.resize(images[0], (300,300), interpolation = cv2.INTER_AREA)
        
    for i in np.arange(1,len(images)):
        aux = cv2.resize(images[i], (300,300), interpolation = cv2.INTER_AREA)
        
        original = np.concatenate((original, aux), axis=1)

    titulo = ''
        
    for n in names:
        titulo = titulo + n + '                                                                              '
        
    print_image(titulo, original)
    
    
###############################################################################
    

#
#ejercicio1()
#input("Presiona cualquier tecla para continuar...")
#ejercicio2()
#input("Presiona cualquier tecla para continuar...")
ejercicio3()
input("Presiona cualquier tecla para continuar...")
ejercicio4()
input("Presiona cualquier tecla para continuar...")
ejercicio5()