import statistics


print("*** O FABULOSO CALCULADOR DE DISPERSÃO ***")

def inteiro (lista): # Converte a lista de entrada - string - para inteiros
    m = [int(x) for x in lista]
    return m

a = (input('Insira os valores sem vírgulas, apenas espaços: ').split())

m = inteiro(a)

print(f'A lista inserida foi {m}')

devpad = statistics.stdev(m)

print(f'O desvio padrão da lista inserida é {float(devpad)}.')


