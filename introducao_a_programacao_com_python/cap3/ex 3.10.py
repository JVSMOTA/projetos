salario = float(input("Digite o salário: "))
porcentagem_aumento = float(input("Digite a porcentagem: "))
aumento = salario * (porcentagem_aumento/100)
print(f"O aumento foi de R${aumento:.2f}.\n" + 
f"O novo salário é de R${salario + aumento:.2f}!")
