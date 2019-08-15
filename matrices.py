import math
import unittest

#ejemplo
#sumaMatrices([[[3,2],[4,-2]],[[1,2],[3,2]]],[[[5,-6],[7,2]],[[2,5],[-12,-9]]])
def sumaMatrices(m1,m2):
    matriz=[]
    for i in range(0,len(m1)):
        vector=[]
        for j in range(0,len(m1[0])):
            vector.append((m1[i][j][0]+m2[i][j][0],m1[i][j][1]+m2[i][j][1]))
        matriz.append(vector)
    return matriz



#ejemplo
#negativaMatriz([[[5,-6],[7,2]],[[2,5],[-12,-9]]])
def negativaMatriz(m1):
    matriz=[]
    for i in range(0,len(m1)):
        vector=[]
        for j in range(0,len(m1[0])):
            vector.append((m1[i][j][0]*-1,m1[i][j][1]*-1))
        matriz.append(vector)
    return matriz
    
def complejoPorMatriz(c1,m1):
    matriz=[]
    for i in range(0,len(m1)):
        vector=[]
        for j in range(0,len(m1[0])):
            vector.append(producto(m1[i][j],c1))
        matriz.append(vector)
    return matriz

def transpuesta(m1):
    matriz=[]
    for i in range(0,len(m1)):
        vector=[]
        for j in range(0,len(m1[0])):
            vector.append(m1[j][i])
        matriz.append(vector)
    return matriz

def conjugada(m1):
    matriz=[]
    for i in range(0,len(m1)):
        vector=[]
        for j in range(0,len(m1[0])):
            vector.append((m1[i][j][0],m1[i][j][1]*-1))
        matriz.append(vector)
    return matriz

def adjunta(m1):
    matriz=transpuesta(m1)
    matriz=conjugada(matriz)
    return matriz


class TestUM(unittest.TestCase):
    #suma
    def test_caso_sumaMatriz_1(self):
        self.assertEqual([[(8, -4), (11, 0)], [(3, 7), (-9, -7)]],sumaMatrices([[[3,2],[4,-2]],[[1,2],[3,2]]],[[[5,-6],[7,2]],[[2,5],[-12,-9]]]))
    #Negativa de Matriz   
    def test_caso_NegativaDeMatriz_1(self):
        self.assertEqual([[(-5, 6), (-7, -2)], [(-2, -5), (12, 9)]],negativaMatriz([[[5,-6],[7,2]],[[2,5],[-12,-9]]]))
    """def test_caso_producto_2(self):
        self.assertEqual((1,21),producto((1,4),(5,1)))"""
   
        

if __name__ =='__main__':
    unittest.main()
    
#recibe dos tuplas con una parte real y otra imaginaria
#EJEMPLO --> (3,-4),(-5,18)
def producto(c1,c2):
    pr=(c1[0]*c2[0])-(c1[1]*c2[1])
    pi=(c1[0]*c2[1])+(c2[0]*c1[1])
    return (pr,pi)
