# Aula 8
# For

alunos = []
notas = []

QuantNotas = [1,2,3,4]

for i in QuantNotas:
    aluno = input("Digite o nome do aluno:")
    nota = float(input("Digite a nota do aluno:"))

    alunos.append(aluno)
    notas.append(nota)

print(f"Aluno: {alunos}")
print(f"Nota: {notas}")