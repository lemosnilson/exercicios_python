a = str(input('Escreva um número decimal, com quantas casas decimais quiser: '))
print(f'O número inserido foi {a}.')

b = a.split('.')
c = b[1]

print(f'A parte decimal do número informado é {c}')

