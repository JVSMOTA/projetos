#==============================================================================
# Author: João Mota < joao.mota@ccc.ufcg.edu.br >
# GitHub: https://github.com/JVSMOTA
# Computer Science undergraduate at UFCG
#==============================================================================

valor = int(input("Tabuada de: "))
inicio = int(input("Digite o início da tabuada: "))
fim = int(input("Digite o fim da tabuada: "))
while inicio <= fim:
    print(f"{valor} + {inicio} = {valor + inicio}")
    inicio += 1

