km_rodados = float(input("Quantidade de KMs rodados = "))
dias_alugado = int(input("Quantidade de dias alugados = "))
valor_total = (km_rodados * 0.15) + (dias_alugado * 60)
print(f"O total a se pagar é de R${valor_total:.2f}!")
