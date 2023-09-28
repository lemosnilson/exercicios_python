print("*** A FABULOSA MÁQUINA DE FAZER PA COM LISTAS ***")

m = []  # Lista vazia para armazenar os valores

q = int(input("Quantos valores você deseja inserir? "))

for i in range(q):
    elementos = int(input("Insira um valor: "))
    m.append(elementos)

print("A lista inserida é:", m)

x = [] # Lista vazia para armazenar os novos valores

for i in range(q):
    somas = sum(m[:i+1])
    x.append(somas)

print("A lista somada é: ",x)
