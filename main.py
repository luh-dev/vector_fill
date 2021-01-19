valor = int(input('digite um valor: '))

numeros_calculados = [valor]

i = 0

while i < 9:
#while True:
    dobro = numeros_calculados[i] * 2

    numeros_calculados.append(dobro)
    i = i + 1

print(numeros_calculados)