salario = float(input("Digite o salário do funcionário: "))

if salario > 1250:
    salario = salario + (salario * 0.15)
if salario <= 1250:
    salario = salario + (salario * 0.15)

print(f"O valor do novo salário é de R${salario:.2f}")
