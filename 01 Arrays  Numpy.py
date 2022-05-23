## Numpy, uma abreviação de Numerical Python. 
## Este é um dos pacotes mais importantes para processamento numérico no Python
## Além de ser a base para a maioria dos pacotes científicos que utilizam dados numéricos.
## No notebook deixamos inclusive um texto explicativo que introduz a esse pacote.

from time import time
import numpy as np ## importa a lib numpy inteira
import time


np.arange(10) ## numpy = np

print(np.arange(10))

# from numpy import arange ## importa só o arange da lib numpy, logo não precisa escrever numpy.arange()

# arange(10)

# print(arange(10))

# km = np.array([1000, 2300, 4987, 1500])

# print(km)

# type(km) # numpy.ndarray


km = np.loadtxt(fname = 'Numpy/carros-km.txt' , dtype =  int)

print(km)

##

dados = [ 
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital', 'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS', 'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
]

acessorios = np.array(dados)

print(acessorios)

km.shape ## mostrar linhas

np_array = np.arange(1000000)

py_list = list(range(1000000))

# %time for _ in range(100): np_array *= 2

# %time for _ in range(100): py_list = [x * 2 for x in py_list]
