# --- 1 ---
"""
Sequência Lógica: É a ordem correta pela qual as ações devem ser 
                  realizadas para resolver um problema.
Instruções: São os comandos individuais que o programa executa por ordem.
Entrada e Saída de Dados: 
  - A entrada é receber dados do utilizador (ex: input()).
  - A saída é mostrar resultados no ecrã (ex: print()).
"""

# --- 3 ---
print()
print("---3---")
nome = input("Introduza o seu nome: ")
print(f"- Olá, {nome}! Bem-vinda(o) ao mundo da programação!")

# --- 4 ---
print()
print("---4---")
cor = input("Qual é a tua cor favorita? ")
resposta = input(f"Tens a certeza que {cor} é a tua cor favorita? (sim/nao) ")

if resposta == "sim":
    print(f"A tua cor favorita é {cor}")
    
if resposta == "nao":
    cor_verdadeira = input("Então qual é a tua verdadeira cor favorita? ")
    print(f"- Afinal a tua cor favorita é {cor_verdadeira}")

# --- 5 ---
print()
print("---5---")
nome = input("Introduza o seu nome: ")
idade = input("Introduza a sua idade: ")
cidade = input("Introduza a sua cidade: ")
print(f"- Olá {nome} com {idade} anos, de {cidade}!")

# --- 6 ---
print()
print("---6---")
num1 = float(input("Introduza o primeiro número: ")) #   Lê o valor, converte para inteiro (int) e armazena na variável 'num1'.
num2 = float(input("Introduza o segundo número: ")) #   Lê o valor, converte para inteiro (int) e armazena na variável 'num2'.
soma = num1 + num2 #   Adiciona os dois números e armazena o resultado na variável 'soma'.
print(f"- A soma de {num1} e {num2} é = {soma}") # Mostra o resultado no ecrã. A f string permite injetar os valores das variáveis diretamente no texto usando chaves {}.

# --- 7 ---
print()
print("---7---")
n1 = float(input("Introduza a primeira nota: ")) #  Converte para inteiro (int) e armazena na variável 'n1'.
n2 = float(input("Introduza a segunda nota: ")) #  Converte para inteiro (int) e armazena na variável 'n2'.
n3 = float(input("Introduza a terceira nota: ")) #  Converte para inteiro (int) e armazena na variável 'n3'.
media = (n1 + n2 + n3) / 3 # Calcula a média das três notas e armazena o resultado na variável 'media'.
print(f"- A média das notas {n1}, {n2} e {n3} é = {media}") # Mostra o resultado no ecrã com 2 casas decimais.


# --- 8 ---
print()
print("---8---")
comp = float(input("Introduza o comprimento do retângulo: ")) # Converte para inteiro (int) e armazena na variável 'comp'.
alt = float(input("Introduza a altura do retângulo: ")) # Converte para inteiro (int) e armazena na variável 'alt'.
area = comp * alt # Calcula a área do retângulo e armazena o resultado na variável 'area'.
print(f"- A área do retângulo com comprimento {comp} e altura {alt} é = {area}") # Mostra o resultado no ecrã.

# --- 9 ---
print()
print("---9---")
preco = float(input("Introduza o preço do produto: ")) # Converte para inteiro (int) e armazena na variável 'preco'.
desconto = float(input("Introduza o desconto em %: ")) # Converte para inteiro (int) e armazena na variável 'desconto'.
preco2 = preco - (preco * (desconto / 100)) # Calcula o preço final após o desconto e armazena o resultado na variável 'preco2'.
print(f"- O preço final do produto de {preco} com desconto de {desconto}% é = {preco2}") # Mostra o resultado no ecrã.
