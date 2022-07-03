valor_mercadoria = float(input("Insira o valor da mercadoria: "))
percentual_desconto = float(input("Insira o percentual de desconto: "))
valor_desconto = valor_mercadoria - (valor_mercadoria * percentual_desconto / 100)
print(f"O valor do desconto é de R${valor_desconto:.2f} e o valor total a pagar é de R${valor_mercadoria + valor_desconto}")
