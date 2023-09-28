a = str(input("Insira a palavra ou frase: "))

print(f"A palavra ou frase inserida foi '{a}'.")

a = a.upper()

print(f"A palavra ou frase escrita toda em maiúsculas é '{a}'.")

b = int(a.count('A'))
c = int(a.count('E'))
d = int(a.count('I'))
e = int(a.count('O'))
f = int(a.count('U'))

print(f"Existem {b+c+d+e+f} vogais na palavra ou frase inserida.")
print(f"Existem {b} letras A, {c} letras E, {d} letras I, {e} letras O e {f} letras U.")

g = int(a.count(" "))

if g ==0:
    print("Não é uma frase. É apenas uma palavra.")
else:
    print("Não é apenas uma palavra. É uma frase.")