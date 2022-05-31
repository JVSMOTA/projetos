dias_alugados = int(input("Quantos dias alugados? "))
km_rodados = int(input("Quantos Km rodados? "))
print(f"O total a pagar é R${(dias_alugados * 60) + (km_rodados * 0.15):.2f}")
