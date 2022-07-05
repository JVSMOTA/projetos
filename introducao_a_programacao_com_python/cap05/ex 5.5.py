#==============================================================================
# Author: João Mota < joao.mota@ccc.ufcg.edu.br >
# GitHub: https://github.com/JVSMOTA
# Computer Science undergraduate at UFCG
#==============================================================================

qtd = int(input("Digite o número para imprimir múltiplos de 3: "))
x = 0
contador_de_multiplos = 0
while contador_de_multiplos < qtd:
    if x % 3 == 0 and x!= 0:
        print(x)
        contador_de_multiplos += 1
    x += 1

