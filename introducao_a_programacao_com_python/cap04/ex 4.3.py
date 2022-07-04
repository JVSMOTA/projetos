numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))
numero3 = float(input("Digite outro número: "))

if numero1 >= numero2:
    if numero1 >= numero3:
        maior = numero1
    if numero3 >= numero1:
        maior = numero3

if numero2 >= numero1:
    if numero2 >= numero3:
        maior = numero2
    if numero3 >= numero2:
        maior = numero3

if numero1 <= numero2:
    if numero1 <= numero3:
        menor = numero1
    if numero3 <= numero1:
        menor = numero3

if numero2 <= numero1:
    if numero2 <= numero3:
        menor = numero2
    if numero3 <= numero2:
        menor = numero3

print(f"O maior número é {maior} e o menor é {menor}")
