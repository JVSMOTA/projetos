kWh_consumida = float(input("Digite a quantidade de kWh consumida: "))
instalacao = input("Escolha o tipo de Instalação:" +
                 "\nR - Residências" +
                 "\nI - Indústrias" +
                 "\nC - Comércios" +
                 "\nDigite aqui: ")

if instalacao == "R" or instalacao == "r":
    if kWh_consumida <= 500:
        valor = kWh_consumida * 0.40
    else:
        valor = kWh_consumida * 0.65

elif instalacao == "I" or instalacao == "i":
    if kWh_consumida <= 1000:
        valor = kWh_consumida * 0.55
    else:
        valor = kWh_consumida * 0.60

elif instalacao == "C" or instalacao == "c":
    if kWh_consumida <= 5000:
        valor = kWh_consumida * 0.55
    else:
        valor = kWh_consumida * 0.60
else:
    print("ERRO: O Tipo de instalação não está disponível!")

print(f"O valor a ser pago é de R${valor:.2f}")
