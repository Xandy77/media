# lista de numeros
numeros = [10, 5, 7, 4, 6, 3, 8]

# classifica em ordem decrescente
numeros.sort(reverse=True)

for numero in numeros:
    print(numero, end=' ')

media = sum(numeros)/len(numeros)

print(f'Resultado da média: {media:,.2f}.')


