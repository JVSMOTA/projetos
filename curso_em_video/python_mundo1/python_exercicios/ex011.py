largura_parede = float(input("Digite a largura da parede (em metros): "))
altura_parede = float(input("Digite a altura da parede (em metros): "))
area_parede = altura_parede * largura_parede
print(f"A área a ser pintada é de {area_parede:.2f}m².")
print(f"Você precisará de {area_parede/2:.2f} litros de tinta para pintar essa parede.")
