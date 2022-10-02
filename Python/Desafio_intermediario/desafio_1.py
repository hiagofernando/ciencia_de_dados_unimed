letras = input('c')
num = 0
soma = 0

num = ord(letras)
for i in range(65,91):
 soma = soma + 1
 if i == num:
  print(soma)
  break