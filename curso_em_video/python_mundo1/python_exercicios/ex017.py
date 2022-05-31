from math import hypot
cateto_oposto = float(input("Digite o valor do cateto oposto: "))
cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))
print(f"O valor da hipotenusa desse triângulo retângulo é {hypot(cateto_adjacente, cateto_oposto):.2f}")
