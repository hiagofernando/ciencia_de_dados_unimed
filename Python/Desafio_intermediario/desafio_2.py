while True:
    try:
      entrada = input("qual perna")
      if entrada == 'esquerda':
        print("I speak English!")

      elif entrada == 'direita':
       print("¡Yo hablo español!")
      elif entrada == 'nenhuma':
         print("Eu falo portugues!")
      elif entrada == 'ambas':
        print("Me derrubaram aqui!")
    except EOFError:
        break