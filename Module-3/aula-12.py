# Aula 12
# Functions

# Declarations
alunos = []
notas = []
media = 6.0
minimo = 3.0

# Function Register
def cadastrarNotas():
    for i in range(5):
        aluno = input("Digite o nome do aluno: ")
        nota = float(input("Digite a nota do aluno: "))

        alunos.append(aluno)
        notas.append(nota)

# Function main
def main():

    cadastrarNotas()

    # Verificando situação de cada aluno
    for i in range(len(alunos)):
        aluno = alunos[i]
        nota = notas[i]

        print(f"\nA nota do aluno {aluno} é: {nota}")

        if nota >= media:
            print("O aluno está Aprovado!")
        elif nota >= minimo:
            print("O aluno está em Recuperação.")
        else:
            print("O aluno está Reprovado!")

    # Mostrando listas finais
    print("\nLista de alunos:", alunos)
    print("Lista de notas:", notas)

if __name__ == "__main__":
    main()
