a = str(input("Insira a data do seu nascimento no formato dd/mm/aaaa: "))

a = a.split('/')
dia, mes, ano = a



print(f"Você nasceu no dia {dia} de {mes} de {ano}.")