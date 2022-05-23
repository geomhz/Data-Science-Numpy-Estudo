import numpy as np

# dados = np.array([[44410.,  5712., 37123.,     0., 25757.], 
#     [ 2003.,  1991.,  1990.,  2019.,  2006.]])

# print(dados)

# print(dados.shape) ## linhas 2, colunas 5

# print(dados.ndim) ## quantas dimensões temos (2 chaves)

# print(dados.size) ## retorna o número de elementos linhas + colunas

# print(dados.dtype) ## tipo de elementos dentro do array (pode ter float, str, int)

# print(dados.T) ## transforma linha para coluna
#     # indice 1 linha 1 com indice 1 linha 2

# print(dados.tolist()) ## retorna o array como uma lista

# ## reshape retorna um array que contém os mesmos dados com uma nova forma
# ## dados.reshape
# ## nomedoarray.reshape

# contador = np.arange(10)
# print(contador)

# print(contador.reshape((5, 2))) ## Refazer contador para ter 5 linhas e 2 colunas

# print(contador.reshape((5, 2), order='C')) ##usa a indexação da linguagem C

# print(contador.reshape((5, 2), order='F')) ## usa a indexação da linguagem Fortran

# km = [44410., 5712., 37123., 0., 25757.]
# anos = [2003, 1991, 1990, 2019, 2006]

# info_carros = km + anos

# print(np.array(info_carros).reshape(2, 5)) 

# print(np.array(info_carros).reshape((5 ,2) , order ='f')) ## Separa 5 linhas e 2 colunas ( km  +  ano )

## resize

dados = np.array([[44410.,  5712., 37123.,     0., 25757.], 
    [ 2003.,  1991.,  1990.,  2019.,  2006.]])

dados_new = dados.copy()

print(dados_new)

print(dados_new.resize((3, 5), refcheck=False)) ## fazer os dados_new com 3 linhas e 5 colunas

print(dados_new)

dados_new[2] = dados_new[0] / (2019 - dados_new[1])

print(dados_new)