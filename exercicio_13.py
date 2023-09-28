print('*** A FABULOSA MAQUINA DE MONTAR TABUADA ***')

i = int(input('Digite um número inteiro entre 1 e 10: '))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 0
b = a[n]

while i > 10 or i < 1:
    i = int(input("O número digitado não está entre 1 e 10. Por favor, digite um número entre 1 e 10: "))

while n < len(a):
    print(f'{i} x {a[n]} = {i * a[n]}')
    n += 1

