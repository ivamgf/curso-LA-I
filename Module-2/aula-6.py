# Aula 5
# If, Else, Elif

aluno = input("Digite o nome de um aluno:")
nota = input("Digite a nota:")
media = 6.0
minimo = 3.0

if (float(nota) >= media):
    print(f"A nota do aluno {aluno} é: {nota}")
    print("O aluno está Aprovado!")
elif (float(nota) >= minimo):
    print("O aluno está em Recuperação")
else:
    print("O aluno está Reprovado!")