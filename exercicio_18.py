import statistics

print("*** O FABULOSO CALCULADOR DE QUARTIS ***")

def inteiro (lista): # Converte a lista de entrada - string - para inteiros
    m = [int(x) for x in lista]
    return m

a = (input('Insira os valores sem vírgulas, apenas espaços: ').split())

m = inteiro(a)

print(f'A lista inserida foi {m}')

quartis = statistics.quantiles(m, n=4, method='exclusive')

q1 = quartis[0]
q2 = quartis[1]
q3 = quartis[2]

print(f'O primeiro quartil Q1 da lista inserida é {float(q1)}.')
print(f'O segundo quartil Q2 da lista inserida é {float(q2)}.')
print(f'O terceiro quartil Q3 da lista inserida é {float(q3)}.')

