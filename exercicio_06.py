A = float(input("Insira o preço do produto A: "))
B = float(input("Insira o preço do produto B: "))
C = float(input("Insira o preço do produto C: "))
print(f"Os preços inseridos foram {A}, {B} e {C}.")

if A<B and A<C:
    print(f"O produto com o melhor preço é o A, que custa {A}.")
elif B<A and B<C:
    print(f"O produto com o melhor preço é o B, que custa {B}.")
else:
    print(f"O produto com o melhor preço é o C, que custa {C}.")