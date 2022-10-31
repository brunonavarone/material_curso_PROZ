qtd_rodas = 2
qtd_pessoas = 0
peso_carro = 0

if qtd_rodas <= 3:
    print("Veículo da categoria A")

elif qtd_rodas == 4 and qtd_pessoas <= 8 and peso_carro <= 3500:
    print("Este veículo possui 4 rodas, suporta até 8 pessoas e seu peso máximo é de até 3500 kg - Categoria B")

elif qtd_rodas >= 4 and peso_carro >= 500 and peso_carro <= 6000:
    print("Este carro possui 4 rodas ou mais e seu peso está entre 500 kg e 6000 kg - Categoria C")

elif qtd_rodas >= 4 and qtd_pessoas > 8:
    print("Este carro possui 4 rodas ou mais e consegue carregar mais de 8 pessoas - Categoria D")

elif qtd_rodas >= 4 and peso_carro > 6000:
    print("Este veículo possui 4 rodas ou mais e seu peso é maior que 6000 kg - Categoria E")