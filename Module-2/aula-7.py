# Aula 7
# For

alunos = []
notas = []

for i in range(0,6):
    aluno = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))

    alunos.append(aluno)
    notas.append(nota)

print(alunos)
print(notas)