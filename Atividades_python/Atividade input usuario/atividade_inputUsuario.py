def funcaoUsuarioCalcula():
  print("Escolha um numero para realizar uma operação!  \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n 0 - Sair")
  escolha = int(input())
  while escolha != 0:
    print("Digite o primeiro número: ")
    numero_1 = int(input())
    print("Digite o segundo número: ")
    numero_2 = int(input())
    result = 0
    if escolha == 1:
      result = numero_1 + numero_2

    elif escolha == 2:
      result = numero_1 - numero_2

    elif escolha == 3:
      result = numero_1 * numero_2

    elif escolha == 4:
      result = numero_1 / numero_2

    else:
      print("Digite uma operação válida! \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n 0 - Sair")
      escolha = int(input())
    
    return result 
    continue

funcaoUsuarioCalcula()