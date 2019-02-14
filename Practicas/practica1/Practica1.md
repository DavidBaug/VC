# Prácica1: Filtrado y Muestreo

#### David Gil Bautista

#### 45925324M



### Ejercicio 1: Funciones OpenCV

USANDO LAS FUNCIONES DE OPENCV : escribir funciones que implementen los siguientes puntos:



##### a) El cálculo de la convolución de una imagen con una máscara Gaussiana 2D (Usar GaussianBlur). Mostrar ejemplos con distintos tamaños de máscara y valores de sigma. Valorar los resultados.


Para resolver este apartado debemos saber cómo funciona una máscara Gaussiana, y para ello mostraré el siguiente gráfico que nos ayudará a comprender mejor el concepto.



![Related image](https://homepages.inf.ed.ac.uk/rbf/HIPR2/figs/gauss2.gif)





Una máscara Gaussiana presenta un kernel que es una aproximación en dos dimensiones de una función Gaussiana.
$$
h(u,v) = \frac{1}{2\pi\sigma^2}e^{-\frac{u^2+v^2}{\sigma^2}}
$$
En nuestro caso el kernel nos permitirá escoger el tamaño de la máscara con el que trabajaremos, y para ello probaremos con los siguientes tamaños 1, 3, 5 y 7 píxeles.  Un tamaño de 5 píxeles quiere decir que trabajaremos con el pixel central y dos a su izquierda y derecha, es decir, siendo **x** el pixel central y **k** el tamaño de la máscara, trabajaremos con las siguientes posiciones:
$$
x\pm\frac{(k-1)}{2}+1
$$
La varianza, por definición es la desviación estandar al cuadrado. Esta desviación nos indica lo dispersos que están los elementos respecto de la media. Una función con una varianza alta hace que la función sea más plana y que los datos no estén tan cerca de la media. Sabiendo esto podemos decir que cuanto menor sea la varianza vamos a tener más ceros en el mismo kernel, por lo que estos datos serán menos relevantes.



![](D:\Mega\Dropbox\UGR\4\VC\Practicas\practica1\res\1a1.PNG)

![](D:\Mega\Dropbox\UGR\4\VC\Practicas\practica1\res\1a2.PNG)

![](D:\Mega\Dropbox\UGR\4\VC\Practicas\practica1\res\1a3.PNG)



Como podemos ver en las imágenes mostradas, conforme aumentamos el tamaño del kernel y la varianza vamos obteniendo un desenfoque mayor.



##### b) Usar getDerivKernels para obtener las máscaras 1D que permiten calcular al convolución 2D con máscaras de derivadas. Representar e interpretar dichas máscaras 1D para distintos valores de sigma.

Para este ejercicio usamos la función getDerivKernels para obtener las máscaras de derivadas que podemos usar para calcular la convolución en 2D. Para ello hemos probado con distintos tamaños de máscara y hemos escogido la derivada de las columnas para representar un filtro de alisamiento en el que todos los valores son positivos y suman 1.



![](D:\Mega\Dropbox\UGR\4\VC\Practicas\practica1\res\1b1.PNG)

![](D:\Mega\Dropbox\UGR\4\VC\Practicas\practica1\res\1b11.PNG)

Para un kernel de tamaño 1 obtenemos un dato de valor 1, al pasar el filtro por una imagen obtenemos otra imagen exactamente igual puesto que al evaluar el pixel central toma su mismo valor.





![](D:\Mega\Dropbox\UGR\4\VC\Practicas\practica1\res\1b2.PNG)

![](D:\Mega\Dropbox\UGR\4\VC\Practicas\practica1\res\1b22.PNG)

Cambiando el kernel a 3 podemos ver que el píxel central va a ser más relevante, aunque ya notamos un claro desenfoque en los píxeles vecinos.





![](D:\Mega\Dropbox\UGR\4\VC\Practicas\practica1\res\1b3.PNG)

![](D:\Mega\Dropbox\UGR\4\VC\Practicas\practica1\res\1b33.PNG)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

![](D:\Mega\Dropbox\UGR\4\VC\Practicas\practica1\res\1b4.PNG)

![](D:\Mega\Dropbox\UGR\4\VC\Practicas\practica1\res\1b44.PNG)



Conforme aumentamos el tamaño del kernel podemos ver que el área de desenfoque se distribuye más y que los píxeles centrales a la media son menos relevantes que con un tamaño de máscara menor. De esta forma podemos ver gráficamente lo que hemos realizado en el apartado anterior donde para una misma varianza el tamaño de la máscara es proporcional al desenfoque que obtenemos.



##### c) Usar la función Laplacian para el cálculo de la convolución 2D con una máscara de Laplaciana-de-Gaussiana de tamaño variable. Mostrar ejemplos de funcionamiento usando dos tipos de bordes y dos valores de sigma: 1 y 3

Para este ejercicio hemos usado la función Laplaciana para detectar los bordes de una imagen y también la derivada parcial de la imagen para ver qué método es más efectivo.

![](D:\Mega\Dropbox\UGR\4\VC\Practicas\practica1\res\1c1.PNG)

![](D:\Mega\Dropbox\UGR\4\VC\Practicas\practica1\res\1c2.PNG)

Para un tamaño de máscara de 3 píxeles podemos ver que la función Laplaciana con dos tipos distintos de bordes nos ofrece un resultado similar. El escoger un determinado tipo de bordes nos ayuda a conseguir un resultado más fiable en una imagen en la cual nos encontramos con detalles en los bordes y que podemos perder en caso de rellenar el borde con un color sólido, pero en este caso los resultados han sido idénticos.

Respecto a los bordes de los objetos encontrados, podemos apreciar que la función laplaciana nos da unos bordes más finos y con más detalle, mientras que la suma de las derivadas parciales reconoce bien los bordes pero nos da un resultado más tosco.

![](D:\Mega\Dropbox\UGR\4\VC\Practicas\practica1\res\1c3.PNG)

![](D:\Mega\Dropbox\UGR\4\VC\Practicas\practica1\res\1c4.PNG)



Al aumentar el tamaño del kernel podemos ver que la función laplaciana ha hecho más gordos los bordes que ya había encontrado con un tamaño de kernel menor y que muestra ciertos detalles que antes no se apreciaban, a pesar de mostrar un poco más de ruido.

Usando las derivadas parciales generamos mucho ruido en el objeto, debido a las luces y sombras, y en la propia escena. Al sumar las derivadas obtenemos una imagen con mucho ruido y rugosidad. Por lo que podemos determinar que la función Laplaciana nos ofrece mejores resultados.



### Ejercicio 2: Convolución y pirámides

Implementar apoyándose en las funciones getDerivKernels, getGaussianKernel, pyrUp(), pyrDown(), escribir funciones los siguientes:



##### a) El cálculo de la convolución 2D con una máscara separable de tamaño variable. Usar bordes reflejados. Mostrar resultados.

Para el desarrollo de este apartado he optado por usar *getGaussianKernel* para obtener una máscara separable de tamaño **k** y **sigma** fijo en 3.

Una vez usamos la función y obtenemos nuestro kernel calculamos la convolución como la multiplicación de la máscara por su traspuesta y la aplicamos usando la función *filter2D* con bordes constantes (bordes negros)

![](D:\Mega\Dropbox\UGR\4\VC\Practicas\practica1\res\2a1.PNG)

![](D:\Mega\Dropbox\UGR\4\VC\Practicas\practica1\res\2a2.PNG)

![](D:\Mega\Dropbox\UGR\4\VC\Practicas\practica1\res\2a3.PNG)

Como se puede comprobar en esta última imagen obtenemos dos matrices gaussianas en las que podemos apreciar que en la primera, con un tamaño del kernel de 3 pixeles, apenas hay diferencia entre los valores de la matriz, pero en la segunda, con un tamaño de 7 pixeles, se nota más la diferencia con los puntos que están más alejados de la media.



##### b) El cálculo de la convolución 2D con una máscara 2D de 1ª derivada de tamaño variable. Mostrar ejemplos de funcionamiento usando bordes a cero.

En este apartado usamos *getDerivKernels* para obtener una máscara de primera derivada con un tamaño variable de k. El uso de la primera derivada nos permite calcular los saltos que hay en las fronteras y realzarlos.

![](D:\Mega\Dropbox\UGR\4\VC\Practicas\practica1\res\2b3.PNG)

La primera derivada realza las partes de una imagen donde encontramos un contraste mayor, y esto suele darse en las fronteras donde la información los pixeles suele ser muy diferente.



![](D:\Mega\Dropbox\UGR\4\VC\Practicas\practica1\res\2b1.PNG)

![](D:\Mega\Dropbox\UGR\4\VC\Practicas\practica1\res\2b2.PNG)

Conforme aumentamos el tamaño de la máscara usamos más valores para operar con la derivada y en este caso hacemos que los saltos sean más grandes.





##### c) El cálculo de la convolución 2D con una máscara 2D de 2ª derivada de tamaño variable. 

En este apartado volvemos a usar *getDerivKernels* pero esta vez usando la segunda derivada para para crear una máscara con tamaño *k*.

En el apartado anterior hemos podido ver la forma que tiene la segunda derivada, dicha máscara realza un pixel central sobre los contiguos al mismo. De esta forma también conseguimos realzar las fronteras en una imagen.

![](D:\Mega\Dropbox\UGR\4\VC\Practicas\practica1\res\2c1.PNG)

![](D:\Mega\Dropbox\UGR\4\VC\Practicas\practica1\res\2c2.PNG)

Al igual que en el caso anterior conforme aumentamos el tamaño del kernel los saltos entre las fornteras son más pronunciados por lo que a pesar de representar aquellas fronteras más relevantes perdemos detalle en las que son menos apreciables.



##### d) Una función que genere una representación en pirámide Gaussiana de 4 niveles de una imagen. Mostrar ejemplos de funcionamiento usando bordes.

Con una piramide Gaussiana representamos cómo se vería una imagen al hacerla más pequeña y después volver a escalarla al tamaño anterior. Haciendo esto podemos ver que en cada nivel la imagen tiene menos calidad debido que al hacer más pequeña la imagen estamos perdiendo información ya que no vamos a poder ver todos los píxeles que teníamos antes, y al volver a escalarla interpolamos menos información a un tamaño mayor, por lo que podemos ver gráficamente cómo va empeorando con el paso de los niveles.

Se ha realizado con dos tipos de bordes, el borde por defecto que tiene OpenCV y el borde reflejado que replica la información de las fronteras de la imagen. El resultado es similar para ambos bordes.



![](D:\Mega\Dropbox\UGR\4\VC\Practicas\practica1\res\2d1.PNG)

![](D:\Mega\Dropbox\UGR\4\VC\Practicas\practica1\res\2d2.PNG)



##### e) Una función que genere una representación en pirámide Laplaciana de 4 niveles de una imagen. Mostrar ejemplos de funcionamiento usando bordes.

En este caso hacemos una piramide similar a la del ejercicio anterior en la que lo primero que debemos hacer es escalar la imagen original a una más pequeña y volverla a escalar al tamaño original. Una vez hecho esto tenemos la misma imagen que en el apartado anterior, una imagen con menos calidad y más difuminada. Con dicha imagen la restamos a la imagen original y de esta forma conseguimos eliminar las bajas frecuencias y hallar los bordes. Mientras iteramos sobre las imágenes modificadas vamos eliminando cada vez más información y al final encontramos una imagen con las fronteras más relevantes.

Para esta representación también se han usado dos bordes, el que nos ofrece por defecto OpenCV y el borde reflejado. Al igual que en el apartado anterior la diferencia apenas es apreciable.

![](D:\Mega\Dropbox\UGR\4\VC\Practicas\practica1\res\2e1.PNG)

![](D:\Mega\Dropbox\UGR\4\VC\Practicas\practica1\res\2e2.PNG)



### Ejercicio 3: Imágenes Híbridas

Mezclando adecuadamente una parte de las frecuencias altas de una imagen con una parte de las frecuencias bajas de otra imagen, obtenemos una imagen híbrida que admite distintas interpretaciones a distintas distancias ( ver hybrid images project page). 

Para seleccionar la parte de frecuencias altas y bajas que nos quedamos de cada una de las imágenes usaremos el parámetro sigma del núcleo/máscara de alisamiento gaussiano que usaremos. A mayor valor de sigma mayor eliminación de altas frecuencias en la imagen convolucionada. Para una buena implementación elegir dicho valor de forma separada para cada una de las dos imágenes ( ver las recomendaciones dadas en el paper de Oliva et al.). 

Recordar que lasmáscaras 1D siempre deben tener de longitud un número impar. Implementar una función que genere las imágenes de baja y alta frecuencia a partir de las parejas de imágenes ( solo en la versión de imágenes de gris) . El valor de sigma más adecuado para cada pareja
habrá que encontrarlo por experimentación.



##### a) Escribir una función que muestre las tres imágenes ( alta, baja e híbrida) en una misma ventana. (Recordar que las imágenes después de una convolución contienen número flotantes que pueden ser positivos y negativos)



##### b) Realizar la composición con al menos 3 de las parejas de imágenes

#### 