texto = 'Python' # tupla('P', 'y', 't', 'h', 'o', 'n')

# imprimir letra da string com índice
print(texto[3])

# imprimir a última letra com índice
print(texto[-1])

# erro ao tentar atribuir um valor à tupla
#texto[3] = 't'

# é imutável, mas posso trocar o valor inteiro
texto = 'Pythonia'
print(texto)

# .find - retorna o índice do texto desejado
# obs.: retorna -1 caso não encontre o texto
print(texto.find('n')) #5
print(texto.find('f')) #-1

# .index - retorna o índice do texto desejado
# obs.: retorna ValueError caso não encontre o texto
print(texto.index('n')) #5
@@ -45,4 +45,18 @@
subtexto = frase[9:15]
print(frase)

print(f'O texto {subtexto} está entre os índices 9 e 15')
print(f'O texto {subtexto} está entre os índices 9 e 15')

# texto = "BR-SP-2024-0042"
# print(texto[-4:])

valor = 1250.5
print(f"R$ {valor:.2f}".replace(".", ","))
print(f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

valor = 0.857
print(f"{valor:.2%}".replace(".", ","))

texto = "BR-ABC-SP-2024-0042"
inicio = texto.find('SP')
print(texto[inicio:inicio+7])