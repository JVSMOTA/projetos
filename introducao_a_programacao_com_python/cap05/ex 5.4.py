#==============================================================================
# Author: João Mota < joao.mota@ccc.ufcg.edu.br >
# GitHub: https://github.com/JVSMOTA
# Computer Science undergraduate at UFCG
#==============================================================================

fim = int(input("Digite o último número a imprimir: "))
x = 0
while x <= fim:
    if x % 2 != 0:
        print(x)
    x += 1

