print("*** A FABULOSA MÁQUINA DE FAZER COMBINAÇÕES ***")

m = []  # Lista vazia para armazenar os valores

q = int(input("Quantos valores você deseja inserir? "))

for i in range(q):
    elementos = int(input("Insira um valor: "))
    m.append(elementos)

print("A lista inserida é:", m)

# Combinação dos valores em pares
pares = []

for x in m:
    for y in m:
        par = (x, y)
        if x != y:
            pares.append(par)

print("As combinações dos valores em pares são:")
print(pares)
