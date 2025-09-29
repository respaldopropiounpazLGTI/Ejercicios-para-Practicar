"""2) Dado un vector de 6 posiciones cargado con números enteros, se
debe realizar lo siguiente:
a) Calcular y mostrar la suma de todos los valores pares del
vector.
b) Calcular y mostrar la multiplicación de todos los valores
impares del vector.
Ejemplo:
● Vector original: [2, 5, 4, 7, 6, 3]
● Suma de los pares = 2 + 4 + 6 = 12
● Multiplicación de los impares = 5 * 7 * 3 = 105"""

import array as arr
import math
Vector_original=arr.array('i',[2, 5, 4, 7, 6, 3])
primero_descrimino_pares=[numero for numero in Vector_original if numero%2==0]
sumo=sum(primero_descrimino_pares)
print(f"la suma de los numeros pares es {sumo}")
saco_inpares=[numero for numero in Vector_original if numero%2!=0]
multiplico=math.prod(saco_inpares)
print(f" la multiplicacion es {multiplico}")


import array as arr
vector_original=arr.array('i',[2, 5, 4, 7, 6, 3])
suma=0
for i in range(len(vector_original)):
    if vector_original[i]%2==0:
        suma+=vector_original[i]
        
print(suma)        
multiplicacion=1
for i in range (len(vector_original)):
    if vector_original[i]%2!=0:
        multiplicacion*=vector_original[i]
        
        
print(multiplicacion)        
        
 

       
        
        



