velocidade_carro = float(input("Velocidade do carro: "))

if velocidade_carro > 80:
    multa = (velocidade_carro - 80) * 5
    print(f"Você foi multado por excesso de velocidade!")
    print(f"O valor da multa é de R${multa:.2f}")

