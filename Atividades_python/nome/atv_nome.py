def dizAniversario():
  anoCerto = False
  print("Digite seu nome: ")
  nome = input()
  while(anoCerto == False):
   try:
     print("Digite o ano em que você nasceu: ")
     anoNascimento = int(input())
     if(anoNascimento < 1922):
       print("Ano de nascimento incorreto! Digite um número maior ou igual a 1922 e menor ou igual a 2021!")

     elif(anoNascimento > 2021):
       print("Ano de nascimento incorreto! Digite um número menor ou igual a 2021 ou igual ou maior a 1922")
  
     else:
       anoCerto = True

   except:
     print("Caracter inválido! Digite um número")

  idade = 2022 - anoNascimento
  print('Olá, ' + str(nome) + '.' + "\nVocê completou ou completará " + str(idade) + " anos no ano de 2022!")     

dizAniversario()