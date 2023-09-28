print("*** O FABULOSO CALCULADOR DE MEDIANAS ***")

import statistics
def inteiro (lista): # Converte a lista de entrada - string - para inteiros
    m = [int(x) for x in lista]
    return m

a = (input('Insira os valores sem vírgulas, apenas espaços: ').split())

m = inteiro(a)

print(f'A lista inserida foi {m}')

mediana = statistics.median(m)

print(f'A mediana da lista inserida é {float(mediana)}.')

