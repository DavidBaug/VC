# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 17:48:53 2018

@author: david
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


def a():

    
    img = read_image("e.png", 0)

    img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)


    current = img.copy()


    print()
    print("Level = 0")
    print_image("Original image", current)
        
    laplacian = []
    
    for i in range(1,5):
        
        print("Level = ", i)
            
        pd = cv2.pyrDown(current)
            
        pu = cv2.pyrUp(pd, dstsize=(current.shape[1],current.shape[0]))
            
            # Restamos en cada iteración la nueva imagen que hemos obtenido tras
            # hacer pyrDown y pyrUp
            
        aux = current - pu
            
#        print_image("Laplacian Pyramid lvl {}".format(i), aux)

        laplacian.append(aux)
            
        current = pu
        
    final = current
    
    for i in range(1,5):
        
        final = final + laplacian[-i]
        
        
    print_image("final", final)

    print_image("original", img)
        
    
    aux = final/img
    
    print_image("Compro", aux)
        
        
a()