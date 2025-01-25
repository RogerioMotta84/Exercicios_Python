# Com base na lista criada no exercício 1, utilize list comprehension para gerar uma nova lista contendo apenas os números pares e armazene-a em uma variável.

lista = [numero for numero in range (101)]
novaLista=[]

for numero in lista:
    if numero%2==0:
        novaLista.append(numero)
print(novaLista)

