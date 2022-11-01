def funcaoCalculadora(num_1, num_2, sinalOperacao):
  resultado = 0
  if sinalOperacao == "+" or sinalOperacao == 1:
    resultado = num_1 + num_2
  
  elif sinalOperacao == "-" or sinalOperacao == 2:
    resultado = num_1 - num_2

  elif sinalOperacao == "*" or sinalOperacao == 3:
    resultado = num_1 * num_2

  elif sinalOperacao == "/" or sinalOperacao == 4:
    resultado = num_1 / num_2

  else:
    print("O sinal inserido é inválido!")

  return resultado

funcaoCalculadora(100, 20, 4)
  