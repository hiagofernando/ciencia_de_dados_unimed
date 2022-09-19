texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
        
        
print()  # adiciona uma quebra de linha

#Exemplo com range
for numero in range(0, 51, 5):
    print(nuemro, end=' ')
