# lab2 CNYT - Laboratorio 2 sobre operaciones en matrices complejas
### Descripcion
#
#### Este programa crea una libreria que implementa operaciones algebraicas sobre vectores y matrizes para numeros complejos C de la forma (parte real,parte imaginaria), vectores de la forma [[C1,C2,........,Cn]] y matrices de la forma [[C1-1,C1-2,...C1-n],[C2-1,C2-2,........,C2-n],........[Cn-1,Cn-2,....,Cn-n] y las siguientes funciones:

- Adición de vectores complejos.
- Inversa de vectores complejos.
- Multiplicación escalar de vectores complejos.
- Adición de matrices complejos.
- Inversa de matrices complejos.
- Multiplicación escalar de matrices complejas.
- Matriz transpuesta
- Matriz conjugada
- Matriz adjunta
- Función para calcular la "acción" de una matriz sobre un vector.
- Norma de matrices
- Distancia entrematrices
- Revisar si es unitaria
- Revisar si es Hermitian
- Producto tensor.

### Suma Matrices
#
#### recibe dos matrices con una parte real y una imaginaria, y retorna la matriz resultado de la suma
#### EJEMPLO:
~~~~
 matriz1=[[[3,2],[4,-2]],[[1,2],[3,2]]]
 matriz2=[[[5,-6],[7,2]],[[2,5],[-12,-9]]]
 sumaMatrices(matriz1,matriz2)
 ~~~~
#
### NegativaMatriz
#
#### recibe una matriz con una parte real y una imaginaria, y retorna la matriz negativa
#### EJEMPLO:
~~~~
negativaMatriz([[[5,-6],[7,2]],[[2,5],[-12,-9]]])
~~~~
#
### ComplejoPorMatriz
#
#### recibe una matriz con una parte real y una imaginaria, y retorna la matriz negativa
#### EJEMPLO:
~~~~
complejoPorMatriz((3,1),[[(1,0),(1,0),(1,0)]])
~~~~
#
### Transpuesta
#
#### recibe una matriz con una parte real y una compleja y retorna la transpuesta de la matriz entrante
#### EJEMPLO:
~~~~
transpuesta([[(3,2),(4,2)],[(5,1),(6,3)]])
~~~~
#
### Conjugada
#
#### recibe una matriz con una parte real y una imaginaria, y retorna la matriz Conjugada
#### EJEMPLO:
~~~~
conjugada([[(3,2),(4,2)],[(5,1),(6,3)]])
~~~~
#
### Adjunta
#
#### recibe una matriz con una parte real y una imaginaria, y retorna la matriz Adjunta
#### EJEMPLO:
~~~~
adjunta([[(3,2),(4,2)],[(5,1),(6,3)]])
~~~~
#
### Accion
#
#### recibe dos matrices con una parte real y una imaginaria, y retorna la  accion de una matriz sobre otra matriz (Si se quiere sacar la accion de matriz sobre vector sepuede ingresar matriz de un solo vector)
#### EJEMPLO:
~~~~
m1=[[(3,0),(1,2),(0,-1)],[(2,-1),(0,0),(1,0)],[(0,0),(4,3),(0,1)]]
m2=[[(1,0)],[(1,-2)],[(0,-1)]]
multiplicacionDeMatrices(m1,m2)
~~~~
#
### Norma
#
#### Recibe una matriz con una parte real y una imaginaria, y retorna la Norma de la matriz como un flotante
#### EJEMPLO:
~~~~
Norma([[(2.8,5.8),(3.4,-8.4)]])
~~~~
#
### Distancia
#
#### Recibe dos matrices con una parte real y una imaginaria, y retorna la distancia entre las matrizes como un flotante
#### EJEMPLO:
~~~~
  distancia([[(2.8,5.8),(3.4,-8.4)]],[[(2.8,5.8),(3.4,-8.4)]])
~~~~
#
### Unitario
#
#### Recibe una matriz con una parte real y una imaginaria, y retorna un Booleano (True/False) dependiendo de si es unitaria
#### EJEMPLO:
~~~~
Unitario([[(1,0),(0,0),(0,0)],[(0,0),(0,0),(1,0)],[(0,0),(1,0),(0,0)]])
~~~~
#
### Hermitian
#
#### Recibe una matriz con una parte real y una imaginaria, y retorna un Booleano (True/False) dependiendo de si es Hermitian
#### EJEMPLO:
~~~~
Hermitian([[(5,0),(4,5),(6,-16)],[(4,-5),(13,0),(7,0)],[(6,16),(7,0),(-2.1,0)]])
~~~~
#
### ProductoTensor
#
#### Recibe dos matrices con una parte real y una imaginaria, y retorna el punto Tensor que es una nueva Matriz
#### EJEMPLO:
~~~~
m=[[(1,0),(2,0)],[(3,0),(4,0)]]
m1=[[(1,0),(2,0),(3,0)],[(1,0),(2,0),(3,0)],[(1,0),(2,0),(3,0)]]
ProductoTensor(m,m1)
~~~~
# Pruebas
#### Al compilar el archivo automaticamente se ejecutan 15 pruebas que verifican todas las operaciones especificadas anteriormente.
#### para ejecutar el archivo matrices.py sigua las siguientes intrucciones:

1. Descargue el repositorio
~~~~
git clone https://github.com/ItaloNovoa/lab2-CNYT.git
~~~~
2. Ingrese al cmd/Terminal o simbolo del sistema
3. Ingresar a la carpeta de archivo 
4. digitar (Windows):
~~~~
python  matrices.py 
~~~~ 
4.digitar (Ubuntu, Mac)
~~~~
python3 matrices.py 
~~~~
