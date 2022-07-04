valor_casa = float(input("Digite o valor da casa a comprar: "))
salario = float(input("Digite o seu salário: "))
qtd_anos = int(input("Digite a quantidade de anos desejado para pagar: "))

mensalidade = (valor_casa / qtd_anos) / 12

if valor_casa <= 0:
    print("ERRO: Valor de compra impossível")
elif mensalidade > (salario * 0.3):
    print(f"A mensalidade seria de R${mensalidade:.2f}")
    print(f"A mensalidade não pode ser maior que 30% do salário.")
else:
    print(f"Com o salário de R${salario:.2f} pode-se pagar R${mensalidade:.2f} de mensalidade em {qtd_anos} anos para ter sua casa própria!")
