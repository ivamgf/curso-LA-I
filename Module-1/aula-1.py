# Aula
# Variáveis e constantes

# Imports
import numpy as np

# Declarações
firstName = "João"
lastName = "Silva"
name = firstName + " " + lastName
valorHora = 45.36
valorHoraAprox = int(valorHora)
diasTrabalhados = 30
HORASTRABALHADAS = 8
HORASTRABALHADASAJUST = float(HORASTRABALHADAS)
vencimento = (HORASTRABALHADASAJUST * valorHora) * diasTrabalhados

dadosFuncionario = [firstName,lastName,vencimento]
dadosFuncionario = dadosFuncionario.append(diasTrabalhados)
valores = np.array([valorHora,HORASTRABALHADASAJUST])

print(valores)

funcionarios = {
    "num1": "Joao",
    "num2": "Pedro",
    "num3": "Paulo"
}

# Saídas

print(funcionarios)