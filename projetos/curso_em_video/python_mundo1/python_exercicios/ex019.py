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
escolhido = random.randrange(0,3)
print(f"O aluno escolhido para apagar o quadro é {lista_alunos[escolhido]}.")
