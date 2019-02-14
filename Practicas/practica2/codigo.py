# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 18:19:46 2018

@author: david
"""

import cv2
import math
from random import sample
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


def sift_points(img, ct, et):
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 
    sift = cv2.xfeatures2d.SIFT_create(contrastThreshold = ct, edgeThreshold = et)
    kp = sift.detect(gray,None)

    img=cv2.drawKeypoints(gray,kp, 0)
    
    
#    mostrar("SIFT",img)
    
#    cv2.imshow("SIFT Points", img)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
    
    return len(kp), img
    



def surf_points(img, hess):
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    surf = cv2.xfeatures2d.SURF_create(hessianThreshold = hess)
    kp, des = surf.detectAndCompute(img,None)

    img=cv2.drawKeypoints(gray,kp, 0)
#    img=cv2.drawKeypoints(img,kp, 0)

#    mostrar("SURF",img)

#    cv2.imshow("SURF Points", img)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()

    return len(kp), img

#------------------------------------------------------------------------------

def mostrar(titulo, imagen):
    plt.title(titulo)
    if len(imagen.shape) == 3:
        img = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        plt.imshow(img)
    else:
        img = imagen
        plt.imshow(img, cmap='Greys_r')
    
    plt.xticks([]), plt.yticks([])
    plt.show()


#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
    
#------------------------------------------------------------------------------

def ej1a1():
    
    print("Ejercicio 1 - Apartado a")
    print("SIFT")
    
    img = cv2.imread("imagenes/yosemite1.jpg")

    salir = False

    ct = [0.2, 0.15, 0.1, 0.08, 0.06, 0.04, 0.02]
    
    et = [5, 10, 15, 20, 25, 30]
    
    for c in ct:
        for e in et:
            num, img = sift_points(img, c, e)

            if num >= 1000:
                print("Contrast: ", c)
                print("Edge: ", e)
                mostrar("SIFT "+str(num)+" points", img)
                
                cv2.imshow("SIFT Points", img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                
                salir = True
        
            if salir:
                break
        if salir:
            break
        
    print()


def ej1a2():
    
    print("Ejercicio 1 - Apartado a")
    print("SURF")
    
    img = cv2.imread("imagenes/yosemite1.jpg")

    salir = False

    hess = [1000, 900, 800, 700, 600, 500, 400]

    
    for h in hess:
        num, img = surf_points(img, h)

        if num >= 1000:
            print("Hessian: ", h)
            mostrar("SURF "+str(num)+" points", img)
                
            cv2.imshow("SURF Points", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
            salir = True
        
        if salir:
            break

    print()

def ej1b1():
    
    print("Ejercicio 1 - Apartado b")
    print("SIFT")
    
    img = cv2.imread("imagenes/yosemite1.jpg")
    
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    sift = cv2.xfeatures2d.SIFT_create(contrastThreshold = 0.06, edgeThreshold = 5)
    kp = sift.detect(img,None)
    
    kp_octave = []
    kp_layer = []
    
    print("Key points", len(kp))
    
    print()
    
    color = [(255, 0 ,0),
             (0, 255, 0),
             (0, 0, 255),
             (255, 100, 50),
             (100, 50, 255),
             (50, 255, 100),
             (100, 190, 255)]
    
    for i in range(0, len(kp)):
#        print(((kp[i].octave>>8) & 0xFF))
        aux = (kp[i].octave) & 0xFF
        
        if aux>=128:
            aux |= -128
        
        center = (np.int(kp[i].pt[0]), np.int(kp[i].pt[1]))
        rad = np.int(kp[i].size)
        
        cv2.circle(img, center, rad, color[aux], 1)
        
        kp_octave.append(aux)
        kp_layer.append((kp[i].octave>>8) & 0xFF)

#    Octave
    unique, counts = np.unique(kp_octave, return_counts=True)
        
    for i, num in zip(unique, counts):    
        print("Octave {}, key points: {}".format(i, num))

    print()

#    Layer
    unique, counts = np.unique(kp_layer, return_counts=True)
    
    for i, num in zip(unique, counts):    
        print("Layer {}, key points: {}".format(i, num))
        
    mostrar("SIFT Points Octave", img)
        
    cv2.imshow("SIFT Points", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    print()
    
#    mostrar("SIFT Points", img)


def ej1b2():
    
    print("Ejercicio 1 - Apartado b")
    print("SURF")
    
    img = cv2.imread("imagenes/yosemite1.jpg")
    
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    
    surf = cv2.xfeatures2d.SURF_create(hessianThreshold = 900)
    kp, des = surf.detectAndCompute(img,None)
    
    kp_octave = []
    
    print("Key points", len(kp))
    
    print()
    
    color = [(255, 0 ,0),
             (0, 255, 0),
             (0, 0, 255),
             (255, 255, 255)]
    
    for i in range(0, len(kp)):
#        print(((kp[i].octave>>8) & 0xFF))
        aux = (kp[i].octave) & 0xFF
        
        if aux>=128:
            aux |= -128
 
        center = (np.int(kp[i].pt[0]), np.int(kp[i].pt[1]))
        rad = np.int(kp[i].size)
        
        cv2.circle(img, center, rad, color[aux], 0)
       
        kp_octave.append(aux)

#    Octave
    unique, counts = np.unique(kp_octave, return_counts=True)
    
    for i, num in zip(unique, counts):    
        print("Octave {}, key points: {}".format(i, num))


    mostrar("SURF Points Octave", img)

    print()
    
    
    
    cv2.imshow("SURF Points", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
        
        
    
def ej2():
    
    print("Ejercicio 2 - Apartado a")
    
    img1 = cv2.imread("imagenes/yosemite1.jpg") 
    img2 = cv2.imread("imagenes/yosemite2.jpg") 
    
    print("SIFT detector with ContrastThreshold: 0.06, edgeTreshold: 5")
    print()
    print("BF + CrossCheck")
    
    # Initiate SIFT detector
    sift = cv2.xfeatures2d.SIFT_create(contrastThreshold = 0.06, edgeThreshold = 5)
    
    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)
    
    
    # create BFMatcher object
    bf = cv2.BFMatcher_create(crossCheck=True)
    
    # Match descriptors.
    matches = bf.match(des1,des2)
    
    # Sort them in the order of their distance.
#    matches = sorted(matches, key = lambda x:x.distance)
    
    # Random de todos los elementos
    np.random.shuffle(matches)
    
    # Draw 100 random matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:100],None, flags=2)
    
    cv2.imshow("BF + Cross Check", img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#    plt.imshow(img3),plt.show()
    
    
#    Lowe Average

    print("Lowe Average, knn with k = 2")

    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)
    
    # Match descriptors.
    matches = flann.match(des1,des2)
    
    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)
    
    np.random.shuffle(matches)
    
    # Draw 100 random matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:100],None, flags=2)
    
    cv2.imshow("FLANN knn, k=2", img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#-----------------------------------------------------------------------------


def panorama_2(img1, img2, mostrar):
    sift = cv2.xfeatures2d.SIFT_create(contrastThreshold = 0.06, edgeThreshold = 5)

#    img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
#    img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    
#    img = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

#    sift = cv2.xfeatures2d.SIFT_create()
    
    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)
        
    # create BFMatcher object
    bf = cv2.BFMatcher_create(crossCheck=True)
    
    # Match descriptors.
    matches = bf.match(des1,des2)
    
    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)
        
    dst_p = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1,1,2)
    src_p = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1,1,2)
        
    M, mask = cv2.findHomography(src_p, dst_p, cv2.RANSAC, 1)
        
    # Juntar imágenes con homografía
    result = cv2.warpPerspective(src=img2, M=M, dsize=(img1.shape[1] + img2.shape[1], img2.shape[0]), borderMode=cv2.BORDER_TRANSPARENT)
    
    # Copiar imagen izquierda
    result[0:img1.shape[0], 0:img1.shape[1]] = img1

    #Borrar parte negra
    
    x = cv2.cvtColor(result,cv2.COLOR_BGR2GRAY)
    
    #Buscamos negros
    ind = np.where((x==0)[1])
    a = list(ind[0])

#    print(a)
            
    if len(a)!=0:
    # Nos quedamos con la imagen desde el 0 hasta el indice del primer negro
        result = result[:, :a[0]]
#        result = np.delete(result, a, 1)
      
    
#    mostrar("Panorama 2", result)
#        
#    cv2.imshow("Panorama 2", result)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()

    return result


def panorama_n(imgs):
    if len(imgs)==2:
        return panorama_2(imgs[0], imgs[1], False)
    
    elif len(imgs)==3:
        izq = panorama_2(imgs[0], imgs[1], False)

        der = panorama_2(imgs[1], imgs[2], False)
    
        return panorama_2(izq, der, False)
    
    else:    
        centro = np.int(math.floor(len(imgs)/2))
        
#        print("Centro: ", centro)
        
        izq = panorama_n(imgs[:centro])
                
        der = panorama_n(imgs[centro:])
        
        return panorama_2(izq, der, False)
    
#-----------------------------------------------------------------------------    

def ej3():
    
    print("Panorama N=3 imágenes yosemite")
    
    imagenes = []
    
    for i in range(1,4):
        img = cv2.imread("imagenes/yosemite"+str(i)+".jpg", 1)
        img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
        
        imagenes.append(img)
    
    img = panorama_n(imagenes)
            
    cv2.imshow("Panorama N", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()       
    
    print()
    
    
def ej4():

    print("Panorama N imágenes con mosaico")
    
    img1 = cv2.imread('imagenes/mosaico002.jpg', 1)
    img2 = cv2.imread('imagenes/mosaico003.jpg', 1)
    img3 = cv2.imread('imagenes/mosaico004.jpg', 1)
    img4 = cv2.imread('imagenes/mosaico005.jpg', 1)
    img5 = cv2.imread('imagenes/mosaico006.jpg', 1)
    img6 = cv2.imread('imagenes/mosaico007.jpg', 1)
    img7 = cv2.imread('imagenes/mosaico008.jpg', 1)
    img8 = cv2.imread('imagenes/mosaico009.jpg', 1)
    img9 = cv2.imread('imagenes/mosaico010.jpg', 1)
    img10 = cv2.imread('imagenes/mosaico011.jpg', 1)
        
    img = panorama_n([img1,img2,img3,img4,img5,img6,img7,img8,img9,img10])
#    img = panorama_n([img1,img2,img3,img4,img5])

    
    cv2.imshow("Panorama N", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
      
    print()
    
    
    
ej1a1()
input("Press Enter to continue...\n\n")
ej1a2()
input("Press Enter to continue...\n\n")
ej1b1()
input("Press Enter to continue...\n\n")
ej1b2()

input("Press Enter to continue...\n\n")
ej2()

input("Press Enter to continue...\n\n")
ej3()

input("Press Enter to continue...\n\n")
ej4()

    