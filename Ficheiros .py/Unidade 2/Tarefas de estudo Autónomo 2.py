# --- 1. Soma de duas variáveis ---
print("\n--- 1 ---")
valor1 = 8
valor2 = 2
print(f"A soma de {valor1} e {valor2} é = {valor1 + valor2}")


# --- 2. Cálculo da Idade ---
print("\n--- 2 ---")
ano_nascimento = 2008
ano_atual = 2026
idade = ano_atual - ano_nascimento

# Juntar strings com '+'
print("A tua idade é " + str(idade) + " anos.")


# --- 3. Conversor Celsius para Fahrenheit ---
print("\n--- 3 ---")
temperatura_celsius = 28.0
# Fórmula: F = 1.8 * C + 32
temperatura_fahrenheit = 1.8 * temperatura_celsius + 32
print(f"A temperatura de {temperatura_celsius}ºC equivale a {temperatura_fahrenheit}ºF")


# --- 4. Grilos (Cricris por minuto) ---
print("\n--- 4 ---")
cricris_por_minuto = 80 # Variável do tipo inteiro
# Fórmula: T = 40 + c/4
temperatura_grilos = 40 + cricris_por_minuto / 4
print(f"Com {cricris_por_minuto} cricris por minuto, a temperatura é de {temperatura_grilos}ºF")


# ==========================================
# DESAFIOS
# ==========================================

# --- Desafio 1: Produto e Soma de Variáveis ---
print("\n--- Desafio 1 ---")
a = 5
b = 10
c = 15

produto = a * b
soma = a + b + c
media = (a + b + c) / 3

print(f"Produto de a e b: {produto}")
print(f"Soma de a, b e c: {soma}")
print(f"Média de a, b e c: {media}")


# --- Desafio 2: Conversor de Moeda Dinâmico ---
print("\n--- Desafio 2 ---")
euros = float(input("Introduza o valor em euros (€): "))
taxa_cambio = float(input("Introduza a taxa de câmbio atual (ex: 1.10 para dólares): "))

dolares = euros * taxa_cambio
print(f"O valor de {euros}€ convertido é = {dolares}$")


# --- Desafio 3: Verificação de Paridade ---
print("\n--- Desafio 3 ---")
# O resto da divisão por 2 (módulo %) de um número par é sempre 0
numero = 14 

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")


# --- Desafio 4: Cálculo de IMC ---
print("\n--- Desafio 4 ---")
# IMC = peso / (altura * altura)
peso = float(input("Introduza o seu peso (kg): "))
altura = float(input("Introduza a sua altura (metros, ex: 1.75): "))

imc = peso / (altura * altura)
print(f"O teu IMC é {imc}.")


# --- Desafio 5: Identificação de Múltiplos ---
print("\n--- Desafio 5 ---")
var_a = 20
var_b = 5

if var_a % var_b == 0:
    print(f"O número {var_a} é múltiplo de {var_b}.")
else:
    print(f"O número {var_a} não é múltiplo de {var_b}.")
