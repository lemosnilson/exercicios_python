print("*** O FABULOSO FAZEDOR DE MÉDIA DE LISTAS ***")

def media (lista): # Calcula a média dos valores contidos em uma lista
   tamanho = len(lista)
   soma = sum(lista)
   media = soma / tamanho
   return media

def inteiro (lista): # Converte a lista de entrada - string - para inteiros
    m = [int(x) for x in lista]
    return m

a = (input('Insira os valores sem vírgulas, apenas espaços: ').split())

m = inteiro(a)
y = media(m)
print(y)

# print(media(inteiro(a))) --> Mas poderia ser assim. Funciona.
