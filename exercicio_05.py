x = input("Insira a primeira nota do aluno: ")
y = input("Insira a segunda nota do aluno: ")
print(f"As notas inseridas foram {x} e {y}")

m = (int(x) + int(y))/2

print(f"A média das duas notas do aluno é {m}")

if m == 10:
    print("Aluno aprovado com distinção.")
elif m>=7:
    print("Aluno aprovado.")
else:
    print("Aluno reprovado.")