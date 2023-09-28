a = []
n=1

while n<=5:
    a.append(input(f'insira o {n}° número: '))
    n += 1
else:
    print(f'os números digitados foram {a}')

b = sorted(a)
max = b[4]

print(f'A lista de números, em ordem crescente é {b}.')
print(f'Portanto, o maior número da lista é o quinto E último elemento da lista em ordem crescente, ou seja, número {max}.')
print("GOD! I'M ON FIRE")