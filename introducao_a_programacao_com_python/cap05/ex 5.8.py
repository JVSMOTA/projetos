#==============================================================================
# Author: João Mota < joao.mota@ccc.ufcg.edu.br >
# GitHub: https://github.com/JVSMOTA
# Computer Science undergraduate at UFCG
#==============================================================================

n1 = int(input("Digite o primeiro valor para multiplicar: "))
n2 = int(input("Digite o segundo valor para multiplicar: ")) 

r1 = 0
resultado1 = ""
while r1 < (n1 * n2):
    resultado1 += f"{n1}"
    if r1 + n1 < (n1 * n2):
        resultado1 += " + "
    r1 += n1 

r2 = 0
resultado2 = ""
while r2 < (n1 * n2):
    resultado2 += f"{n2}"
    if r2 + n2 < (n1 * n2):
        resultado2 += " + "
    r2 += n2

print(f"{n1 * n2} = {resultado1} = {resultado2}")
