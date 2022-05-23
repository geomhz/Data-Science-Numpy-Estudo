## Seleções em lista com arrays numpy

import numpy as np

km = np.array([44410., 5712., 37123., 0., 25757.])  ## linha 1 (0)
anos = np.array([2003, 1991, 1990, 2019, 2006]) ## linha 2 (1)
dados = np.array([km, anos])

print(dados) ## puxa os dados e ano 

contador = np.arange(10) ## do 0 ao 9 pq a contagem começa do 0

print(contador)

item = 6 ## quero o item 6

index = item - 1 ## como começa do 0, então é o item que quero - 1

contador[index] ## puxa o número item 6 - 1 

print (contador[index])

print(contador[-1]) ## puxa o ultimo número do contador

print(dados[0]) ## imprime apenas linha 1 (km)
print(dados[1]) ## imprime apenas linha 2 (anos)

print(dados[1, 2]) ## imprime o dado da linha 2 (1), 2 (terceiro numero da linha 2)

## Fatiamento
## A sintaxe para realizar fatiamento em um array Numpy é i:j:k onde i é o índice inicial, j é o índice de parada, e k é o indicador de passo ( k≠0 )

contador = np.arange(10)

print(contador[1:4]) ## [1:4] chama o indice numero 01 até o 03

print(contador[1:8:2]) ## [1:8:2] Vai do indice 01 até o indice 07 pulando de 2 em 2 números

print(contador[::2]) ## [::2] pega todos os números pares

print(contador[1::2]) ## [1::2] pega todos os números impares

print(dados[:, 1:4]) ## [:, 1:4]) :, Seleciona todas as linhas e 1:4 seleciona o indice 1 até o 3 de todas as linhas

print(dados[:, 1:3][0]) ## seleciona o indice 1 até o 2 da linha 0 (primeira linha)

print(dados[:, 1:3][1]) ## seleciona o indice 1 até o 2 da linha 1 (segunda linha)

media = dados[:, 1:3][0] / (2019 - dados[:, 1:3][1]) 
        #indice 1:3 todas colunas, do indice 1 ao 3 linha 0 dividido pelo ano 2019 - indice 1:3 da linha 1

print(media)

print(contador > 5) ## contador com bool true e false (>5 true, <5 false)

print(contador[contador>5]) ## pega apenas numeros maiores que 5 dentro do contador

print(dados[1] > 2000) ## true para o dado 1 (ano do veiculo) maior que ano 2000 e false para mais velho que 2000

print(dados[:, dados[1]>2000])
        ##[: seleciona todas colunas existentes
        ##, dados[1]>2000 pega a linha anos >2000 na linha 1 (anos)