import random
lista_alunos = []
nome_aluno = input("Digite o nome do primero aluno: ")
lista_alunos.append(nome_aluno)
nome_aluno = input("Digite o nome do segundo aluno: ")
lista_alunos.append(nome_aluno)
nome_aluno = input("Digite o nome do terceiro aluno: ")
lista_alunos.append(nome_aluno)
nome_aluno = input("Digite o nome do quarto aluno: ")
lista_alunos.append(nome_aluno)
escolhido = random.randrange(0, len(lista_alunos) - 1)
print("A ordem para apresentação será: ")
print(f"1° {lista_alunos[escolhido]}")
lista_alunos.pop(escolhido)
escolhido = random.randrange(0, len(lista_alunos) - 1)
print(f"2° {lista_alunos[escolhido]}")
lista_alunos.pop(escolhido)
escolhido = random.randrange(0, len(lista_alunos) - 1)
print(f"3° {lista_alunos[escolhido]}")
lista_alunos.pop(escolhido)
print(f"4° {lista_alunos[0]}")

