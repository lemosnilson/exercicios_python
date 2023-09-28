a = int(input('Por favor, insira uma nota entre 0 e 10: '))

b = list(range(0,11,1))

while a not in b:
    a = int(input('A nota que você digitou não está entre 0 e 10. Por favor, digite uma nota entre 0 e 10. '))
else:
    print(f'Você inseriu a nota {a}.')
