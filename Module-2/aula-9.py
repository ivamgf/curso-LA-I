# Aula 9

# Declarations
alunos = []
notas = []
media = 6.0
minimo = 3.0

# Functions
for i in range(5):
    aluno = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))

    alunos.append(aluno)
    notas.append(nota)

    if (float(nota) >= media):
        print(f"A nota do aluno {aluno} é: {nota}")
        print("O aluno está Aprovado!")
    elif (float(nota) >= minimo):
        print("O aluno está em Recuperação")
    else:
        print("O aluno está Reprovado!")

print(alunos)
print(notas)