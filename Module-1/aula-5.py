# Aula 5
# Arrays

# imports
import array as arr

notas = arr.array('f', [10.4, 4.5])
notas.append(5.3)
# notas.remove(4.5)

print(notas)
print(round(notas[0],2))