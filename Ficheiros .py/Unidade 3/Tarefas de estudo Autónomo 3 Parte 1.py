# --- 1 ---
"""
Estruturas de Controlo: Permitem ramificar o código, criando fluxos de execução 
                        diferentes consoante certas condições lógicas (True/False).
Tipos:
  - Simples (if): Executa caso a condição seja verdadeira.
  - Composta (if-else): Executa uma ação se True e outra alternativa se False.
  - Múltipla (if-elif-else): Testa condições em cadeia.
  - Aninhada: Estruturas de controlo dentro de outras estruturas.
"""

# --- 2 ---
print("\n--- 2 ---")
num = int(input("Introduza um número: "))
if num % 2 == 0:
    print(f"- O número {num} é par.")
else:
    print(f"- O número {num} é ímpar.")

# --- 3 ---
print("\n--- 3 ---")
idade = int(input("Introduza a sua idade: "))
if 13 <= idade <= 19:
    print("- És adolescente.")
else:
    print("- Não és adolescente.")

# --- 4 ---
print("\n--- 4 ---")
idade = int(input("Introduza a idade para o bilhete: "))
if idade == 100 or idade < 5:
    print("- Preço: Grátis")
elif 5 <= idade <= 10 or idade >= 65:
    print("- Preço: €5")
elif 11 <= idade <= 64:
    print("- Preço: €20")


# --- 5 ---
print("\n--- 5 ---")
ano = int(input("Introduza um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"- O ano {ano} é bissexto.")
else:
    print(f"- O ano {ano} não é bissexto.")

# ==========================================
# DESAFIOS
# ==========================================

# --- 6 ---
print("\n--- 6 ---")
numero = input("Introduza o número de telemóvel (9 dígitos): ")
if not numero.isnumeric():
    print("- Inválido: contém letras ou outros caracteres.")
elif len(numero) != 9:
    print("- Inválido: não tem 9 dígitos.")
elif numero[0] != '9':
    print("- Inválido: não começa por 9.")
else:
    print("- Número válido!")

# --- 7 ---
print("\n--- 7 ---")
n1 = float(input("Introduza a primeira nota: "))
n2 = float(input("Introduza a segunda nota: "))
n3 = float(input("Introduza a terceira nota: "))
media = (n1 + n2 + n3) / 3

if n1 < 7.5 or n2 < 7.5 or n3 < 7.5:
    print(f"- Reprovado: nota inferior a 7.5. Média = {media}")
elif media < 9.5:
    print(f"- Reprovado: média inferior a 9.5. Média = {media}")
else:
    print(f"- Aprovado! Média = {media}")

# --- 8 ---
print("\n--- 8 ---")
l1 = float(input("Introduza o lado 1: "))
l2 = float(input("Introduza o lado 2: "))
l3 = float(input("Introduza o lado 3: "))

if l1 >= l2 and l1 >= l3:
    hip = l1
    c1 = l2
    c2 = l3
elif l2 >= l1 and l2 >= l3:
    hip = l2
    c1 = l1
    c2 = l3
else:
    hip = l3
    c1 = l1
    c2 = l2

if (c1**2 + c2**2) == hip**2:
    print("- É um triângulo retângulo.")
else:
    print("- Não é um triângulo retângulo.")

# --- 9 ---
print("\n--- 9 ---")
x = float(input("Introduza a coordenada X: "))
y = float(input("Introduza a coordenada Y: "))
raio = float(input("Introduza o raio da circunferência: "))

if (x**2 + y**2) <= (raio**2):
    print("- O ponto está dentro da circunferência.")
else:
    print("- O ponto está fora da circunferência.")

# --- 10 ---
print("\n--- 10 ---")
num1 = float(input("Introduza o primeiro número: "))
operação = input("Introduza a operação (+, -, *, /): ")
num2 = float(input("Introduza o segundo número: "))

if operação == '+':
    print(f"- Resultado: {num1 + num2}")
elif operação == '-':
    print(f"- Resultado: {num1 - num2}")
elif operação == '*':
    print(f"- Resultado: {num1 * num2}")
elif operação == '/':
    if num2 == 0:
        print("- Erro: divisão por zero.")
    else:
        print(f"- Resultado: {num1 / num2}")
else:
    print("- Operação inválida.")