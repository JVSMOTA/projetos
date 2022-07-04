distancia = float(input("Digite a distância a percorrer (em km): "))

if distancia <= 200:
    preco_passagem = distancia * 0.50
else: 
    preco_passagem = distancia * 0.45

print(f"O preço da passagem é de R${preco_passagem:.2f}")
