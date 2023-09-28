#informar a área que será pintada

area = float(input("Qual o tamanho, em m², da área que será pintada? "))

#cálculo do número de galoes

print(f"Para os cálculos da quantidade de tinta necessária, será considerado o valor informado de {area} m².")

volume = round(area/3,1)
galoes = round(volume//18,1)
resto = round(volume%18,1)
ngal1 = int(galoes)
ngal2 = int(galoes + 1)
ngal3 = int(18-resto)

print(f"Serão necessários {volume} litros de tinta para pintar a área informada.")

if resto > 0:
    print(f"Você precisará de {ngal2} galões, e sobrará {ngal3} litros de tinta.")
else:
    print(f"Você precisará de exatos {ngal1} galões de tinta.")
