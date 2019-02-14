# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 11:32:42 2018

@author: david
"""

"""
Practica 1

Al ejecutar el archivo se irán ejecutando los ejercicios uno a uno. Cuando salga
una imagen presionar ESC para cerrar la ventana y para ejecutar el siguiente ejercicio
presionar ENTER en la terminal.

"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

def read_image(path, mode):

    if mode==0:
        print("Reading {} in grey mode".format(path))
    elif mode==1:
        print("Reading {} in RGB mode".format(path))
    else:
        print("Mode must be: 0, 1")
     
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



#Uso de gaussianBlur para comprobar como afectan los distintos parámetros al 
# aplicar el filtro a una iamgen

def ejercicio1a():
    
    print("Ejercicio 1 - Apartado a")
    print()
    
    path = 'imagenes/'
    title = 'einstein'
    formato = '.bmp'
    
    img = read_image(path+title+formato, 1)

    images = []
    
    kernels = [5,11,17]
    sigmas = [1, 5, 9]
    
    
    print()
    
    for k in kernels:
        
        aux = img.copy()
        
        for s in sigmas:
            
            print("Using kernel ({},{} and sigma: {})".format(k,k,s))
            
            dst = cv2.GaussianBlur(img,(k,k),s, cv2.BORDER_DEFAULT)
    
#            print("Shape: ", dst.shape)
        
            images.append(dst)

        print()

        for i in images:
            aux = np.concatenate((aux,i),axis=1)
        
        print_image("Kernel: {}, sigma: {}".format(k, sigmas), aux)
        
        images.clear()
        
    print()



def ejercicio1b():
    
    print("Ejercicio 1 - Apartado b")
    print()
    
    kernels = [1,3,5,7]
    
    for k in kernels:
        print("Using kernel: ", k)
        deriv = cv2.getDerivKernels(dx=1, dy=0, ksize=k, normalize=True)
            
        print("Derived mask rows: ",deriv[0])
        print()
        print("Derived mask columns: ",deriv[1])
        print()
        
#        Máscara como el producto de la derivada respecto a y
        aux = np.dot(deriv[1],deriv[1].transpose())
        
#        print("Aux: ",aux)
#        print()
        
        
#       Aumentamos el tamaño de la máscara y la realzamos
        aux = cv2.resize(aux, None, fx=50, fy=50, interpolation = cv2.INTER_CUBIC)
        aux = aux*4
        
        print_image("Convolution ksize={}".format(k),aux)
        
        print("----------------------------------------")
        
    print()
        

# Uso de Laplacian y Sobels para ver como actuan los filtros para realzar los
# bordes de una imagen
def ejercicio1c():    
    
    print("Ejercicio 1 - Apartado c")
    print()
    
    path = 'imagenes/'
    title = 'submarine'
    formato = '.bmp'
    
    img = read_image(path+title+formato, 0)
    
    img = img.astype(np.uint8)

#    Borders constant, replicate
    borders = [0,2]
    kernel = [3,5]

    imgs = []
    sobels = []

    for d in kernel:
        aux = img.copy()
                
        for b in borders:
        
            laplacian = cv2.Laplacian(img.copy(),cv2.CV_8U,ksize=d,borderType=b)
            sobelx = cv2.Sobel(img.copy(),cv2.CV_8U,1,0,ksize=d)
            sobely = cv2.Sobel(img.copy(),cv2.CV_8U,0,1,ksize=d)
                
            sobels = cv2.Sobel(img.copy(),cv2.CV_8U,1,0,ksize=d)
            sobels = cv2.Sobel(sobels,cv2.CV_8U,0,1,ksize=d)

            sobelss = cv2.Sobel(img.copy(),cv2.CV_8U,1,1,ksize=d)
            sobelss *= 10
            

            # Combinación de las derivadas respecto a x e y
            x = sobelx + sobely
            
            print_image("Sum der x + der y", x)
            print_image("der x, der y", sobels)
            print_image("der x, der y", sobelss)

            aux = np.concatenate((aux,laplacian),axis=1)
            s = np.concatenate((sobelx,sobely),axis=1)
            s = np.concatenate((s,x),axis=1)
            
        imgs.append(aux)
        sobels.append(s)

    
    
    for i,k,s in zip (imgs,kernel,sobels):
        print_image("Laplacian with {} kernel size, constant border and reflect border".format(k), i)
        print_image("Sobels with {} kernel size".format(k), s)
        
    print()

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------


def ejercicio2a():
    
    print("Ejercicio 2 - Apartado a")
    print()
    
    path = 'imagenes/'
    title = 'einstein'
    formato = '.bmp'
    
    img = read_image(path+title+formato, 0)
    
    img = cv2.resize(img, None, fx=1.6, fy=1.6, interpolation = cv2.INTER_CUBIC)
    
    img = img.astype(np.uint8)
    
    ksize = [3,7]
    
    sigma = 3
        
    for k in ksize:
    
        # Kernel gaussiano de 1D
        kernel = cv2.getGaussianKernel(k, sigma, ktype=cv2.CV_64F )
        
        # Lo multiplicamos por el mismo para obtener la convolucion
        conv = kernel*np.transpose(kernel)
        
        print("Convolution 2D: ", conv)    
    
    
        res = cv2.filter2D(src=img, ddepth=cv2.CV_8U, kernel=conv, borderType=cv2.BORDER_REFLECT)
        
        print_image("Gaussian kernel ksize={}, sigma=3".format(k), res)
        

def ejercicio2b():
    
    print("Ejercicio 2 - Apartado b")
    print()
    
    path = 'imagenes/'
    title = 'einstein'
    formato = '.bmp'
    
    img = read_image(path+title+formato, 0)
    
    img = cv2.resize(img, None, fx=1.4, fy=1.4, interpolation = cv2.INTER_CUBIC)
    
#    img = img.astype(np.uint8)
    
    kernels = [3,9]
    
    for  k in kernels:
        deriv = cv2.getDerivKernels(dx=1, dy=0, ksize=k, normalize=True)
        
        #Probamos a aplicar los kernels separables que hemos obtenido de las derivadas
        convx = cv2.sepFilter2D(src=img, ddepth=cv2.CV_64F, kernelX=deriv[0], kernelY=deriv[1], borderType=cv2.BORDER_CONSTANT)
        convy = cv2.sepFilter2D(src=img, ddepth=cv2.CV_64F, kernelX=deriv[1], kernelY=deriv[0], borderType=cv2.BORDER_CONSTANT)
    
        a = convx + convy
        
        i = np.hstack((convx,convy,a))
        
        print_image("Derivatives x, y and sum, k={}".format(k), i)
        
                
def ejercicio2c():
    
    print("Ejercicio 2 - Apartado c")
    print()
    
    path = 'imagenes/'
    title = 'cat'
    formato = '.bmp'
    
    img = read_image(path+title+formato, 0)
    
    img = cv2.resize(img, None, fx=1.1, fy=1.1, interpolation = cv2.INTER_CUBIC)
 
    kernels = [3, 15]
    
    for k in kernels:
        
        # Segunda derivada respecto a x e y
        deriv = cv2.getDerivKernels(dx=2, dy=0, ksize=k, normalize=True)
        
        # En este caso hacemos la combinación de las máscaras separables para obtener
        # una convolución de segunda derivada (laplaciana)
        conv = deriv[0]*np.transpose(deriv[1])
            
        print("Convolution: ", conv)
    
        
        res = cv2.filter2D(src=img, ddepth=cv2.CV_32F, kernel=conv, borderType=cv2.BORDER_DEFAULT)
        
        print_image("Second derivative, k={}".format(k), res)
    




    
# Implementado para ver cómo la imagen decrece con las iteraciones de pyrDown pero 
# manteniendo la escala original para que sea más fácil percibir las diferencias
        
# Para ver el funcionamiento sin escalado ejecutar la función   ejercicio2d1()            
def ejercicio2d():
    
    print("Ejercicio 2 - Apartado d")
    print()
    
    path = 'imagenes/'
    title = 'cat'
    formato = '.bmp'
    
    img = read_image(path+title+formato, 0)
                
    img = cv2.resize(img, None, fx=0.7, fy=0.7, interpolation = cv2.INTER_CUBIC)

    borders = [cv2.BORDER_DEFAULT, cv2.BORDER_REFLECT]

    
    for b in borders:
        current = img.copy()
        imgs = img.copy()
 
        
        print("Using border = ", b)
        print()
        print("Level = 0")
        print_image("Original image, b={}".format(b), current)

        

        for i in range(1,5):
            print("Level = ", i)
            
#           Hacemos más pequeña la imagen con pyrDown, con pyrUp convertimos esa 
#           imagen a la escala que tenía antes para poder apreciar los cambios mejor
            aux = cv2.pyrDown(current, borderType=b)
            
            aux = cv2.pyrUp(aux,  dstsize=(current.shape[1],current.shape[0]))
                   
            imgs = np.hstack((imgs, aux))
                
            current = aux

            print_image("Pyramid lvl={} b={}".format(i,b), aux)
            
        print("-------------------------------")
        
        print_image("Pyramid levels with b = {}".format(b), imgs)
    


def ejercicio2d1():
    print("Ejercicio 2 - Apartado d")
    print()
    
    path = 'imagenes/'
    title = 'cat'
    formato = '.bmp'
    
    img = read_image(path+title+formato, 0)
    img = cv2.resize(img, None, fx=0.7, fy=0.7, interpolation = cv2.INTER_CUBIC)
    borders = [cv2.BORDER_DEFAULT, cv2.BORDER_REFLECT]

    for b in borders:
        current = img.copy()       
        print("Using border = ", b)
        print()
        print("Level = 0")
        print_image("Original image, b={}".format(b), current)        

        for i in range(1,5):
            print("Level = ", i)
            
            aux = cv2.pyrDown(current, borderType=b)
            current = aux

            print_image("Pyramid lvl={} b={}".format(i,b), aux)
            
        print("-------------------------------")

    

#------------------------------------------------------------------------------


def ejercicio2e():
    
    print("Ejercicio 2 - Apartado e")
    print()
    
    path = 'imagenes/'
    title = 'cat'
    formato = '.bmp'
    
    img = read_image(path+title+formato, 0)
    
    img = cv2.resize(img, None, fx=0.7, fy=0.7, interpolation = cv2.INTER_CUBIC)

        
    borders = [cv2.BORDER_DEFAULT, cv2.BORDER_REFLECT]
    
    for b in borders:
        current = img.copy()
        imgs = img.copy()

        print("Using border = ", b)
        print()
        print("Level = 0")
        print_image("Original image, b={}".format(b), current)
        
        for i in range(1,5):
        
            print("Level = ", i)
            
            pd = cv2.pyrDown(current, borderType=b)
            
            pu = cv2.pyrUp(pd, dstsize=(current.shape[1],current.shape[0]))
            
            # Restamos en cada iteración la nueva imagen que hemos obtenido tras
            # hacer pyrDown y pyrUp
            
            aux = current - pu
            
            print_image("Laplacian Pyramid lvl {}".format(i), aux)
            
            imgs = np.hstack((imgs, aux))
            
            current = pu
        
        print("-------------------------------")

        print_image("Laplacian Pyramid using b = {}".format(b), imgs)
        

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Con un mismo kernel aplicamos el filtro a dos imágenes y las combinamos
def hybrid(a, b, k):
   
    gauss = cv2.getGaussianKernel(k , sigma=11, ktype=cv2.CV_64F)
    gauss = gauss*np.transpose(gauss)
    
    a = cv2.filter2D(src=a, ddepth=cv2.CV_64F, kernel=gauss, borderType=cv2.BORDER_DEFAULT)
    
    # Filtro realce usando la misma máscara que para el de alisamiento
    lap = cv2.filter2D(src=b, ddepth=cv2.CV_64F, kernel=gauss, borderType=cv2.BORDER_DEFAULT)    
    b = b-lap
        
    aux = np.hstack((a,b))
    
    #Con la función add conseguimos no hacer una suma que haga que la imagen salga blanca
    res = cv2.add(a,b)
    
    aux = np.hstack((aux, res))
    
    print_image("Hybrid image", aux)
    
    
    

def ejercicio3a():
    print("Ejercicio 3 - Apartado a")
    print()
    
    path = 'imagenes/'
    title = 'cat'
    formato = '.bmp'
    
    #Convertimos imagen al rango (0,1)
    a = read_image(path+title+formato, 0)/255.0
    b = read_image(path+"dog"+formato, 0)/255.0
    
    #K size depende del tamaño de las imagenes originales
    k = np.int(np.ceil(a.shape[1]/16))
        
    if(np.mod(k,2) == 0):
        k=k+1
        
    print("Kernel size = ", k)
    
    hybrid(a,b, k)
    
    
def ejercicio3b():
    print("Ejercicio 3 - Apartado b")
    print()
    
    path = 'imagenes/'
    formato = '.bmp'
    
    titles = [["cat", "dog"], ["einstein","marilyn"], ["plane", "bird"], ["fish", "submarine"], ["bicycle", "motorcycle"]]
    
    for t in titles:
        a = read_image(path+t[0]+formato, 1)/255.0
        b = read_image(path+t[1]+formato, 1)/255.0
        
        k = np.int(np.ceil(a.shape[1]/16))
        
        if(np.mod(k,2) == 0):
            k=k+1
        
        print("Kernel size = ", k)
        
        hybrid(a,b,k)


    
#    
#ejercicio1a()
#input("Press Enter to continue...\n\n")
#ejercicio1b()
#input("Press Enter to continue...\n\n")
#ejercicio1c()
#input("Press Enter to continue...\n\n")
#
#ejercicio2a()
#input("Press Enter to continue...\n\n")
#ejercicio2b()
#input("Press Enter to continue...\n\n")
#ejercicio2c()
#input("Press Enter to continue...\n\n")
#ejercicio2d()
##ejercicio2d1()
#input("Press Enter to continue...\n\n")
#ejercicio2e()    
#
#input("Press Enter to continue...\n\n")
#ejercicio3a()    
#input("Press Enter to continue...\n\n")
#ejercicio3b()      
        
ejercicio2e()
        
#ejercicio2e()