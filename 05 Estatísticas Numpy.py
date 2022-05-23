from matplotlib.pyplot import axis
import numpy as np

anos = np.loadtxt(fname = "Numpy/carros-anos.txt", dtype = int)
km = np.loadtxt(fname = "Numpy/carros-km.txt")
valor = np.loadtxt(fname = "Numpy/carros-valor.txt")

## column_stack() transforma arrays unidimensionais em colunas de um array bidimensional

dataset = np.column_stack((anos, km, valor))
 # nome =   column_stack ((tupla))

print(dataset)

# A primeira estatística que calcularemos usando esse dataset é a media, que conseguiremos usando o método np.mean().

print(np.mean(dataset)) ## os 3 itens tudo somado 

print(np.mean(dataset, axis=0)) ## pega a média de cada valor ano km e valor

np.mean(dataset[:, 0]) ## pega a média do ano *linha 0

np.mean(dataset[:, 1]) ## pega a média da kilometragem *linha 1

np.mean(dataset[:, 2]) ## pega a média do valor dos veiculos *linha 2

np.std(dataset[:, 2]) ## retorna o desvio padrão da linha 2

dataset.sum(axis=0) ## retorna soma dos elementos do arrays do eixo especificado

dataset[:, 1].sum() ## retorna a soma da linha 1

np.sum(dataset, axis=0)