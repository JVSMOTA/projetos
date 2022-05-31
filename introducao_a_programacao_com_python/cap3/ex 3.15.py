quantidade_cigarros = int(input("Quantidade de cigarros fumados por dia = "))
anos_fumando = int(input("Quantos anos fumando = "))
dias_perdidos = ((quantidade_cigarros * 10) * (anos_fumando * 365)) // 1440
print(f"Você perdeu {dias_perdidos} dias fumando.")
