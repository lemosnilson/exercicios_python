palavra = str(input('Insira qualquer palavra: '))

v = ['a','e','i','o','u']

for letra in palavra:
    if letra in v:
        print('vogal')
    else:
        print(letra)