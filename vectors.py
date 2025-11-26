#arrays com numpy:
#Possuindo diversas dimensões, desde a 1D à 3D, ou maior(pouco utilizados).
#Eles agrupam um conjunto de dados dentro de uma matriz.
import numpy as np

array_number_one = np.array([1,2,1,2,4]) #dimensão igual a 1, tal que apresenta linha = 1
print(array_number_one)
print("-----------------separate-----------------")

array_dim_2 = np.array([[1,1,4],
                        [9,9,3]]) #dimensão igual a 2, apresenta números de linhas > 1
print(array_dim_2)
print("-----------------separate-----------------")

array_dim_3 = np.array([
                        #primeira camada
                        [
                        [1,1,3],
                        [1,7,8], #apresenta 3 linhas e 3 colunas, matriz 3x3
                        [9,0,0]  #Podemos também dizer que ela tem 3 de altura(linhas), e 3 de largura(colunas).
                        ],
                        #segunda camda
                        [
                        [2,4,3],
                         [1,5,5], #também apresenta 3 linhas e 3 colunas, matriz 3x3
                         [9,1,2]
                         ]
                        ])

                #Ela apresenta 2 camadas, sendo uma matriz que tem 2 camadas(pode ser também profundidade), 3 linhas e 3 colunas, matriz 2x3x3
print(array_dim_3)
print("-----------------separate-----------------")

zero_dim1 = np.zeros(4) #array com uma dimensão
print(zero_dim1)
print("-----------------separate-----------------")     

zero_dim2 = np.zeros((2,2)) #array com duas dimensões
print(zero_dim2)
print("-----------------separate-----------------")

zero_dim3 = np.zeros((2,2,2)) #array com três dimensões
print(zero_dim3)
print("-----------------separate-----------------")

axis1 = np.array([1,2,3])
axis_column = np.array([[1],
                        [2],
                        [3]])
new_axis = axis1[:,np.newaxis] #transfoma em colunas
new_axis2 = axis_column[np.newaxis,:]
print(new_axis)
print(axis_column)
print("-----------------separate-----------------")