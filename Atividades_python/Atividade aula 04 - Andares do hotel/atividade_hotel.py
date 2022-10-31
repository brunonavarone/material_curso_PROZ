numeroAndares = 20
print("Exercício com o for")
for i in range(numeroAndares, 0, -1):
  if i != 13:
    print(i)

print("\n----seprando exercícios---\n")
print("Exercício com o while")

while numeroAndares > 0:
  if numeroAndares != 13:
    print(numeroAndares)
  numeroAndares -= 1

print("\n---seprando exercícios---\n")
print("Exercício com as palavras-chave")
numeroAndares = 20
for i in range(numeroAndares, 0, -1):
  if i == 13:
    continue
  if i == 21:
    break
  print(i)