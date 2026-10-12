numero_linhas = int(input("Digite o número de linhas da pirâmide: "))
linha = ""

for i in range(1, numero_linhas + 1):
    linha += f"{i}"
    print(linha)
    