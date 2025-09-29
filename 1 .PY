"""
1) Dado un vector de 10 posiciones cargado con números enteros,
se pide reemplazar todos los valores impares por el número 0.
● El programa debe recorrer el vector posición por posición.
● Cuando detecte un valor impar, deberá cambiarlo por 0.
● Al finalizar, mostrar el vector resultante.
Ejemplo:
● Vector original: [2, 1, 2, 3, 4, 11, 3, 2, 5, 9]
● Vector resultante: [2, 0, 2, 0, 4, 0, 0, 2, 0, 0]
""" 
import array as arr
mi_arreglo=arr.array('i',[2, 1, 2, 3, 4, 11, 3, 2, 5, 9])
for i in range (len(mi_arreglo)):
    if mi_arreglo[i]%2!=0:
        mi_arreglo[i]=0
  
        
print(mi_arreglo)
        