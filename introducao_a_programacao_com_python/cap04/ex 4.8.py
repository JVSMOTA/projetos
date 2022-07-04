numero1 = float(input("Primeiro Número: "))
numero2 = float(input("Segundo Número: "))

print(f"Qual operação deseja fazer entre {numero1} e {numero2}?")
print(f"1 - Soma")
print(f"2 - Subtração")
print(f"3 - Multiplicação")
print(f"4 - Divisão")

operacao = int(input("Digite aqui: "))

if operacao == 1:
    resultado = numero1 + numero2
elif operacao == 2:
    resultado = numero1 - numero2
elif operacao == 3:
    resultado = numero1 * numero2
elif operacao == 4:
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = 0
        print("Impossível divisão por Zero")
else:
    print("Operação Indisponível!")
print(f"Resultado = {resultado}")

