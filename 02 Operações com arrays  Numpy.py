import numpy as np

## Operação com Arrays com 1 dimensão

km = np.array([44410., 5712., 37123., 0., 25757.])
anos = np.array([2003, 1991, 1990, 2019, 2006])

idade = 2019 - anos

print(idade)

km_media = km / idade
print(km_media)

## Operação com Arrays com 2 dimensões

dados = np.array([km, anos])

print(dados) ## puxa os dados e ano 

print(dados.shape) ## imprime quantas colunas e linhas tem

print(dados[0]) ## puxa a primeira linha (no caso km)

km_media1 = dados[0] / (2019 - dados[1])

print(km_media1)